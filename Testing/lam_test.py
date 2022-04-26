# CODE BELOW DOES NOT WORK BUT JUST EXAMPLE OF WHAT TESTING LOOKS LIKE WITH AWS AND MOTO
import boto3
import pytest
import init_data_crawler as idc


test_s3_event = {
    "Records": [{
        "s3": {
            'bucket': {'name': 'test_bucket'},
            'object': {
                'key': 'example/s3/path/key'
            }
        }
    }]}

@mock_s3
def test_lambda_handler():

    # set up test bucket
    s3_client = boto3.client('s3')
    test_bucket_name = 'test_bucket'
    test_data = b'col_1,col_2\n1,2\n3,4\n'

    s3_client.create_bucket(Bucket=test_bucket_name)    
    s3_client.put_object(Body=test_data, Bucket=test_bucket_name, Key=f'example/s3/path/key/test_data.csv')
    
    response = lambda_handler(event=test_event, context={})

    assert response['status'] == 'success'