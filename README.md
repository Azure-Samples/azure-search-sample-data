# Azure AI Search Sample Data

This repository contains data files used in Azure AI Search quickstarts, tutorials, and examples. Each folder represents a different sample data set. Most sample data is used for [indexer](https://docs.microsoft.com/azure/search/search-indexer-overview) and [AI enrichment](https://docs.microsoft.com/azure/search/cognitive-search-concept-intro) scenarios and is typically uploaded to Azure Storage so that it can be accessed by an indexer.

+ [ai-enrichment-mixed-media folder](#ai-enrichment-mixed-media)
+ [good-books folder](#good-books)
+ [health-plan folder](#health-plan)
+ [hotelreviews folder](#hotelreviews)
+ [hotels folder](#hotels-data)
+ [microsoft-earnings-calls folder](#microsoft-earnings-calls)
+ [nasa-e-book folder](#nasa-e-books)
+ [ny-philharmonic folder](#ny-philharmonic)
+ [unsplash-images folder](#unsplash-images)

This repository also contains an [**ARCHIVE** folder](#archive) for previously published data files that are no longer used in samples or docs. 

It previously included a STOPWORDS.MD file. This file is now in the Reference section of the Azure AI Search documentation. [Stopwords reference (Microsoft analyzers)](https://learn.microsoft.com/azure/search/reference-stopwords) is the new location.

## ai-enrichment-mixed-media

Contains 14 files of mixed content types, including HTML, JPG, PDF, PowerPoint, Word, PNG, and TXT files. These files are used to demonstrate the breadth of skillset processing of multiple content types using a combination of built-in skills. This sample data is intended for upload to an Azure Blob storage container, and then referenced from an indexer's data source object.

**Used in:** [Quickstart: Create a skillset](https://learn.microsoft.com/azure/search/cognitive-search-quickstart-blob)

## good-books

Contains a CSV file containing 10,000 book titles.

**Used in:** [Tutorial: Add search to static web apps](https://learn.microsoft.com/azure/search/tutorial-csharp-overview)

## health-plan

PDFs containing fictitious health plan data for Northwind and Contoso.

**Used in:** [Quickstart: Vector search](https://learn.microsoft.com/azure/search/search-get-started-vector), and [Chunk and vectorize by document layout or structure](https://learn.microsoft.com/azure/search/search-how-to-semantic-chunking).

## hotelreviews

Contains two files from an open-source Kaggle dataset:

+ A CSV file provides data consisting of customer reviews of various fictional hotels in Europe. You can use this data in AI enrichment tutorials, applying sentiment analysis, language detection, and text translation. When indexing content from a CSV file, be sure to select a parsing mode so that individual documents can be created for each line in the file.

+ A JSON file provides a skillset definition.

**Used in:** [knowledge store articles](https://learn.microsoft.com/azure/search/knowledge-store-create-rest)

## hotels

Contains fictitious demo data for quickstarts, tutorials, and code examples. We used Azure OpenAI GPT-35-turbo to generate a portion of the data. Any resemblance to actual hotels or related businesses is unintentional. This is the default data set for many Azure AI Search examples and queries. It consists of 50 hotels across the United States and includes data to support all query types, including geospatial filters. It is structured and sized to run on the free tier. 

Hotels demo data is provided in multiple formats to support different consumption models. Some data files contain a small number of hotels.

## microsoft-earnings-calls

Contains [49 Microsoft earnings-call transcripts](microsoft-earnings-calls/README.md), one for each fiscal quarter from FY14 Q4 through FY26 Q4. The folder provides normalized UTF-8 text and links to the source documents. The dataset is licensed under [CDLA-Permissive-2.0](microsoft-earnings-calls/LICENSE).

## nasa-e-book

Content from [NASA's earth book (February 2019)](https://earthobservatory.nasa.gov/features/earth-book-2019) is used in conceptual examples that explain semantic search and answers. This folder contains a collection of PDFs from NASA's downloadable books site. The folder includes intact versions of the entire book as single PDF file. A subfolder contains per-page extractions as separate PDF files for both images and text, as well as text-only pages to facilitate indexing on service tiers that have lower limits.

The first 10 PDFs in \azure-search-sample-data\nasa-e-book\text-only are used in entity recognition and entity linking skills processing demos.

This folder also contains [Earth at Night](https://www.nasa.gov/stem-content/earth-at-night-e-book/) in PDF and JSON formats.

**Used in:** [Tutorial: Build a RAG solution](https://learn.microsoft.com/azure/search/tutorial-rag-build-solution) and multiple [agentic retrieval](https://learn.microsoft.com/azure/search/search-agentic-retrieval-concept) examples.

## ny-philharmonic

Contains JSON files of nested JSON arrays. There is one folder with one JSON file that you can run on the free tier. A second folder provides more files if you want to work with larger data.

**Used in:** [Index Azure JSON blobs tutorial](https://docs.microsoft.com/azure/search/search-semi-structured-data)

## state-parks

Contains CSV files for two state parks.

**Used in:** [Tutorial: Index permission metadata from ADLS Gen2 and query with permission-filtered results](https://learn.microsoft.com/azure/search/tutorial-adls-gen2-indexer-acls)

## sustainable-ai-pdf

Contains PDFs with text and images for multimodal scenarios.

**Used in:** [Quickstart: Search for multimodal content in the Azure portal](https://learn.microsoft.com/azure/search/search-get-started-portal-image-search), [Tutorial: Vectorize images and text](https://learn.microsoft.com/azure/search/tutorial-document-extraction-multimodal-embeddings), [Tutorial: Vectorize from a structured document layout]https://learn.microsoft.com/azure/search/tutorial-document-layout-multimodal-embeddings(), [Tutorial: Verbalize images using generative AI](https://learn.microsoft.com/azure/search/tutorial-document-extraction-image-verbalization), [Tutorial: Verbalize images from a structured document layout](https://learn.microsoft.com/azure/search/tutorial-document-layout-image-verbalization).

## unsplash-images

Contains images from [https://unsplash.com/s/photos/landmark](https://unsplash.com/s/photos/landmark) and [https://unsplash.com/s/photos/](https://unsplash.com/s/photos/) are used in OCR and image analysis skills processing demos. There are ten images in each folder. 

+ The "jpg-landmarks" folder contains photos of well-known buildings and structures. It's used to demonstrate image analysis.

+ The "jpg-signs" folder contains photos that include signs and is used to demonstrate OCR skillset processing.
