# Azure Cognitive Search Sample Data

This repository contains data files used in Azure Cognitive Search quickstarts, tutorials, and examples. Each folder represents a different sample data set.

+ ai-enrichment-mixed-media folder
+ clinical-trials folder
+ hotelreviews folder
+ hotels folder
+ nasa-e-book folder
+ spanish-museums folder
+ unsplash-images folder

This repository contains an **ARCHIVE** folder for previously published data files that are no longer used in samples or docs. It also includes a **STOPWORDS** file that lists the stopwords for each language analyzer used in text analysis.

## AI-enrichment-mixed-media (files for skillsets and AI enrichment)

This folder contains 14 files of mixed content types, including HTML, JPG, PDF, PowerPoint, Word, PNG, and TXT files. These files are used to demonstrate the breadth of skillset processing of multiple content types using a combination of built-in skills. This sample data is intended for upload to an Azure Blob storage container for AI enrichment examples.

## Clinical trials

This folder contains three subfolders of clinical trials data from [https://clinicaltrials.gov](https://clinicaltrials.gov/ct2/resources/download). Subfolders contain large and small numbers of files, plus a JSON version.

| Folder | Description |
|--------|-------------|
| Clinical trials JSON | Consists of 8 semi-structured JSON files that you can upload to Azure Blob storage, and then import using the Azure Blob indexer. This data is used in the [Index Azure JSON blobs tutorial](https://docs.microsoft.com/azure/search/search-semi-structured-data). |
| Clinical trials PDF 19 | Consists of 19 PDF files used in AI enrichment lessons. This data set can be used in AI enrichment pipelines on the free tier, using the free allocation of daily transactions per indexer. |
| Clinical trials PDF 107 | Consists of 107 PDF files used in knowledge mining labs and tutorials. Processing this quantity of documents requires an attached Cognitive Services all-in-one resource. |

## Hotels data

The Hotels folder contains fictitious demo data for quickstarts, tutorials, and code examples. This is the default data set for many Azure Cognitive Search samples. It consists of 50 hotels across the United States and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier.

Hotels demo data is provided in multiple formats to support different consumption models. The data is identical regardless of how you load it. Data files are in JSON, but there are several versions depending on whether you are uploading it Azure Cosmos DB or pushing it to an index in Azure Cognitive Search. 

Use the following files to create the hotels sample on your search service:

+ **Hotels.postman_collection.json** - Using Postman, import this collection to execute requests that create and populate the Hotels index using JSON documents.

+ **Hotels_IndexDefinition.JSON** - A standalone JSON file containing just the index. This index definition is equivalent to the hosted index on azs-playground search service.

+ **HotelsData_toAzureSearch.JSON** - A standalone JSON file containing documents for 50 hotels and related room information.

+ **HotelsData_toCosmosDB.JSON** - JSON used to populate an Azure Cosmos DB with the Hotels sample data.  This can be used as a data source for an indexer to pull data into the Hotels index.

### Hotels-json-documents

This sample data set consists of 5 JSON documents containing structured JSON, used for evaluating or testing JSON blob indexing. Each file consists of hotel information, an address complex field, and a rooms complex collection. The blob indexer can detect and match this JSON structure through equivalent fields in a search index.

## HotelReviews

This folder contains two files:

+ A CSV file provides data consisting of customer reviews of various fictional hotels in Europe. You can use this data in AI enrichment tutorials, applying sentiment analysis, language detection, and text translation. This data set is used in the [Create a knowledge store quickstart](https://docs.microsoft.com/azure/search/knowledge-store-create-portal). When indexing content from a CSV file, be sure to select a parsing mode so that individual documents can be created for each line in the file.

+ A JSON file provides a skillset definition.

## NASA e-books

Content from [NASA's earth book (February 2019)](https://earthobservatory.nasa.gov/features/earth-book-2019) is used in conceptual examples that explain semantic search and answers. This folder contains a collection of PDFs from NASA's downloadable books site. The folder includes intact versions of the entire book as single PDF file. A subfolder contains per-page extractions as separate PDF files for both images and text, as well as text-only pages.

The first 10 PDFs in \azure-search-sample-data\nasa-e-book\text-only are used in entity recognition and entity linking skills processing demos.

## Unsplash images

Images from [https://unsplash.com/s/photos/landmark](https://unsplash.com/s/photos/landmark) and [https://unsplash.com/s/photos/](https://unsplash.com/s/photos/) are used in OCR and image analysis skills processing demos. There are ten images in each folder. 

+ The "jpg-landmarks" folder contains photos of well-known buildings and structures. It's used to demonstrate image analysis.

+ The "jpg-signs" folder contains photos that include signs and is used to demonstrate OCR skillset processing.

## Spanish museums

This folder includes 10 Word document files in Spanish and French, five in each language. Content consists of museum descriptions from the "Essential Museums" brochure on the [Official tourism portal of Spain](https://www.spain.info/en/brochures/leisure-culture/). These files are used in Language Detection and Text Translation skills processing demos. Content from the brochure was copied into individual Word document files, one for each museum and language combination.

## STOPWORDS.MD

The stopwords.md file is a list of the stopwords used by the Microsoft analyzer for each language.

## ARCHIVE

### hotels-2019

The original version of the built-in sample containing fictitious hotel information.

### Caselaw 

An example that used data from the Caselaw has been updated to use different data and steps. The data file used for that exercise is now archived. The [Caselaw Access Project](https://case.law/bulk/download/) provides public bulk downloads of case data by jurisdiction. Several jurisdictions are freely available without having to request access first. We chose the first one (Arkansas jurisdiction) and took the first 10 cases. The file name for this data set is `caselaw-sample.json`. If you upload this file to Azure Blob storage and use the **Import data** wizard to index the documents, choose the **JSON Lines** parsing mode.