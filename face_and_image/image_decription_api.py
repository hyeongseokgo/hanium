import requests


# Hugging Face API URL과 헤더에 API 키를 포함
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer mykey"}

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
image_path = '이미지 주소'

# API 호출 및 결과 출력
output = query(image_path)
print("이미지 설명:", output)
