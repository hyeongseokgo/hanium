import os
import io
import cv2
from google.cloud import vision

# 환경 변수 설정
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\kkhs4\Desktop\졸작\mykey.json'

def detect_labels(image_path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()
    img = cv2.imread(image_path)

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(f"{label.description}, Confidence: {label.score*100:.2f}%")

    cv2.imshow("image", img)
    cv2.waitKey(0)

# 객체 인식을 수행할 이미지 경로
image_path = 'face_test.png'
image_path = 'gaffney-group.jpg'
image_path = 'cats_around.jpg'
image_path = 'cat2.jpg'


detect_labels(image_path)
