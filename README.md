---
page_type: sample
languages:
- html
products:
- azure
description: "Data files used in Azure Cognitive Search quickstarts, tutorials, and examples. Use this data as a starting point for exploring Azure Search functionality."
urlFragment: azure-search-sample-data
---

# Azure Cognitive Search Sample Data

Data files used in Azure Cognitive Search quickstarts, tutorials, and examples. Use this data as a starting point for exploring search and AI functionality.

Each folder represents a different sample data set.

## Hotels

The Hotels sample data is used in quickstarts, tutorials, and examples. It consists of 50 hotels located in cities across the United States. The data includes images, hotel information, and room information. Data files are in JSON, but there are several versions depending on whether you are uploading it Azure Cosmos DB or pushing it to an index in Azure Search. 

Alternatively, you can access this data from a read-only sandbox in the following ways. 

### Hosted read-only index

There is a staged index populated with the hotels demo data, hosted on a search service, accessed with a query api-key for read-only access to hotel documents.

Endpoint to the index: `https://azs-playground.search.windows.net/indexes/hotels/docs?api-version=2017-11-11&search=*`

query api-key: `EA4510A6219E14888741FCFC19BFBB82`

### Hosted read-only version database

The hotels demo data is also in Azure Cosmos DB. Using the **Import data** wizard, you can create a new Cosmos DB data source based on this connection information. The wizard will ask you for the following three inputs.

Cosmos DB connection string: `AccountEndpoint=https://hotels-docbb.documents.azure.com:443/;AccountKey=4UPsNZyFAjgZ1tzHPGZaxS09XcwLrIawbXBWk6IixcxJoSePTcjBn0mi53XiKWu8MaUgowUhIovOv7kjksqAug==;Database=SampleData`

Database Name: `SampleData`

Collection: `hotels`

## mixedContent 

This sample data is intended for upload to an Azure Blob storage container for AI enrichment examples. The data is a collection of mixed content types including images, Office documents, and text documents in common file formats.

## Caselaw 

The [Caselaw Access Project](https://case.law/bulk/download/) provides public bulk downloads of case data by jurisdiction. Several jurisdictions are freely available without having to request access first. We chose the first one (Arkansas jurisdiction), and then took the first 10 cases.

The file name for this data set is `caselaw-sample.json`.

You can upload this file to Azure Blob storage and use the **Import data** wizard to index the documents. Choose the **JSON Lines** parsing mode.
