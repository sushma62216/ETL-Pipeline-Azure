#!/bin/bash

echo "Setting up project structure..."

# Create directories
mkdir -p data/raw data/processed
mkdir -p config etl notebooks logs .devcontainer

# Create files
touch config/db_config.py
touch etl/extract.py etl/transform.py etl/load.py etl/etl_pipeline.py

echo "Project structure created successfully!"
