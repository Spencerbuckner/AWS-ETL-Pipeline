import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Starting crawler: transformed-data-crawler')

glue = boto3.client(service_name='glue', region_name='us-east-1',endpoint_url='https://glue.us-east-1.amazonaws.com')

def lambda_handler(event, context):
    try:
        glue.start_crawler(Name='transformed-data-crawler')
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e