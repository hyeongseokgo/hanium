import json
import boto3
import base64

ACCESS_KEY = "APIKEY"
SECRET_KEY = "APIKEY"
REGION = "ap-northeast-2"
client = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def lambda_handler(event, context):
    
    data = base64.b64decode(event['body']).decode('utf-8')
    #data = event['body']
    
    decoded_data = base64.b64decode(data)
    
    
    response = client.detect_labels(
            Image={'Bytes' : decoded_data},
            MaxLabels=10,
            MinConfidence=50
    )
    
    labels = response['Labels']
    
    if len(labels) != 0:
        return {
            'statusCode': 200,
            'body': json.dumps(labels)
        }
    else:
        return {
            'statusCode': 400,
            'body' : json.dumps("사물이 감지되지 않았어요")
        }