import json
import boto3
import base64

ACCESS_KEY = ""
SECRET_KEY = ""
REGION = ""
rekognition = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
collection_id = ''
def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        data = base64.b64decode(body['image'])
        #data = base64.b64decode(data)
        name = body['name']
        name = base64.b64decode(name).decode("utf-8")
    except Exception as e:
        return {
            'statusCode' : 400,
            'body' : json.dumps(f"데이터 처리 오류{e}", ensure_ascii=False)
        }
    
    try:
        encoded_name = base64.urlsafe_b64encode(name.encode('utf-8')).decode('utf-8')
        response = rekognition.index_faces(
            CollectionId=collection_id,
            Image={
                'Bytes' : data
            },
            ExternalImageId=encoded_name,
            DetectionAttributes=['ALL']
        )
        
        return {
            'statusCode' : 200,
            'body' : json.dumps(f"{name}의 얼굴이 등록되었습니다.", ensure_ascii=False)
        }
    except Exception as e:
        return {
            'statusCode' : 400,
            'body' : json.dumps(f"얼굴 저장 오류{e}", ensure_ascii=False)
        }
