# PySpark ETL Project

This project is designed as a template for building scalable ETL jobs using PySpark. The project will handle ingestion, transformation, and export of JSON and Parquet files, with future AWS integration.

## Current Stage: Level 0 - Initial Setup
The project structure has been created and the basic components (directories and files) are now in place.

## Directory Structure:
```
pyspark-etl-project/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── etl_job.py
│   ├── transformations.py
│   ├── io_operations.py
│   └── aws_integration.py
│
├── data/
│   ├── raw/
│   │   ├── sample.json
│   │   └── sample.parquet
│   └── processed/
│
├── tests/
│   ├── test_etl_job.py
│   └── test_transformations.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

Future phases will include implementing the ETL logic, adding unit tests, and integrating with AWS services.
