import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types
#https://mxxxn.tistory.com/9

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\RACS\pythonProject\test1-428102-b4723d05eff5.json'

client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('a.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)