import os
# from flask import Flask
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
path = os.environ['PATH']

print(AWS_ACCESS_KEY_ID)
print(path)

# trying to test boto3. ... fn to get object here.