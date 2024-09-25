import boto3
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

def upload_to_s3(local_file, bucket, s3_file):
    s3 = get_s3_client()
    s3.upload_file(local_file, bucket, s3_file)