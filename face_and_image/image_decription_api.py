#라이브러리 설치
#pip uninstall googletrans
#pip install googletrans==3.1.0a0 


import requests
from googletrans import Translator
translator = Translator()

# Hugging Face API URL과 헤더에 API 키를 포함
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
#headers = {"Authorization": f"Bearer mykey"}
headers = {"Authorization": f"Bearer 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"}

# 이미지 파일을 바이너리 형식으로 읽어오는 함수
def open_image(image_path):
    with open(image_path, "rb") as f:
        return f.read()

# API 호출을 통해 모델에 이미지를 전달하고 캡션을 생성
def query(image_path):
    image_data = open_image(image_path)
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()

# 이미지 경로 설정
image_path = './test_img/13.png'

# API 호출 및 결과 출력
output = query(image_path)

#번역 결과 출력
result = output[0]['generated_text']
translated_result = translator.translate(result, dest='ko')

#이미지 설명
print(f"{translated_result.text}(가/이) 있습니다.")

