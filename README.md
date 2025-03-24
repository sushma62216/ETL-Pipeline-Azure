# ETL Pipeline using Azure Data Factory, Azure SQL Database, Azure Blob Storage, Python, and GitHub Codespaces

# Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Microsoft Azure services. The pipeline extracts data from an API, processes it using Python, stores the raw data in Azure Blob Storage, and then loads the transformed data into an Azure SQL Database using Azure Data Factory.

# Tech Stack

**Azure Data Factory**: Orchestrates the ETL pipeline.

**Azure Blob Storage**: Stores raw and processed data.

**Azure SQL Database**: Stores the final transformed data.

**Python**: Handles data extraction and transformation.

**GitHub Codespaces**: Provides a cloud-based development environment.

# Workflow

**Extract**: Fetch data from an external API using Python.

**Transform**: Clean and process the extracted data.

**Load**: Store raw data in Azure Blob Storage and transformed data into Azure SQL Database via Azure Data Factory.

**Orchestration**: Use Azure Data Factory to schedule and automate the workflow.

# Installation and Setup

## Prerequisites

* Azure subscription
* GitHub repository with Codespaces enabled
* Python environment with required dependencies
* Azure Storage Account and SQL Database setup

## Steps

## Step 1: Clone the repository and open it in GitHub Codespaces:
```
git clone <repo_url>
cd <repo_name>
```
## Step 2: Set up a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
## Step 3: Run the extraction script to pull data from the API:
```
python extract.py
```
