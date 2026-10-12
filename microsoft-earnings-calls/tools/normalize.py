"""Rebuild normalized transcripts from the retained originals; no network calls."""

import argparse
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def docx_text(path):
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    paragraphs = []
    for paragraph in root.findall(".//w:body//w:p", NS):
        chunks = []
        for node in paragraph.iter():
            if node.tag == f"{{{NS['w']}}}t":
                chunks.append(node.text or "")
            elif node.tag == f"{{{NS['w']}}}tab":
                chunks.append("\t")
            elif node.tag in (f"{{{NS['w']}}}br", f"{{{NS['w']}}}cr"):
                chunks.append("\n")
        paragraphs.append("".join(chunks))
    return "\n\n".join(paragraphs)


def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\u00a0", " ")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing.")
    args = parser.parse_args()
    archive_quarters = ["FY14Q4"] + [
        f"FY{year:02}Q{quarter}" for year in range(15, 25) for quarter in range(1, 5)
    ]
    docx_quarters = [f"FY{year:02}Q{quarter}" for year in range(25, 27) for quarter in range(1, 5)]
    quarters = archive_quarters + docx_quarters
    originals = ROOT / "originals"
    archive_path = originals / "MSFT Input Text.zip"
    require({path.name for path in originals.iterdir() if path.is_file()}
            == {"MSFT Input Text.zip"} | {f"Transcript{quarter}.docx" for quarter in docx_quarters},
            "Unexpected or missing original files.")
    with zipfile.ZipFile(archive_path) as archive:
        require({name for name in archive.namelist() if name.endswith(".txt")}
                == {f"txt/Transcript{quarter}.txt" for quarter in archive_quarters},
                "Unexpected or missing archive transcripts.")
        archive_text = {
            quarter: archive.read(f"txt/Transcript{quarter}.txt").decode("utf-8-sig")
            for quarter in archive_quarters
        }
    corpus = ROOT / "corpus"
    expected_files = {f"{quarter}.txt" for quarter in quarters}
    existing_files = {path.name for path in corpus.glob("*.txt")}
    require(not (existing_files - expected_files), "Unexpected TXT files in corpus.")
    if args.check:
        require(existing_files == expected_files, "Missing TXT files in corpus.")
    outputs = []
    for quarter in quarters:
        raw = (archive_text[quarter] if quarter in archive_text
               else docx_text(originals / f"Transcript{quarter}.docx"))
        text = normalize(raw)
        require(re.sub(r"\s", "", raw) == re.sub(r"\s", "", text),
                f"Non-whitespace source characters changed: {quarter}")
        data = text.encode("utf-8")
        path = corpus / f"{quarter}.txt"
        if args.check:
            require(path.read_bytes() == data, f"Normalized file mismatch: {path}")
        else:
            outputs.append((path, data))
    if not args.check:
        corpus.mkdir(exist_ok=True)
        for path, data in outputs:
            path.write_bytes(data)
    print(f"{'Verified' if args.check else 'Normalized'} {len(quarters)} transcripts; "
          "non-whitespace source characters preserved.")


if __name__ == "__main__":
    main()
