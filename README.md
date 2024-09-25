# PySpark ETL Project

This project serves as a template for building scalable ETL jobs using PySpark. It handles the ingestion, transformation, and export of JSON files, with potential AWS integration in future levels.

## Current Stage: Level 1 - ETL Pipeline Implementation

The project has completed the first phase, where JSON files are ingested, transformations are applied, and data is joined across multiple datasets (employees and department budgets). The pipeline reads employee and department data, applies filtering and transformations, and joins the two datasets on `dept_id`. The resulting dataset is ready for export or further processing.

### Key Features:

- **Ingestion**: The pipeline reads JSON files from the `data/raw/` directory.
- **Transformations**: Employee data is filtered based on age, and department information is joined for each employee.
- **Join**: Employee data is joined with the department budget data using the `dept_id` key.
- **Validation**: The output includes the joined results, validating the correctness of the pipeline.

## Previous Stage: Level 0 - Initial Setup

In Level 0, the project structure was set up, and the basic components like directories and files were created. The structure laid the foundation for subsequent levels by organizing code for ingestion, transformations, and future AWS integration.

### Directory Structure:

```bash
pyspark-etl-project/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── etl_job.py          # Main ETL job script
│   ├── transformations.py  # Transformation logic
│   ├── io_operations.py    # Input/output logic
│   └── aws_integration.py  # Future AWS integration
│
├── data/
│   ├── raw/                # Input JSON files
│   └── processed/          # Processed files (export directory)
│
├── tests/
│   ├── test_etl_job.py
│   └── test_transformations.py
│
├── .gitignore
├── README.md               # Project overview
└── requirements.txt        # Python dependencies

```

### Future Phases:

	•	Level 2: Add unit tests and enhance test coverage.
	•	Level 3: Integrate with AWS services for reading from and writing to S3, Glue jobs, and more.
	•	Level 4: Add support for Parquet and other file formats.