# Azure AI Search Sample Data

สวัสดีครับ

This repository contains data files used in Azure AI Search quickstarts, tutorials, and examples. Each folder represents a different sample data set. Most sample data is used for [indexer](https://docs.microsoft.com/azure/search/search-indexer-overview) and [AI enrichment](https://docs.microsoft.com/azure/search/cognitive-search-concept-intro) scenarios and is typically uploaded to Azure Storage so that it can be accessed by an indexer.

+ [ai-enrichment-mixed-media folder](#ai-enrichment-mixed-media)
+ [desert-pdfs](#desert-pdfs)
+ [good-books folder](#good-books)
+ [health-plan folder](#health-plan)
+ [hotelreviews folder](#hotelreviews)
+ [hotels folder](#hotels-data)
+ [nasa-e-book folder](#nasa-e-books)
+ [ny-philharmonic folder](#ny-philharmonic)
+ [spanish-museums folder](#spanish-museums)
+ [unsplash-images folder](#unsplash-images)

This repository also contains an [**ARCHIVE** folder](#archive) for previously published data files that are no longer used in samples or docs. 

It previously included a STOPWORDS.MD file. This file is now in the Reference section of the Azure AI Search documentation. [Stopwords reference (Microsoft analyzers)](https://docs.microsoft.comazure/search/reference-stopwords) is the new location.

## AI-enrichment-mixed-media

This folder contains 14 files of mixed content types, including HTML, JPG, PDF, PowerPoint, Word, PNG, and TXT files. These files are used to demonstrate the breadth of skillset processing of multiple content types using a combination of built-in skills. This sample data is intended for upload to an Azure Blob storage container, and then referenced from an indexer's data source object.

**Used in:** [Quickstart: Create a skillset](https://docs.microsoft.com/azure/search/cognitive-search-quickstart-blob)

## NY Philharmonic

This folder contains JSON files of nested JSON arrays. There is one folder with one JSON file that you can run on the free tier. A second folder provides more files if you want to work with larger data.

**Used in:** [Index Azure JSON blobs tutorial](https://docs.microsoft.com/azure/search/search-semi-structured-data)

## Desert PDFs

This folder includes PDF downloads of Wikipedia pages about well-known deserts across the world. These PDFs have text, images, tables, and other graphical elements.

## Good-books

This folder includes a CSV file containing 10,000 book titles.

## Health-plan

PDFs containing fictitious health plan data for Northwind and Contoso.

## Hotels data

The Hotels folder contains fictitious demo data for quickstarts, tutorials, and code examples. We used Azure OpenAI GPT-35-turbo to generate a portion of the data. Any resemblence to actual hotels or related businesses is unintentional. This is the default data set for many Azure AI Search samples. It consists of 50 hotels across the United States and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier. 

Hotels demo data is provided in multiple formats to support different consumption models. The data is identical regardless of how you load it. Data files are in JSON, but there are several versions depending on whether you are uploading it Azure Cosmos DB or pushing it to an index in Azure AI Search. 

### Hotels-json-documents

This sample data set consists of 5 JSON documents containing structured JSON, used for evaluating or testing JSON blob indexing. Each file consists of hotel information, an address complex field, and a rooms complex collection. The blob indexer can detect and match this JSON structure through equivalent fields in a search index.

### Hotels-sql

This is a SQL script that creates a database, a table, and inserts 12 rows of partial hotel information. 

## HotelReviews

This folder contains two files:

+ A CSV file provides data consisting of customer reviews of various fictional hotels in Europe. You can use this data in AI enrichment tutorials, applying sentiment analysis, language detection, and text translation. When indexing content from a CSV file, be sure to select a parsing mode so that individual documents can be created for each line in the file.

+ A JSON file provides a skillset definition.

**Used in:** [Create a knowledge store](https://docs.microsoft.com/azure/search/knowledge-store-create-portal)

## NASA e-books

Content from [NASA's earth book (February 2019)](https://earthobservatory.nasa.gov/features/earth-book-2019) is used in conceptual examples that explain semantic search and answers. This folder contains a collection of PDFs from NASA's downloadable books site. The folder includes intact versions of the entire book as single PDF file. A subfolder contains per-page extractions as separate PDF files for both images and text, as well as text-only pages.

The first 10 PDFs in \azure-search-sample-data\nasa-e-book\text-only are used in entity recognition and entity linking skills processing demos.

## Unsplash images

Images from [https://unsplash.com/s/photos/landmark](https://unsplash.com/s/photos/landmark) and [https://unsplash.com/s/photos/](https://unsplash.com/s/photos/) are used in OCR and image analysis skills processing demos. There are ten images in each folder. 

+ The "jpg-landmarks" folder contains photos of well-known buildings and structures. It's used to demonstrate image analysis.

+ The "jpg-signs" folder contains photos that include signs and is used to demonstrate OCR skillset processing.

## Spanish museums

This folder includes 10 Word document files in Spanish and French, five in each language. Content consists of museum descriptions from the "Essential Museums" brochure on the [Official tourism portal of Spain](https://www.spain.info/en/brochures/leisure-culture/). These files are used in Language Detection and Text Translation skills processing demos. Content from the brochure was copied into individual Word document files, one for each museum and language combination.
