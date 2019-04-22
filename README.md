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

### Hosted read-only version

Using the **Import data** wizard, you can create a new Cosmos DB data source based on this connection information.

Cosmos DB connection string: `AccountEndpoint=https://hotels-docbb.documents.azure.com:443/;AccountKey=4UPsNZyFAjgZ1tzHPGZaxS09XcwLrIawbXBWk6IixcxJoSePTcjBn0mi53XiKWu8MaUgowUhIovOv7kjksqAug==;`

Database Name: `SampleData`

Collection: `hotels`

## Caselaw 

The [Caselaw Access Project](https://case.law/bulk/download/) provides public bulk downloads of case data by jurisdiction. Two jurisdictions are freely available without having to request access first. We chose the first one (Arkansas jurisdiction) to use in several examples. In this repo, you will find the following JSON files:

+ `data-small.json1` - The first 10 cases. Use this data set if you are using a free shared service.

+ `data-full.json1` - The full data set, 858 documents.

