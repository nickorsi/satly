import os
# from flask import Flask
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# trying to test boto3. ... fn to get object here.

s3 = boto3.client(
    "s3",
    "us-west-1",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
# Uploading a file
s3.upload_file(
    './static/Konica_Minolta_DiMAGE_Z3.jpg',
    'saltly-bucket',
    'Konica_Minolta_DiMAGE_Z3.jpg'
)

# Get URL in S3, which will be BASE_URL + the object key (filename)