import json
import boto3
import base64
ACCESS_KEY = ""
SECRET_KEY = ""
REGION = ""
client = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def lambda_handler(event, context):
    data = base64.b64decode(event['body'])
    data = base64.b64decode(data)
    
    
    response = client.detect_faces(
        Image={'Bytes' : data}
        )
    
    n = len(response['FaceDetails'])
    
    return {
        'statusCode' : 200,
        'body' : json.dumps(str(n))
    }
