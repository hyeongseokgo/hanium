import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image

import cv2
import boto3

ACCESS_KEY = "AKIA6GBMCU3ZOHVGSWNF"
SECRET_KEY = "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"
REGION = "ap-northeast-2"

client = boto3.client("rekognition", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)

path = 'face_test.png'
path = 'gaffney-group.jpg'
path = 'cats_around.jpg'
path = 'cat2.jpg'

img = cv2.imread(path)
imageData = open(path, "rb").read()

response = client.detect_labels(
        Image={'Bytes': imageData},
        MaxLabels=10,
        MinConfidence=50
    )

labels = response['Labels']

for label in labels:
    print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}")

cv2.imshow("image", img)
cv2.waitKey(0)