# 👀 장애인의 생활 불편 해소 AI 음성비서 서비스
# 👀 AI Voice Assistant for Easing Disabilities
![24_PI009(발표자료) - 영상제거_page-0002](https://github.com/user-attachments/assets/5c0cac1b-4d78-4980-ac23-ed5406fe13ca)

본 프로젝트는 2024년 [프로보노 ICT멘토링](https://www.hanium.or.kr/portal/index.do)으로 진행되는 프로젝트 입니다.<br>
This project is part of the 2024 Pro Bono ICT Mentoring program.<br><br>
 
- Project Name : **ChatGPT 기반 장애인의 생활 불편 해소 AI 음성비서 서비스**<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                AI Voice Assistant Service Based on Chat GPT to Assist People with Disabilities
- Objective : **시각장애인 혼자서도 불편함 없이 생활할 수 있는 서비스 구현** <br>
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               To implement a service that enables visually impaired individuals to live independently without inconvenience
- Duration : `2024.04.01` ~ `2024.10.31` <br>

- Members
  
|Name|Role|
|:---:|:---:|
|[고형석](https://github.com/hyeongseokgo)|`Object Recognition`, `Face Recognition`|
|[유하영](https://github.com/Hayeonggg)|`Text Recognition`, `Sentence Generation`|
|[윤진영](https://github.com/jin7369)|`Speech Processing`, `App Development`|


<br><br>


***

## Introduction
본 프로젝트는 시각 정보를 음성으로 전달하여 시각장애인의 일상생활 자립을 지원하고 삶의 질을 향상시키는 것을 목표로 한다. 이를 위해 스마트폰 카메라를 통해 시각장애인들이 스스로 주변 정보를 확인할 수 있는 AI 음성비서 서비스를 제공한다.<br>
The goal of this project is to support the independence of visually impaired individuals in their daily lives and improve their quality of life by delivering visual information through audio. To achieve this, we provide an AI voice assistant service that allows visually impaired individuals to independently access information about their surroundings using a smartphone camera.<br><br>



## Key Features
- Object Recognition : 촬영된 사물에 대한 정확한 인식 및 정보 제공<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accurate recognition and information provision for captured objects<br>
- Face Recognition : 촬영된 얼굴에 대한 정보 제공(성별, 추정나이, 감정)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provides information on captured faces(gender, estimated age, emotion)<br>
- Text Recognition : 촬영된 문자를 인식하여 텍스트로 변환<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recognizes captured text and converts it into digital format<br>
- Sentence Generation : 사물 인식 결과를 문장으로 생성하여 출력<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates and outputs sentences based on object recognition results<br>
- Face Storage : 촬영된 얼굴에 대한 정보와 이름을 매치하여 저장<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores captured face information by matching it with a name<br>
- Speech Processing : 인식된 내용을 음성으로 변환하여 출력<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converts recognized content into audio and outputs it<br>




## Demo
[시연영상 보기(Watch Demo Video)](https://youtu.be/qjB4XeM9WYE?si=yhnpIZsHjzvN_7i6)
<br><br>

## System Architecture
![그림1](https://github.com/user-attachments/assets/f79c73a4-6e6c-4771-bf3a-a840064b2df4)


<br><br>

## 코드설명
(여기다가 순차적으로 써주세요)
예시)
- `text_recognition/` : 텍스트 인식
- `text_recognition/text-recognition.py` : 텍스트 인식을 위한 api 불러오기
- `lambda_functions/` : aws 람다 함수 모음
- `lambda_functions/face.py` : 얼굴 인식
- `lambda_functions/face_check.py` : 얼굴이 있는지 여부 확인
- `lambda_functions/face_save.py` : 얼굴 저장 기능
- `lambda_functions/object.py` : 사물 묘사 기능
- `lambda_functions/text.py` : 텍스트 인식 기능
- `lambda_functions/transcribe.py` : 음성을 텍스트로 변환 기능
- `lambda_functions/tts.py`:tts기능


## 앱 다운로드 방법
1. LifEye_no_url.aia파일을 다운로드 합니다.
2. 앱 인벤터에 접속하여 내 컴퓨터에서 프로젝트 불러오기를 합니다.
3. 각 기능에 맞게 세팅된 url을 앱 인벤터에서 입력해 넣습니다.



<br><br><br><br><br>
