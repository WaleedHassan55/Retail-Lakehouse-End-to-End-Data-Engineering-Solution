# Retail-Lakehouse-End-to-End Data Engineering

An end-to-end data engineering project built using **Azure Databricks, PySpark and Delta Lake**, following the Medallion Architecture to ingest, transform, validate and organise operational retail data into structured datasets ready for analytics.

The platform demonstrates practical data engineering concepts, including ETL pipelines, data quality validation, incremental data processing and Slowly Changing Dimensions (SCD Type 2).

## Project Overview

The objective of this project is to build a scalable data platform that processes retail operational data and transforms raw datasets into reliable, analytics-ready data.

The platform works with operational datasets covering:

- **People:** Employee and workforce information.
- **Shifts:** Employee shift and scheduling information.
- **Work:** Operational workforce activities.
- **Shrinkage:** Retail shrinkage and loss-related information.

The data is processed through different layers using the Medallion Architecture, ensuring that raw data is progressively cleaned, transformed and structured.

## Architecture

The project follows the Databricks Medallion Architecture:

```text
             Source Data
                  |
                  v
          Data Ingestion
                  |
                  v
          +---------------+
          | Bronze Layer  |
          | Raw Data      |
          +---------------+
                  |
                  v
          +---------------+
          | Silver Layer  |
          | Cleaned Data  |
          | Validations    |
          +---------------+
                  |
                  v
          +---------------+
          | Gold Layer    |
          | Business-Ready|
          | Data          |
          +---------------+
                  |
                  v
          Analytics & Reporting
```

### 1. Bronze Layer – Raw Data

The Bronze layer stores ingested source data in its original structure.

Key responsibilities:
- Ingest data from source files.
- Preserve raw records.
- Maintain a foundation for downstream processing.
- Support traceability and reprocessing.

### 2. Silver Layer – Data Transformation

The Silver layer focuses on cleaning, validating and transforming raw data.

Key responsibilities:
- Data cleansing and standardisation.
- Handling missing and invalid values.
- Removing duplicate records.
- Applying data quality checks.
- Preparing structured datasets for further processing.

### 3. Gold Layer – Business-Ready Data

The Gold layer contains transformed datasets designed for downstream analytics and reporting.

Key responsibilities:
- Organising data for analytical use.
- Applying business transformation logic.
- Maintaining historical changes using SCD Type 2.
- Producing structured datasets for reporting and analysis.

## Key Features

- **Medallion Architecture:** Implements Bronze, Silver and Gold data processing layers.
- **ETL Pipelines:** Ingests, transforms and processes operational datasets.
- **PySpark Transformations:** Uses distributed data processing capabilities.
- **Delta Lake:** Uses Delta tables for structured data storage.
- **Data Quality Checks:** Validates data and helps maintain consistency.
- **SCD Type 2:** Maintains historical records when tracked attributes change.
- **Modular Code Structure:** Separates ingestion, transformation and reusable utility logic.
- **Databricks Asset Bundles:** Includes project configuration through `databricks.yml`.

## Technology Stack

| Technology | Purpose |
|---|---|
| Azure Databricks | Data engineering environment |
| PySpark | Distributed data processing |
| Python | Pipeline development |
| Delta Lake | Reliable data storage |
| SQL | Data querying and transformation |
| Databricks Asset Bundles | Project deployment configuration |
| Git & GitHub | Version control |

## Project Structure

```text
retail_data_platform/
│
├── common_utils/
│   └── Reusable utility functions
│
├── docs/
│   └── Project documentation
│
├── resources/
│   └── Pipeline resources and configurations
│
├── src/
│   └── Source code for data pipelines
│
├── databricks.yml
│
└── README.md
```

## Getting Started

### Prerequisites

Before running the project, ensure you have:

- An Azure Databricks workspace.
- Python installed.
- Access to Databricks.
- Databricks CLI installed.
- Git installed.

### 1. Clone the Repository

```bash
git clone https://github.com/WaleedHassan55/retail_data_platform.git
```

### 2. Navigate to the Project

```bash
cd retail_data_platform
```

### 3. Configure Databricks

Authenticate your Databricks CLI using your workspace credentials and configure the appropriate deployment target in `databricks.yml`.

### 4. Validate the Project Configuration

```bash
databricks bundle validate
```

### 5. Deploy the Project

```bash
databricks bundle deploy
```

After deployment, execute the configured pipeline resources according to the project configuration.

## What I Learned

Through this project, I gained practical experience in:

- Designing an end-to-end data engineering solution.
- Implementing Medallion Architecture in Databricks.
- Building modular ETL pipelines using PySpark.
- Working with Delta Lake tables.
- Implementing data quality validation.
- Understanding historical data management through SCD Type 2.
- Organising data engineering projects using reusable components.
- Managing Databricks project configurations and deployments.

## Future Improvements

Potential areas for further development include:

- Implementing automated pipeline scheduling using Databricks Workflows.
- Adding pipeline monitoring and logging.
- Introducing automated testing and data quality reporting.
- Integrating additional cloud data sources.
- Optimising Delta tables and improving processing performance.
- Developing dashboards using Power BI.

## Author

Waleed Hassan

BSc (Hons) Computer Science with Artificial Intelligence | First Class Honours

Interested in Data Engineering, Cloud Technologies, Machine Learning and AI.


---

*This project demonstrates practical implementation of modern data engineering concepts using the Databricks Lakehouse platform.*
