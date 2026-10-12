# Microsoft Earnings Call Graph Retrieval Benchmark

This dataset contains **49 Microsoft earnings-call transcripts, covering every fiscal quarter from FY14 Q4 through FY26 Q4**. It is a document corpus for benchmarking graph-based retrieval and retrieval-augmented generation (RAG): finding relevant information across calls and synthesizing answers grounded in that information.

The corpus combines 41 transcripts from the [Microsoft GraphRAG benchmarking datasets repository](https://github.com/microsoft/graphrag-benchmarking-datasets) with eight newer transcripts from [Microsoft Investor Relations](https://www.microsoft.com/en-us/investor/events/default). These are fiscal quarters, not calendar quarters.

**Start with `corpus/`** for normalized transcript text, ready for parsing. Keep the license with the data when redistributing it.

## What's included

| Path | Contents |
| --- | --- |
| `corpus/` | 49 UTF-8 plain-text files, one per quarter, named `FY14Q4.txt` through `FY26Q4.txt`. |
| `LICENSE` | Community Data License Agreement - Permissive - Version 2.0 for this dataset. |
| `NORMALIZATION.md` | Text extraction and cleanup procedure, output format, and limitations. |

## Sources

The 41 FY14 Q4–FY24 Q4 transcripts come from [`data/MSFT Input Text.zip`](https://github.com/microsoft/graphrag-benchmarking-datasets/blob/bc187ace7ccc2c942155f1160a892a3ccb257179/data/MSFT%20Input%20Text.zip) in the GraphRAG benchmarking datasets repository at commit `bc187ace7ccc2c942155f1160a892a3ccb257179`. The eight later transcripts came from Microsoft Investor Relations:

| Fiscal quarter | Original transcript |
| --- | --- |
| FY25 Q1 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY25Q1) |
| FY25 Q2 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY25Q2) |
| FY25 Q3 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY25Q3) |
| FY25 Q4 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptQandAFY25q4.docx) |
| FY26 Q1 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY26Q1.docx) |
| FY26 Q2 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptQandAFY26q2) |
| FY26 Q3 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptQandAFY26Q3) |
| FY26 Q4 | [Investor Relations DOCX](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/TranscriptFY26Q4.docx) |

Original downloads are not included; source URLs may change.

## What the transcripts contain

The calls contain management's prepared remarks and analyst question-and-answer discussions, including financial performance, business segments, product strategy, and outlook. Speakers, dates, figures, and wording are retained as present in the source text.

This package contains processed transcripts, **not a prebuilt knowledge graph or a scored evaluation set**. It does not include benchmark questions, reference answers, relevance judgments, embeddings, extracted entities, graph edges, or evaluation results. Other datasets and query CSVs in the upstream repository are not included here.

## Parse the data

For file-based ingestion, enumerate `corpus/*.txt`. Each file uses UTF-8 without a byte-order mark, LF line endings, and exactly one final newline.

The filename is the fiscal-quarter identifier. Chunking and speaker/entity extraction are left to the consuming system.

## License and attribution

The complete dataset, including the GraphRAG and Investor Relations transcripts, is released under the [Community Data License Agreement - Permissive - Version 2.0](LICENSE). Include the license text when sharing the data, as required by its terms. Sources for each transcript are linked above.
