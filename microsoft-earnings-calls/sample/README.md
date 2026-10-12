# Index and query the transcripts

These two single-file samples load the adjacent `corpus/` folder into Azure AI Search and run three keyword queries. Each transcript becomes one search document with `id`, `quarter`, and searchable `content` fields. The last query filters to FY26 Q4. These are illustrative queries, not a scored evaluation set; no embeddings or language-model service is required.

## Prerequisites

Use an existing Azure AI Search service with API-key authentication enabled, an admin key, and capacity for one additional index. The samples do not provision a service. A non-dry run creates a uniquely named `earnings-calls-*` index. If creation succeeds, that index remains in place, including if a later step fails. Existing indexes are not updated or deleted. Service charges may apply; delete the printed index in the Azure portal when finished.

For Python, install [uv](https://docs.astral.sh/uv/) and Python 3.10 or later. For C#, install the [.NET 10 SDK or later](https://learn.microsoft.com/dotnet/core/sdk/file-based-apps). Dependencies are declared inside each file and restored from Microsoft's package-feed proxy; no project file or separate dependency manifest is needed.

## Run either sample

From this `sample` folder, set these environment variables in PowerShell. Use your own service endpoint and admin key; do not save the key in a script or commit it.

```powershell
$env:AZURE_SEARCH_ENDPOINT = "https://<service-name>.search.windows.net"
$env:AZURE_SEARCH_ADMIN_KEY = "<admin-key>"

uv run .\index_and_query.py
# Or:
dotnet run .\index_and_query.cs
```

Both samples locate `corpus/` relative to their source file, not the working directory. Keep the file in this folder alongside the dataset layout. They upload in batches of ten, check per-document indexing results, wait up to roughly a minute for the document count to catch up, and print up to three matching quarters with scores and highlighted snippets for each query. Authentication, upload, and query failures stop the run.

To read the local corpus without contacting Azure, omit the environment variables and run either command below. Dependency restoration can still access the package feed.

```powershell
uv run .\index_and_query.py --dry-run
dotnet run .\index_and_query.cs -- --dry-run
```
