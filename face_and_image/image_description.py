from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 사전 학습된 모델과 프로세서를 불러오기.
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 이미지를 불러오기.
image_path = '이미지 주소'
raw_image = Image.open(image_path)

# 이미지를 모델에 입력할 수 있는 형식으로 변환.
inputs = processor(raw_image, return_tensors="pt")

# 모델을 통해 설명 텍스트를 생성. max_new_tokens를 통해 최대를 정할 수 있음.
output = model.generate(**inputs, max_new_tokens=30)

# 생성된 텍스트 출력
caption = processor.decode(output[0], skip_special_tokens=True)
print("이미지 설명:", caption)