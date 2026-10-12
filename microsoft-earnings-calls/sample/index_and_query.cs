#:package Azure.Search.Documents@11.7.0
#:package Azure.Identity@1.21.0
#:property RestoreSources=https://api.nuget.org/v3/index.json
#:property PublishAot=false

using System.Runtime.CompilerServices;
using Azure;
using Azure.Identity;
using Azure.Search.Documents;
using Azure.Search.Documents.Indexes;
using Azure.Search.Documents.Indexes.Models;
using Azure.Search.Documents.Models;

if (args.Any(arg => arg != "--use-key"))
    throw new ArgumentException("Usage: dotnet run index_and_query.cs -- [--use-key]");

string corpus = Path.GetFullPath(Path.Combine(SourceDirectory(), "..", "corpus"));
var documents = Directory.GetFiles(corpus, "*.txt")
    .OrderBy(path => path, StringComparer.Ordinal)
    .Select(path => new SearchDocument
    {
        ["id"] = Path.GetFileNameWithoutExtension(path),
        ["quarter"] = Path.GetFileNameWithoutExtension(path),
        ["content"] = File.ReadAllText(path, System.Text.Encoding.UTF8)
    })
    .ToList();
if (documents.Count == 0 || documents.Any(document => string.IsNullOrWhiteSpace((string)document["content"])))
    throw new InvalidOperationException($"Expected nonempty transcripts in {corpus}");
Console.WriteLine($"Loaded {documents.Count} transcripts.");

string endpoint = RequiredEnvironment("AZURE_SEARCH_ENDPOINT");
string indexName = $"earnings-calls-{Guid.NewGuid().ToString("N")[..8]}";
SearchIndexClient indexes;
SearchClient search;
if (args.Contains("--use-key"))
{
    var credential = new AzureKeyCredential(RequiredEnvironment("AZURE_SEARCH_ADMIN_KEY"));
    indexes = new SearchIndexClient(new Uri(endpoint), credential);
    search = new SearchClient(new Uri(endpoint), indexName, credential);
}
else
{
    var credential = new DefaultAzureCredential();
    indexes = new SearchIndexClient(new Uri(endpoint), credential);
    search = new SearchClient(new Uri(endpoint), indexName, credential);
}
Console.WriteLine($"Index: {indexName} (retained after this run)");
await indexes.CreateIndexAsync(new SearchIndex(indexName)
{
    Fields =
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SimpleField("quarter", SearchFieldDataType.String) { IsFilterable = true, IsSortable = true },
        new SearchableField("content") { AnalyzerName = LexicalAnalyzerName.EnMicrosoft }
    }
});

foreach (var batch in documents.Chunk(10))
{
    var response = await search.UploadDocumentsAsync(batch);
    var failures = response.Value.Results.Where(result => !result.Succeeded).ToList();
    if (failures.Count > 0)
        throw new InvalidOperationException("Indexing failed: " +
            string.Join("; ", failures.Select(result => $"{result.Key}: {result.ErrorMessage}")));
}

// Successful uploads can take a few seconds to become searchable.
bool ready = false;
for (int attempt = 0; attempt < 30; attempt++)
{
    if ((await search.GetDocumentCountAsync()).Value == documents.Count)
    {
        ready = true;
        break;
    }
    await Task.Delay(TimeSpan.FromSeconds(2));
}
if (!ready)
    throw new TimeoutException($"Not all transcripts became searchable in index {indexName}.");

foreach (var (query, filter) in new (string Query, string? Filter)[]
{
    ("Azure revenue", null),
    ("cloud growth", null),
    ("Copilot", "quarter eq 'FY26Q4'")
})
{
    Console.WriteLine($"\nQuery: {query}" + (filter is null ? "" : $" [{filter}]"));
    var options = new SearchOptions { Filter = filter, Size = 3 };
    options.Select.Add("quarter");
    options.HighlightFields.Add("content");
    var response = await search.SearchAsync<SearchDocument>(query, options);
    bool found = false;
    await foreach (var result in response.Value.GetResultsAsync())
    {
        found = true;
        string snippet = result.Highlights is not null && result.Highlights.TryGetValue("content", out var highlights)
            ? string.Join(" ", highlights).Replace("\n", " ")
            : "";
        Console.WriteLine($"  {result.Document["quarter"]} (score {result.Score:F3}): " +
            snippet[..Math.Min(300, snippet.Length)]);
    }
    if (!found)
        Console.WriteLine("  No matches.");
}

static string SourceDirectory([CallerFilePath] string path = "") => Path.GetDirectoryName(path)!;

static string RequiredEnvironment(string name) =>
    Environment.GetEnvironmentVariable(name)?.Trim() is { Length: > 0 } value
        ? value
        : throw new InvalidOperationException($"Set {name}.");
