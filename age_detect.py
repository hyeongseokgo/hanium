import cv2
import dlib

# 사진 검출기
def imgDetector(img, age_net, gender_net, MODEL_MEAN_VALUES, age_list, gender_list):
    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cascade 얼굴 탐지 알고리즘

    faces = detector(image)

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
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)
        cv2.putText(img, info, (x, y - 15), 0, 0.5, (0, 255, 0), 1)

    # 사진 출력
    cv2.imshow('facenet', img)
    cv2.waitKey(0)

# 얼굴 인식기 로드 (dlib)
detector = dlib.get_frontal_face_detector()

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# 언령 예측 모델 불러오기
age_net = cv2.dnn.readNetFromCaffe(
	'models/deploy_age.prototxt',
	'models/age_net.caffemodel')

# 성별 예측 모델 불러오기
gender_net = cv2.dnn.readNetFromCaffe(
	'models/deploy_gender.prototxt',
	'models/gender_net.caffemodel')


age_list = ['(0 ~ 2)', '(4 ~ 6)', '(8 ~ 12)', '(15 ~ 20)',
            '(25 ~ 32)', '(38 ~ 43)', '(48 ~ 53)', '(60 ~ 100)']
gender_list = ['Male', 'Female']

# 이미지 로드
os_path = 'img/'

image_path = 'face_test.png'
image_path = 'ffhq-examples.png'
image_path = 'gaffney-group.jpg'
image_path = 'Lee_DiCaprio.jpg'
image_path = 'twice2.jpg'
image_path = 'vikings_big.jpg'

image = cv2.imread(os_path+image_path)


# 얼굴 감지
faces = detector(image)

cv2.imshow('Image', image)
cv2.waitKey(0)

# 사진 탐지기
imgDetector(image,age_net,gender_net,MODEL_MEAN_VALUES,age_list,gender_list )