import json
import boto3
import base64
from datetime import datetime
from contextlib import closing
ACCESS_KEY = ""
SECRET_KEY = ""
REGION = ""
client = boto3.client("polly", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
s3 = boto3.client("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
BUCKET_NAME = ''
def lambda_handler(event, context):
    try:
        S3_KEY = str(int((datetime.timestamp(datetime.now())) * 1000000)) + ".mp3"
        
        
        text = base64.b64decode(event['body']).decode("utf-8")
        #text = event['body']
        #text = base64.b64decode(text).decode("utf-8")
        response = client.synthesize_speech(
        Engine='standard', LanguageCode='ko-KR',
        OutputFormat='mp3',
        SampleRate='8000',
        Text=text,
        VoiceId='Seoyeon'
        )
        # TODO implement
        
        
        audio_stream = response['AudioStream'].read()
        s3.put_object(Bucket=BUCKET_NAME, Key=S3_KEY, Body=audio_stream)
        
        s3_url = s3.generate_presigned_url('get_object', Params={'Bucket': BUCKET_NAME, 'Key': S3_KEY}, ExpiresIn=3600)
        
        return {
            'statusCode': 200,
            'body': json.dumps(s3_url)
        }
    except:
        return {
            'statusCode' : 400,
            'body' : json.dumps("Error")
        }