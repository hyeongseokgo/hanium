import json
from googletrans import Translator
import requests
import base64

API_URL = ""
headers = ""
translator = Translator()
def lambda_handler(event, context):
    try: 
        data = base64.b64decode(event['body'])
        data = base64.b64decode(data)
        response = requests.post(API_URL, headers=headers, data=data)
        output = response.json()
        result = output[0]['generated_text']
        translated_result = translator.translate(result, dest='ko')
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps(translated_result.text, ensure_ascii=False)
        }
    except:
        return {
            'statusCode' : 200,
            'body' : json.dumps("사물이 제대로 감지되지 않았어요 다시한번 촬영해주세요.")
        }