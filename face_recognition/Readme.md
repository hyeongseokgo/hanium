# 얼굴 인식 기능

## 기능 설명

사진을 입력하면 몇명의 사람이 있는지, 각 얼굴마다 예측한 나이, 성별, 감정을 출력하여 사용자에게 알려주는 기능이다.

## 구현 방법 시나리오

1. 얼굴 인식 기능을 실행하고 얼굴 사진을 입력한다.
2. dlib의 face_recognition을 사용하여 해당 얼굴의 landmarks값을 추출한다.
3. 각각 나이, 성별, 감정을 학습시킨 모델에 landmarks값을 입력하여 각 기능을 예측한다.

- 각 모델은 따로 제작하거나 다른 프로젝트의 모델을 불러서 사용하였다.

## 예시
![KakaoTalk_20241006_233154781_06](https://github.com/user-attachments/assets/0d540f0a-f7a0-45cb-894e-7851ab862a25)

