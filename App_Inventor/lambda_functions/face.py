import json
import boto3
import base64

ACCESS_KEY = ""
SECRET_KEY = ""
REGION = ""
client = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
collection_id = ''
def lambda_handler(event, context):
    try:
        data = base64.b64decode(event['body']).decode('utf-8')
        #data = event['body']
        decoded_data = base64.b64decode(data)
        
        eng_to_kor = {"Male" : "남성", "Female" : "여성", 
            "HAPPY" : "행복한", "CALM" : "침착한", "SURPRISED" : "놀란",
            "CONFUSED" : "당황한", "ANGRY" : "화난", "DISGUSTED" : "화난",
            "SAD" : "슬픈", "FEAR" : "겁에 질린"
        }
    except:
        return {
            'statusCode' : 500,
            'body' : json.dumps("데이터 처리중에 문제가 발생했어요", ensure_ascii)
        }
    response1 = client.detect_faces(
            Image={'Bytes' : decoded_data},
            Attributes=['ALL']
    )
    faceDetails = response1['FaceDetails']
    if len(faceDetails) == 0:
        return {
            'statusCode' : 400,
            'body' : json.dumps("얼굴이 감지되지 않았어요", ensure_ascii=False)
        }
    else:
        ans = ""
        if len(faceDetails) > 1:
            ans = f'총 {len(faceDetails)}명의 얼굴이 감지되었어요\n'
        else:
            try:
                response2 = client.search_faces_by_image(
                    CollectionId=collection_id,
                    Image={'Bytes' : decoded_data},
                    FaceMatchThreshold=80,
                    MaxFaces=1)
                if response2['FaceMatches']:
                    match_face = response2['FaceMatches'][0]
                    name = match_face['Face']['ExternalImageId']
                    name = bytes.fromhex(name).decode('utf-8')
                    ans = f"{name}님의 얼굴이 감지되었어요\n"
            except Exception as e:
                ans = f"{e}"
        for detail in faceDetails:
            gender = eng_to_kor[detail['Gender']['Value']]
            ageRangeLow = detail['AgeRange']['Low']
            ageRangeHigh = detail['AgeRange']['High']
            emotions = eng_to_kor[detail['Emotions'][0]['Type']]
            ans += f"{ageRangeLow}~{ageRangeHigh}세 정도의 {gender}이 {emotions} 표정을 하고있어요\n"
        return {'statusCode' : 200,
                'body' : json.dumps(ans, ensure_ascii=False)
        }
