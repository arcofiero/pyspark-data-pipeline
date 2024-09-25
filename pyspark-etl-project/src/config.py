import os

# Toggle between Local and AWS environments
USE_AWS = False  # Change to True if using AWS services

# Local paths
RAW_DATA_PATH_LOCAL = "../data/raw/"
PROCESSED_DATA_PATH_LOCAL = "../data/processed/"

# AWS Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = "us-west-2"
S3_BUCKET = "your-bucket-name"
RAW_DATA_PATH_S3 = f"s3://{S3_BUCKET}/raw/"
PROCESSED_DATA_PATH_S3 = f"s3://{S3_BUCKET}/processed/"

# Select the appropriate paths based on environment
RAW_DATA_PATH = RAW_DATA_PATH_S3 if USE_AWS else RAW_DATA_PATH_LOCAL
PROCESSED_DATA_PATH = PROCESSED_DATA_PATH_S3 if USE_AWS else PROCESSED_DATA_PATH_LOCAL