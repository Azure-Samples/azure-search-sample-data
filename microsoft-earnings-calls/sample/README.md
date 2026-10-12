# Index and query the transcripts

These two single-file samples load the adjacent `corpus/` folder into Azure AI Search and run three keyword queries. Each transcript becomes one search document with `id`, `quarter`, and searchable `content` fields. The last query filters to FY26 Q4. These are illustrative queries, not a scored evaluation set; no embeddings or language-model service is required.

## Prerequisites

Use an existing Azure AI Search service with capacity for one additional index. The samples do not provision a service. Each sample creates a uniquely named `earnings-calls-*` index. If creation succeeds, that index remains in place, including if a later step fails. Existing indexes are not updated or deleted. Service charges may apply; delete the printed index in the Azure portal when finished.

For Python, install [uv](https://docs.astral.sh/uv/) and Python 3.10 or later. For C#, install the [.NET 10 SDK or later](https://learn.microsoft.com/dotnet/core/sdk/file-based-apps). Dependencies are declared inside each file and restored from public PyPI (Python) or NuGet.org (C#); no project file or separate dependency manifest is needed.

## Run with keyless authentication (default)

Both samples use `DefaultAzureCredential` from Azure Identity unless `--use-key` is specified. The search service must have [role-based access enabled](https://learn.microsoft.com/azure/search/search-security-enable-roles). The identity running the sample needs **Search Service Contributor** to create the index and **Search Index Data Contributor** to upload and query documents, assigned at the search-service scope. See [Azure AI Search roles](https://learn.microsoft.com/azure/search/search-security-rbac).

For local development, sign in with Azure CLI and run either sample from this `sample` folder:

```powershell
az login --tenant "<tenant-id>"
$env:AZURE_SEARCH_ENDPOINT = "https://<service-name>.search.windows.net"

uv run .\index_and_query.py
# Or:
dotnet run .\index_and_query.cs
```

On an Azure host with a system-assigned managed identity, `DefaultAzureCredential` can use that identity without a local sign-in; it needs the same search roles. Authentication or authorization failures stop the run rather than falling back to an API key. `AZURE_SEARCH_ADMIN_KEY` is ignored unless `--use-key` is specified.

## Optional API-key authentication

If your service allows API-key authentication, explicitly opt in with `--use-key` and provide an admin key. A query key cannot create an index or upload documents. Do not save the admin key in a script or commit it.

```powershell
$env:AZURE_SEARCH_ENDPOINT = "https://<service-name>.search.windows.net"
$env:AZURE_SEARCH_ADMIN_KEY = "<admin-key>"

uv run .\index_and_query.py --use-key
# Or:
dotnet run .\index_and_query.cs -- --use-key
```

## Sample behavior

Both samples locate `corpus/` relative to their source file, not the working directory. Keep the file in this folder alongside the dataset layout. They upload in batches of ten, check per-document indexing results, wait up to roughly a minute for the document count to catch up, and print up to three matching quarters with scores and highlighted snippets for each query. Authentication, upload, and query failures stop the run.
