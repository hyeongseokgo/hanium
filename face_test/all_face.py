import cv2
import dlib
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam
import os
import io
from google.cloud import vision

# 얼굴 인식기 로드 (dlib)
detector = dlib.get_frontal_face_detector()

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# 언령 예측 모델 불러오기
age_net = cv2.dnn.readNetFromCaffe(
	'models/deploy_age.prototxt',
	'models/age_net.caffemodel')
age_list = ['0 ~ 2', '4 ~ 6', '8 ~ 12', '15 ~ 20',
            '25 ~ 32', '38 ~ 43', '48 ~ 53', '60 ~ 100']

# 성별 예측 모델 불러오기
gender_net = cv2.dnn.readNetFromCaffe(
	'models/deploy_gender.prototxt',
	'models/gender_net.caffemodel')
gender_list = ['남자', '여자']

# 표정 인식을 위한 눈, 코, 입등의 위치 반환
predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
expression_labels = ['화난', '싫어하는', '두려운', '행복한', '슬픈', '놀란', '무']
model_emotion = load_model('models/emotion_model.hdf5', compile=False)
model_emotion.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# 환경 변수 설정
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\kkhs4\Desktop\졸작\mykey.json'

######### 사물 인식 ##########
def detect_labels(image_path):
	client = vision.ImageAnnotatorClient()
	img = cv2.imread(image_path)

	with io.open(image_path, 'rb') as image_file:
		content = image_file.read()

	image = vision.Image(content=content)

	response = client.label_detection(image=image)
	labels = response.label_annotations

	for label in labels:
		print(label.description, end='  ')
#############################

######### 얼굴 인식 ##########
def detect_face(img, age_net, gender_net, MODEL_MEAN_VALUES, age_list, gender_list):
    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)

    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # dlib 얼굴 탐지 알고리즘
    faces = detector(image)

    print(len(faces), "명의 사람이 있습니다.")

    for box in faces:
        x, y, w, h = (box.left(), box.top(), box.width(), box.height())
        face = img[int(y):int(y + h), int(x):int(x + h)].copy()
        blob = cv2.dnn.blobFromImage(face, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        # gender detection
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        gender = gender_preds.argmax()
        # Predict age
        age_net.setInput(blob)
        age_preds = age_net.forward()
        age = age_preds.argmax()
        info = gender_list[gender] + ' ' + age_list[age]

        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, (64, 64))
        face_roi = np.expand_dims(face_roi, axis=-1)
        face_roi = np.expand_dims(face_roi, axis=0)
        face_roi = face_roi / 255.0
        # 모델을 통해 표정 분석
        output = model_emotion.predict(face_roi, verbose=0)[0]
        expression_index = np.argmax(output)
        expression_label = expression_labels[expression_index]


        print(f"{age_list[age]}살 {gender_list[gender]}가 {expression_label} 표정을 짓고 있습니다." )

#############################

# 이미지 저장 경로
os_path = 'img/'
image_path = 't4.png'
img_path = os_path+image_path

image = cv2.imread(img_path)

print("사물인식")
detect_labels(img_path)

print("\n\n얼굴인식")
detect_face(image,age_net,gender_net,MODEL_MEAN_VALUES,age_list,gender_list )

cv2.imshow("image", image)
cv2.waitKey(0)