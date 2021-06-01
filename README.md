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

## Clinical trials PDF 19

Consists of 19 PDF files used in AI enrichment lessons. This data set can be used in AI enrichment pipelines on the free tier, using the free allocation of daily transactions per indexer.

## Clinical trials PDF 107

Consists of 107 PDF files used in knowledge mining labs and tutorials. Processing this quantity of documents requires an attached Cognitive Services all-in-one resource.

## Hotels-json-documents

This sample data set consists of 5 JSON documents containing structured JSON, used for evaluating or testing JSON blob indexing. Each file consists of hotel information, an address complex field, and a rooms complex collection. The blob indexer can detect and match this JSON structure through equivalent fields in a search index.

## Hotels data

Fictitious demo data for quickstarts, tutorials, and code examples. This is the default data set for most Azure Cognitive Search samples. It consists of 50 hotels across the United States and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier.

Hotels demo data is provided in multiple formats to support different consumption models. The data is identical regardless of how you load it. Data files are in JSON, but there are several versions depending on whether you are uploading it Azure Cosmos DB or pushing it to an index in Azure Cognitive Search. 

Use the following files to create the hotels sample on your search service:

+ **Hotels.postman_collection.json** - Using Postman, import this collection to execute requests that create and populate the Hotels index using JSON documents.

+ **Hotels_IndexDefinition.JSON** - A standalone JSON file containing just the index. This index definition is equivalent to the hosted index on azs-playground search service.

+ **HotelsData_toAzureSearch.JSON** - A standalone JSON file containing documents for 50 hotels and related room information.

+ **HotelsData_toCosmosDB.JSON** - JSON used to populate an Azure Cosmos DB with the Hotels sample data.  This can be used as a data source for an indexer to pull data into the Hotels index.

## HotelReviews

A CSV file provides data consisting of customer reviews of various fictional hotels in Europe. You can use this data in AI enrichment tutorials, applying sentiment analysis, language detection, and text translation. This data set is used in the [Create a knowledge store quickstart](https://docs.microsoft.com/azure/search/knowledge-store-create-portal).

A JSON file provides a skillset that articulate the AI enrichment steps used by the indexer.

## NASA e-books

NASA earth book is used in conceptual examples that explain semantic search and answers. This folder contains a collection of PDFs from NASA's downloadable books site. The folder includes intact versions of entire books as single PDF files. It also includes per-page extractions as separate PDF files for both images and text, as well as text-only pages.