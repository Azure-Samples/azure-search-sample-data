# How the transcripts were normalized

All 49 transcripts use the same output contract: **one fiscal-quarter document per UTF-8 TXT file, without a BOM, using LF line endings and exactly one final newline**.

Normalization was deterministic text extraction and whitespace cleanup using Python's standard library, with no language model, OCR, summarization, translation, or spelling correction. Original downloads are not included in this package; see the source links in `README.md`.

## Source extraction

| Source | Extraction |
| --- | --- |
| GraphRAG: 41 TXT files | Read each `txt/TranscriptFYxxQy.txt` member from the source ZIP and decode it as UTF-8, accepting an optional initial UTF-8 BOM. Map the quarter in the original filename to `FYxxQy.txt`. No rescraping or re-extraction from another source. |
| Investor Relations: eight DOCX files | Open the DOCX as an OOXML ZIP and read `word/document.xml`. Walk body paragraphs, including table-cell paragraphs, in document order. Concatenate `w:t` text nodes, retain `w:tab` as a tab and `w:br`/`w:cr` as line breaks, and place a blank line between paragraphs. |

Only the Word document body is extracted. Fonts, styles, layout, images, headers, footers, comments, and document metadata are not included in the text output. Table-cell text is retained, but table geometry is not. The supplied calls are text documents; no OCR is performed.

## Common cleanup applied to every transcript

1. Convert CRLF and standalone CR line endings to LF.
2. Replace non-breaking spaces (`U+00A0`) with ordinary spaces.
3. Remove trailing whitespace on each line.
4. Collapse runs of three or more newlines to two, retaining a single blank separator line.
5. Remove outer blank lines and add exactly one final LF.
6. Encode as UTF-8 without a BOM and write `corpus/FYxxQy.txt`.

Internal tabs, ordinary spaces, capitalization, punctuation, source typos, speaker labels, financial figures, and dates are not otherwise changed. No Unicode NFC/NFKC conversion or smart-quote substitution was performed. The sequence of non-whitespace characters was checked against each source during processing.

These rules standardize encoding, file naming, and whitespace; they **do not impose a uniform speaker-turn or paragraph schema** on historically different transcripts. Apart from the blank-line cleanup described above, existing line boundaries are retained; paragraphs are not semantically reconstructed.

## Limits

The source transcripts retain their original wording and any source errors. Extraction is not a manual editorial correction or an independent verification of financial statements. Fiscal quarters are assigned from the source filenames, not inferred from calendar dates. No questions, answers, labels, embeddings, chunks, graph structures, or benchmark scores were generated. Without the original downloads in this package, the normalization cannot be verified or rebuilt from this package alone.
