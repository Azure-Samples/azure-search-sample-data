# Hotels Sample Data

Fictitious demo data for quickstarts, tutorials, and code examples. This is the default data set for most Azure Cognitive Search samples. It consists of 50 hotels across the US and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier.

Hotels demo data is provided in multiple formats to support different consumption models. The data is identical regardless of how you load it.

## Hotels.postman_collection.json

Import this collection into Postman to execute requests to create the Hotels index and populate data. The hotels index and documents are in JSON in the request body for each request.

## Hotels_IndexDefinition.JSON

JSON in the body of the POST request to create the Hotels index. This is just the schema.

## HotelsData_toAzureSearch.JSON

JSON in the body of the POST request to populate the Hotels index with data for 50 hotels.

## HotelsData_toCosmosDB.JSON

JSON to populate an Azure Cosmos DB with the Hotels sample data.  This can be used as a data source for an indexer to pull data into the Hotels index.
