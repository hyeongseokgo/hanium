import json
import os
import io
import base64
import boto3
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'path'
client_google = vision.ImageAnnotatorClient()

ACCESS_KEY = "APIKEY"
SECRET_KEY = "APIKEY"
REGION = "ap-northeast-2"
client_aws = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

def lambda_handler(event, context):
    
    # 텍스트 감지부
    #data = base64.b64decode(event['body']).decode('utf-8')
    #decoded_data = base64.b64decode(data)
    decoded_data = base64.b64decode(event['body'])
    content = decoded_data
    image = vision.Image(content=content)
    response = client_google.document_text_detection(image=image)
    document = response.full_text_annotation
    
    ret = "텍스트 감지 결과 \n"
    
    if document.text:
        document_text = document.text
        ret += document_text + "\n\n"
    else:
        ret += "텍스트 감지 없음\n\n"
        
    
    # 얼굴 감지부
    eng_to_kor = {"Male" : "남성", "Female" : "여성", 
        "HAPPY" : "행복한", "CALM" : "침착한", "SURPRISED" : "놀란",
        "CONFUSED" : "당황한", "ANGRY" : "화난", "DISGUSTED" : "화난",
        "SAD" : "슬픈", "FEAR" : "겁에 질린"
    }
    
    response = client_aws.detect_faces(
            Image={'Bytes' : decoded_data},
            Attributes=['ALL']
    )
    faceDetails = response['FaceDetails']
    ret += "얼굴 감지 결과\n"
    if len(faceDetails) == 0:
        ret += "얼굴이 감지되지 않았어요.\n\n"
    else:
        if len(faceDetails) > 1:
            ret += f'총 {len(faceDetails)}명의 얼굴이 감지되었어요\n'
        for detail in faceDetails:
            gender = eng_to_kor[detail['Gender']['Value']]
            ageRangeLow = detail['AgeRange']['Low']
            ageRangeHigh = detail['AgeRange']['High']
            emotions = eng_to_kor[detail['Emotions'][0]['Type']]
            ret += f"{ageRangeLow}~{ageRangeHigh}세 정도의 {gender}이 {emotions} 표정을 하고있어요\n"
        
        ret += "\n"
    
    # 사물 감지부 (미구현)
    
    return {'statusCode' : 200,
            'body' : json.dumps(ret, ensure_ascii=False)}