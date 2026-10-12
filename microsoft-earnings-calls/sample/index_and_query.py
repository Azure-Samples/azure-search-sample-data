# /// script
# requires-python = ">=3.10"
# dependencies = ["azure-search-documents==11.6.0", "azure-identity==1.26.0"]
#
# [[tool.uv.index]]
# url = "https://pypi.org/simple/"
# default = true
# ///

import argparse
import os
from pathlib import Path
import time
import uuid

from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchableField,
    SearchFieldDataType,
    SearchIndex,
    SimpleField,
)


def main():
    parser = argparse.ArgumentParser(description="Index and search earnings-call transcripts.")
    parser.add_argument("--use-key", action="store_true", help="Use AZURE_SEARCH_ADMIN_KEY instead of Microsoft Entra ID.")
    args = parser.parse_args()

    corpus = Path(__file__).resolve().parent.parent / "corpus"
    documents = [
        {"id": path.stem, "quarter": path.stem, "content": path.read_text(encoding="utf-8")}
        for path in sorted(corpus.glob("*.txt"))
    ]
    if not documents or any(not document["content"].strip() for document in documents):
        raise ValueError(f"Expected nonempty transcripts in {corpus}")
    print(f"Loaded {len(documents)} transcripts.")

    endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT", "").strip()
    if not endpoint:
        parser.error("Set AZURE_SEARCH_ENDPOINT.")
    if args.use_key:
        key = os.environ.get("AZURE_SEARCH_ADMIN_KEY", "").strip()
        if not key:
            parser.error("--use-key requires AZURE_SEARCH_ADMIN_KEY.")
        credential = AzureKeyCredential(key)
    else:
        credential = DefaultAzureCredential()

    index_name = f"earnings-calls-{uuid.uuid4().hex[:8]}"
    print(f"Index: {index_name} (retained after this run)")
    with SearchIndexClient(endpoint, credential) as indexes:
        indexes.create_index(
            SearchIndex(
                name=index_name,
                fields=[
                    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
                    SimpleField(name="quarter", type=SearchFieldDataType.String, filterable=True, sortable=True),
                    SearchableField(name="content", type=SearchFieldDataType.String, analyzer_name="en.microsoft"),
                ],
            )
        )

    with SearchClient(endpoint, index_name, credential) as search:
        for start in range(0, len(documents), 10):
            results = search.upload_documents(documents[start : start + 10])
            failures = [f"{result.key}: {result.error_message}" for result in results if not result.succeeded]
            if failures:
                raise RuntimeError("Indexing failed: " + "; ".join(failures))

        # Successful uploads can take a few seconds to become searchable.
        for attempt in range(30):
            if search.get_document_count() == len(documents):
                break
            time.sleep(2)
        else:
            raise TimeoutError(f"Not all transcripts became searchable in index {index_name}.")

        for query, query_filter in [
            ("Azure revenue", None),
            ("cloud growth", None),
            ("Copilot", "quarter eq 'FY26Q4'"),
        ]:
            print(f"\nQuery: {query}" + (f" [{query_filter}]" if query_filter else ""))
            results = list(
                search.search(
                    search_text=query,
                    filter=query_filter,
                    select=["quarter"],
                    highlight_fields="content",
                    top=3,
                )
            )
            if not results:
                print("  No matches.")
            for result in results:
                highlights = result.get("@search.highlights", {}).get("content", [])
                snippet = " ".join(highlights).replace("\n", " ")[:300]
                print(f"  {result['quarter']} (score {result['@search.score']:.3f}): {snippet}")


if __name__ == "__main__":
    main()
