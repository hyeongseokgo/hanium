import json
import os
import io
import base64
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ""

client = vision.ImageAnnotatorClient()
def lambda_handler(event, context):
    data = base64.b64decode(event['body']).decode('utf-8')
    
    
    
    decoded_data = base64.b64decode(data)
    content = decoded_data
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    
    if document.text:
        document_text = document.text
        return {
            'statusCode' : 200,
            'body' : json.dumps(document_text, ensure_ascii=False)
        }
    else:
        return {
            'statusCode' : 400,
            'body' : json.dumps("텍스트 감지 없음", ensure_ascii=False)
        }