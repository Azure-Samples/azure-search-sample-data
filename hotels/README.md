# Hotels Sample Data

Data for samples that reference the Hotels schema and data set.  This is the default set for most Azure Search samples. 

Overview of the files contained in this folder:

##Hotels.postman_collection.json

Import this collection into Postman to execute request to create the Hotels index and populate data.

##Hotels_IndexDefinition.JSON

JSON in the body of the Post request to create the Hotels index.

##HotelsData_toAzureSearch.JSON

JSON in the body of the Post request to populate the Hotels index.

##HotelsData_toCosmosDB.JSON

JSON to populate a CosmosDB with the Hotels sample data.  This can be used as a data source for an indexer to pull data into the Hotels index.