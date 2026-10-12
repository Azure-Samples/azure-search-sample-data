"""Rebuild normalized text and JSONL from the retained originals; no network calls."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
VERSION = 1


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


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
    jsonl_path = ROOT / "corpus.jsonl"
    records = [json.loads(line) for line in jsonl_path.read_text(encoding="utf-8").splitlines()]
    expected = {"FY14Q4"} | {f"FY{year:02}Q{quarter}" for year in range(15, 27) for quarter in range(1, 5)}
    require(len(records) == 49 and {record["id"] for record in records} == expected,
            "Expected exactly 49 unique quarters, FY14 Q4 through FY26 Q4.")
    outputs = []
    for record in records:
        quarter = record["id"]
        require(record["fiscal_year"] == 2000 + int(quarter[2:4])
                and record["fiscal_quarter"] == int(quarter[-1]),
                f"Inconsistent fiscal metadata: {quarter}")
        require(record["normalization_version"] == VERSION,
                f"Unsupported normalization version: {quarter}")
        require(record["text_file"] == f"corpus/{quarter}.txt",
                f"Unexpected output path: {quarter}")
        is_archive = quarter <= "FY24Q4"
        original_file = "originals/MSFT Input Text.zip" if is_archive else f"originals/Transcript{quarter}.docx"
        require(record["original_file"] == original_file,
                f"Unexpected original path: {quarter}")
        original = ROOT / original_file
        require(sha256(original.read_bytes()) == record["original_sha256"],
                f"Original hash mismatch: {original}")
        if is_archive:
            member = f"txt/Transcript{quarter}.txt"
            require(record["archive_member"] == member,
                    f"Unexpected archive member: {quarter}")
            with zipfile.ZipFile(original) as archive:
                raw = archive.read(member).decode("utf-8-sig")
        else:
            require(record["archive_member"] is None,
                    f"DOCX cannot have an archive member: {quarter}")
            raw = docx_text(original)
        text = normalize(raw)
        require(re.sub(r"\s", "", raw) == re.sub(r"\s", "", text),
                f"Non-whitespace source characters changed: {quarter}")
        data = text.encode("utf-8")
        path = ROOT / record["text_file"]
        if args.check:
            require(path.read_bytes() == data, f"Normalized file mismatch: {path}")
            require(record["text"] == text, f"JSONL text mismatch: {quarter}")
            require(record["sha256"] == sha256(data), f"Normalized hash mismatch: {quarter}")
        else:
            record.update(text=text, sha256=sha256(data))
            outputs.append((path, data))
    records.sort(key=lambda record: record["id"])
    jsonl = "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records).encode("utf-8")
    if args.check:
        require(jsonl_path.read_bytes() == jsonl, "JSONL ordering or serialization mismatch.")
        require({path.name for path in (ROOT / "corpus").glob("*.txt")}
                == {f"{quarter}.txt" for quarter in expected},
                "Unexpected or missing TXT files in corpus.")
    else:
        (ROOT / "corpus").mkdir(exist_ok=True)
        for path, data in outputs:
            path.write_bytes(data)
        jsonl_path.write_bytes(jsonl)
    print(f"{'Verified' if args.check else 'Normalized'} 49 transcripts and matching JSONL; non-whitespace source characters preserved.")


if __name__ == "__main__":
    main()
