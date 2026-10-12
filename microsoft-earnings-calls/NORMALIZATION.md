# How the transcripts were normalized

All 49 transcripts use the same output contract: **one fiscal-quarter document per UTF-8 TXT file, without a BOM, using LF line endings and exactly one final newline**.

Normalization is deterministic text extraction and whitespace cleanup. It uses Python's standard library, with no language model, OCR, summarization, translation, or spelling correction. The eight DOCX downloads are retained unchanged; the 41 GraphRAG TXT members are retained byte-for-byte after extraction from their source ZIP.

## Source extraction

| Source | Extraction |
| --- | --- |
| GraphRAG: 41 TXT files | Read each unmodified `originals/TranscriptFYxxQy.txt` extracted from the source ZIP and decode it as UTF-8, accepting an optional initial UTF-8 BOM. Map the quarter in the original filename to `FYxxQy.txt`. No rescraping or re-extraction from another source. |
| Investor Relations: eight DOCX files | Open the DOCX as an OOXML ZIP and read `word/document.xml`. Walk body paragraphs, including table-cell paragraphs, in document order. Concatenate `w:t` text nodes, retain `w:tab` as a tab and `w:br`/`w:cr` as line breaks, and place a blank line between paragraphs. |

Only the Word document body is extracted. Fonts, styles, layout, images, headers, footers, comments, and document metadata are not included in the text output. Table-cell text is retained, but table geometry is not. The supplied calls are text documents; no OCR is performed.

## Common cleanup applied to every transcript

1. Convert CRLF and standalone CR line endings to LF.
2. Replace non-breaking spaces (`U+00A0`) with ordinary spaces.
3. Remove trailing whitespace on each line.
4. Collapse runs of three or more newlines to two, retaining a single blank separator line.
5. Remove outer blank lines and add exactly one final LF.
6. Encode as UTF-8 without a BOM and write `corpus/FYxxQy.txt`.

Internal tabs, ordinary spaces, capitalization, punctuation, source typos, speaker labels, financial figures, and dates are not otherwise changed. No Unicode NFC/NFKC conversion or smart-quote substitution is performed. The script checks that the sequence of non-whitespace characters is identical before and after common cleanup.

These rules standardize encoding, file naming, and whitespace; they **do not impose a uniform speaker-turn or paragraph schema** on historically different transcripts. Apart from the blank-line cleanup described above, existing line boundaries are retained; paragraphs are not semantically reconstructed.

## Reproduce or verify

From the package folder, with Python 3 installed:

```powershell
python .\tools\normalize.py --check
```

This checks that the retained originals contain exactly the expected 41 TXT files and eight DOCX files, re-extracts and normalizes them in memory, compares the normalized bytes with the 49 corpus TXT files, and checks for missing or extra files. It does not change files or independently authenticate the originals against their download sources.

To intentionally rebuild the normalized outputs from the retained originals:

```powershell
python .\tools\normalize.py
```

This rewrites `corpus/*.txt` from the retained originals, including any missing TXT files. It does not modify originals, access the network, install packages, or build a retrieval index.

## Limits

The source transcripts retain their original wording and any source errors. Extraction is not a manual editorial correction or an independent verification of financial statements. Fiscal quarters are assigned from the source filenames, not inferred from calendar dates. No questions, answers, labels, embeddings, chunks, graph structures, or benchmark scores were generated.
