# How the transcripts were normalized

All 49 transcripts use the same output contract: **one fiscal-quarter document per UTF-8 TXT file, without a BOM, using LF line endings and exactly one final newline**. `corpus.jsonl` contains the identical text plus explicit identifiers and source metadata.

Normalization is deterministic text extraction and whitespace cleanup. It uses Python's standard library, with no language model, OCR, summarization, translation, or spelling correction. All original downloads are retained unchanged.

## Source extraction

| Source | Extraction |
| --- | --- |
| GraphRAG ZIP: 41 TXT files | Read each recorded archive member directly and decode it as UTF-8, accepting an optional initial UTF-8 BOM. Map the quarter in the original filename to `FYxxQy.txt`. No rescraping or re-extraction from another source. |
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

## JSONL representation

`corpus.jsonl` has 49 records sorted by quarter identifier. The `text` field matches the complete decoded TXT file, including its final newline. Newlines within `text` are escaped by JSON serialization, so each record occupies one physical line. Non-ASCII transcript characters remain UTF-8 rather than being rewritten as ASCII.

Record identifiers, fiscal-year and fiscal-quarter values, source references, and SHA-256 hashes are metadata, not inserted into the transcript body. Each JSONL record maps its normalized file to the original download, names the ZIP member when applicable, and carries original and normalized hashes, the original collection timestamp, and normalization version `1`. This replaces the separate manifest.

## Reproduce or verify

From the package folder, with Python 3 installed:

```powershell
python .\tools\normalize.py --check
```

This reads provenance from `corpus.jsonl`, verifies original hashes, re-extracts and normalizes the source text in memory, checks each TXT file against its JSONL text and hash, checks JSONL ordering and serialization, and confirms exactly 49 unique quarters with no coverage gaps or extra TXT files. It does not change files.

To intentionally rebuild the normalized outputs from the retained originals:

```powershell
python .\tools\normalize.py
```

This rewrites `corpus/*.txt` and the text and normalized-hash fields in `corpus.jsonl`, retaining its source provenance. Keep `corpus.jsonl`: the script uses it as the source index for rebuilding. It can regenerate missing TXT files but does not recreate a missing source index. It does not modify originals, access the network, install packages, or build a retrieval index.

## Limits

The source transcripts retain their original wording and any source errors. Extraction is not a manual editorial correction or an independent verification of financial statements. Fiscal quarters are assigned from the source filenames and source records, not inferred from calendar dates. No questions, answers, labels, embeddings, chunks, graph structures, or benchmark scores were generated.
