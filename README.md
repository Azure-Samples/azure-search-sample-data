---
topic: sample
services: azure-search
name: Azure Search Sample Data
description: |
  Data and index definition metadata for use in the Azure Search samples.
products:
  - azure-search
---

# Azure Search Sample Data

Data and index definition metadata for use in the Azure Search samples.  Use this as a starting point for exploring Azure Search functionality.

Each folder represents a different sample data set.

## Hotels

The Hotels sample data is used in quickstarts, tutorials, and examples. The data is available as JSON files, but there are several versions depending on whether the resides in Azure Cosmost DB or is pushed to an index in Azure Search. 

The files in this repo are available so that you can upload data the data to your own Azure services. But you can also access this data from a read-only public sandbox. The sandbox data is hosted in Azure Cosmos DB. 

### Hosted read-only index

There is a staged index populated with the hotels demo data, hosted on an Azure Search service, accessed with a query api-key for read-only access to hotel documents.

Endpoint to the index: `https://azs-playground.search.windows.net/indexes/hotels/docs?api-version=2017-11-11&search=*`

query api-key: `EA4510A6219E14888741FCFC19BFBB82`

### Hosted read-only version database

Using the **Import data** wizard, you can create a new Cosmos DB data source based on this connection information.

Cosmos DB connection string: `AccountEndpoint=https://hotels-docbb.documents.azure.com:443/;AccountKey=4UPsNZyFAjgZ1tzHPGZaxS09XcwLrIawbXBWk6IixcxJoSePTcjBn0mi53XiKWu8MaUgowUhIovOv7kjksqAug==;`

Database Name: `SampleData`

Collection: `hotels`

## mixedContent 

This sample data is intended for upload to an Azure Blob storage container for AI-indexing (cognitive search) examples. The data is a collection of mixed content types including images, Office documents, and text documents in common file formats.

## Caselaw 

The [Caselaw Access Project](https://case.law/bulk/download/) provides public bulk downloads of case data by jurisdiction. Two jurisdictions are freely available without having to request access first. We chose the first one (Arkansas jurisdiction) to use in several examples, and then grabbed the first 10 cases.

The file name for this data set is `caselaw-small.json`.

You can upload this file to Azure Blob storage and use the **Import data** wizard to index them. Choose the **JSON Lines** parsing mode.