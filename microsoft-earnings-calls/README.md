# Microsoft Earnings Call Graph Retrieval Benchmark

This dataset contains **49 Microsoft earnings-call transcripts, covering every fiscal quarter from FY14 Q4 through FY26 Q4**. It is a document corpus for benchmarking graph-based retrieval and retrieval-augmented generation (RAG): finding relevant information across calls and synthesizing answers grounded in that information.

The corpus combines 41 transcripts from the [Microsoft GraphRAG benchmarking datasets repository](https://github.com/microsoft/graphrag-benchmarking-datasets) with eight newer transcripts from [Microsoft Investor Relations](https://www.microsoft.com/en-us/investor/events/default). These are fiscal quarters, not calendar quarters.

**Start with `corpus/` or `corpus.jsonl`.** Both contain the same normalized transcript text, ready for parsing. Keep the source files, license, and notices together when redistributing the dataset.

## What's included

| Path | Contents |
| --- | --- |
| `corpus/` | 49 UTF-8 plain-text files, one per quarter, named `FY14Q4.txt` through `FY26Q4.txt`. |
| `corpus.jsonl` | The same 49 transcripts as one JSON object per line, with fiscal-quarter identifiers and source metadata. |
| `originals/MSFT Input Text.zip` | Unmodified GraphRAG archive containing 41 TXT transcripts, FY14 Q4 through FY24 Q4. |
| `originals/TranscriptFY25Q1.docx` through `originals/TranscriptFY26Q4.docx` | Eight unmodified Investor Relations Word documents, FY25 Q1 through FY26 Q4. |
| `originals/GraphRAG-LICENSE.txt` | Repository license: Community Data License Agreement - Permissive - Version 2.0. |
| `originals/GraphRAG-NOTICE.md` | Original repository attribution and source notices. It describes multiple repository datasets, not all of which are included here. |
| `LICENSE` | Community Data License Agreement - Permissive - Version 2.0 for this dataset. |
| `NORMALIZATION.md` | Exact text-conversion and cleanup rules, preservation guarantees, and limitations. |
| `tools/normalize.py` | Reproducible, Python-standard-library-only normalization and verification script; no downloads or model calls. |

Source provenance is stored directly in `corpus.jsonl`; no separate manifest is needed. The GraphRAG source files and notices are pinned to repository commit `bc187ace7ccc2c942155f1160a892a3ccb257179`. The eight Investor Relations originals were downloaded on October 8, 2026; their URLs can change, so the retained bytes and hashes identify this package's version.

## What the transcripts contain

The calls contain management's prepared remarks and analyst question-and-answer discussions, including financial performance, business segments, product strategy, and outlook. Speakers, dates, figures, and wording are retained as present in the source text.

This package contains source documents, **not a prebuilt knowledge graph or a scored evaluation set**. It does not include benchmark questions, reference answers, relevance judgments, embeddings, extracted entities, graph edges, or evaluation results. Other datasets and query CSVs in the upstream repository are not included here.

## Parse the data

For file-based ingestion, enumerate only `corpus/*.txt`; do not ingest source notices or original files as additional transcripts. The filename is the document identifier. Each file uses UTF-8 without a byte-order mark, LF line endings, and exactly one final newline.

For record-based ingestion, read `corpus.jsonl` as UTF-8 JSON Lines. Each record has these fields:

| Field | Meaning |
| --- | --- |
| `id` | Stable quarter identifier, such as `FY25Q1`. |
| `fiscal_year`, `fiscal_quarter` | Numeric fiscal year and quarter, such as `2025` and `1`. |
| `text` | Complete normalized transcript text, identical to the corresponding TXT file. |
| `text_file` | Relative path to that TXT file. |
| `source_id`, `source_url` | Source identifier and exact download URL. |
| `original_file` | Relative path to the retained original download. |
| `archive_member` | Original TXT member inside the GraphRAG ZIP, or `null` for a DOCX source. |
| `original_sha256` | SHA-256 of the unmodified original download; the ZIP hash is shared by its 41 records. |
| `downloaded_at_utc` | UTC collection timestamp of the original download. |
| `normalization_version` | Transformation version, currently `1`; see `NORMALIZATION.md`. |
| `sha256` | SHA-256 of the corresponding normalized TXT file's UTF-8 bytes. |

Choose one ingestion representation; loading both TXT and JSONL would duplicate the documents. Chunking and speaker/entity extraction are left to the consuming system.

## License and attribution

The complete dataset, including the GraphRAG and Investor Relations transcripts, is released under the [Community Data License Agreement - Permissive - Version 2.0](LICENSE). Include the license text when sharing the data, as required by its terms. The retained GraphRAG license and attribution notices are in `originals/GraphRAG-LICENSE.txt` and `originals/GraphRAG-NOTICE.md`; the notices describe other upstream datasets that are not part of this package. Per-record source links and original-file hashes are in `corpus.jsonl`.
