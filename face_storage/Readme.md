# 얼굴 저장 기능

## 기능 설명

저장하고 싶은 얼굴의 사진을 입력하고 이름을 저장하면 얼굴인식 기능을 사용할 때 저장한 얼굴의 이름도 같이 출력하는 기능이다.

## 구현 방법 시나리오

1. 저장 기능을 실행하고 얼굴 사진을 입력하면 dlib의 face_recognition을 사용하여 해당 얼굴의 landmarks값을 추출한다.
2. 이 값을 해당 얼굴의 이름과 함께 pickle파일 형태로 저장한다.
3. 저장한 이후에는 얼굴인식 기능을 사용할때마다 저장되어 있는 얼굴 landmarks 값과 비교하여 일정 유사도 임계치를 넘기게 되면 저장되어 있는 이름과 같이 출력하게 된다.


## 예시
![KakaoTalk_20241006_233154781_10](https://github.com/user-attachments/assets/57820aba-3efb-463b-a4d2-81a51a6da82f) ![KakaoTalk_20241006_233154781_11](https://github.com/user-attachments/assets/58caf2c6-7c96-4a9f-85fe-6a2747eaa463)


