# Microsoft Earnings Call Graph Retrieval Benchmark

This dataset contains **49 Microsoft earnings-call transcripts, covering every fiscal quarter from FY14 Q4 through FY26 Q4**. It is a document corpus for benchmarking graph-based retrieval and retrieval-augmented generation (RAG): finding relevant information across calls and synthesizing answers grounded in that information.

The corpus combines 41 transcripts from the [Microsoft GraphRAG benchmarking datasets repository](https://github.com/microsoft/graphrag-benchmarking-datasets) with eight newer transcripts from [Microsoft Investor Relations](https://www.microsoft.com/en-us/investor/events/default). These are fiscal quarters, not calendar quarters.

**Start with `corpus/`** for normalized transcript text, ready for parsing. Keep the license with the data when redistributing it.

## What's included

| Path | Contents |
| --- | --- |
| `corpus/` | 49 UTF-8 plain-text files, one per quarter, named `FY14Q4.txt` through `FY26Q4.txt`. |
| `originals/TranscriptFY14Q4.txt` through `originals/TranscriptFY24Q4.txt` | 41 original GraphRAG TXT transcripts, extracted byte-for-byte from the source archive. |
| `originals/TranscriptFY25Q1.docx` through `originals/TranscriptFY26Q4.docx` | Eight unmodified Investor Relations Word documents, FY25 Q1 through FY26 Q4. |
| `LICENSE` | Community Data License Agreement - Permissive - Version 2.0 for this dataset. |
| `NORMALIZATION.md` | Exact text-conversion and cleanup rules, preservation guarantees, and limitations. |
| `tools/normalize.py` | Reproducible, Python-standard-library-only normalization and verification script; no downloads or model calls. |

The 41 GraphRAG originals come from [`data/MSFT Input Text.zip`](https://github.com/microsoft/graphrag-benchmarking-datasets/blob/bc187ace7ccc2c942155f1160a892a3ccb257179/data/MSFT%20Input%20Text.zip) at repository commit `bc187ace7ccc2c942155f1160a892a3ccb257179`. The eight Investor Relations originals were downloaded on October 8, 2026; their source links may change, so the retained documents identify this package's version.

## What the transcripts contain

The calls contain management's prepared remarks and analyst question-and-answer discussions, including financial performance, business segments, product strategy, and outlook. Speakers, dates, figures, and wording are retained as present in the source text.

This package contains source documents, **not a prebuilt knowledge graph or a scored evaluation set**. It does not include benchmark questions, reference answers, relevance judgments, embeddings, extracted entities, graph edges, or evaluation results. Other datasets and query CSVs in the upstream repository are not included here.

## Parse the data

For file-based ingestion, enumerate only `corpus/*.txt`; do not ingest original files as additional transcripts. The filename is the document identifier. Each file uses UTF-8 without a byte-order mark, LF line endings, and exactly one final newline.

The filename is the fiscal-quarter identifier. Chunking and speaker/entity extraction are left to the consuming system.

## License and attribution

The complete dataset, including the GraphRAG and Investor Relations transcripts, is released under the [Community Data License Agreement - Permissive - Version 2.0](LICENSE). Include the license text when sharing the data, as required by its terms. The original transcript files are retained in `originals/`, and their sources are linked above.
