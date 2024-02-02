import os
import boto3
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
S3_BUCKET = os.environ['S3_BUCKET']
BASE_URL = f'https://{S3_BUCKET}.s3.us-west-1.amazonaws.com'

s3 = boto3.client(
    "s3",
    "us-west-1",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def s3_upload(file_path, file_name):
    """s3_upload takes two strings, 'file_path' and 'file_name'. Uploads this
    file to S3 with the given name as the key. Returns error if unsuccessful.
    """

    s3.upload_file(file_path, S3_BUCKET, file_name)
