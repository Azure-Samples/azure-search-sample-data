# Azure Cognitive Search Sample Data

Data files used in Azure Cognitive Search quickstarts, tutorials, and examples. Use this data as a starting point for exploring search and AI functionality.

Each folder represents a different sample data set.

## AI-enrichment-mixed-media (files for skillsets and AI enrichment)

This sample data is intended for upload to an Azure Blob storage container for AI enrichment examples. The data is a collection of mixed content types including images, Office documents, and text documents in common file formats.

## Caselaw 

The [Caselaw Access Project](https://case.law/bulk/download/) provides public bulk downloads of case data by jurisdiction. Several jurisdictions are freely available without having to request access first. We chose the first one (Arkansas jurisdiction), and then took the first 10 cases.

The file name for this data set is `caselaw-sample.json`.

You can upload this file to Azure Blob storage and use the **Import data** wizard to index the documents. Choose the **JSON Lines** parsing mode.

## Clinical trials JSON

Consists of 8 semi-structured JSON files that you can upload to Azure Blob storage, and then import using the Azure Blob indexer. This data is used in the [Index Azure JSON blobs tutorial](https://docs.microsoft.com/azure/search/search-semi-structured-data).

## Hotels data

Fictitious demo data for quickstarts, tutorials, and code examples. This is the default data set for most Azure Cognitive Search samples. It consists of 50 hotels across the United States and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier.

Hotels demo data is provided in multiple formats to support different consumption models. The data is identical regardless of how you load it. Data files are in JSON, but there are several versions depending on whether you are uploading it Azure Cosmos DB or pushing it to an index in Azure Cognitive Search. 

Use the following files to create the hotels sample on your search service:

+ **Hotels.postman_collection.json** - Using Postman, import this collection to execute requests that create and populate the Hotels index using JSON documents.

+ **Hotels_IndexDefinition.JSON** - A standalone JSON file containing just the index. 

+ **HotelsData_toAzureSearch.JSON** - A standalone JSON file containing documents for 50 hotels and related room information.

+ **HotelsData_toCosmosDB.JSON** - JSON used to populate an Azure Cosmos DB with the Hotels sample data.  This can be used as a data source for an indexer to pull data into the Hotels index.

Alternatively, you can access hosted versions of this data set. 

### Hosted read-only index

There is a staged index populated with the hotels demo data, hosted on a search service, accessed with a query api-key for read-only access to hotel documents.

Endpoint to the index: `https://azs-playground.search.windows.net/indexes/hotels/docs?api-version=2017-11-11&search=*`

query api-key: `EA4510A6219E14888741FCFC19BFBB82`

### Hosted read-only version database

The hotels demo data is also in Azure Cosmos DB. Using the **Import data** wizard, you can create a new Cosmos DB data source based on this connection information. The wizard will ask you for the following three inputs.

Cosmos DB connection string: `AccountEndpoint=https://hotels-docbb.documents.azure.com:443/;AccountKey=4UPsNZyFAjgZ1tzHPGZaxS09XcwLrIawbXBWk6IixcxJoSePTcjBn0mi53XiKWu8MaUgowUhIovOv7kjksqAug==;Database=SampleData`

Database Name: `SampleData`

Collection: `hotels`

## HotelReviews

A CSV file provides data consisting of customer reviews of various fictional hotels in Europe. You can use this data in AI enrichment tutorials, applying sentiment analysis, language detection, and text translation. This data set is used in the [Create a knowledge store quickstart](https://docs.microsoft.com/azure/search/knowledge-store-create-portal).

A JSON file provides a skillset that articulate the AI enrichment steps used by the indexer.