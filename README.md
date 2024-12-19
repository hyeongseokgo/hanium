# 👀 장애인의 생활 불편 해소 AI 음성비서 서비스<br>(AI Voice Assistant for Easing Disabilities)
![그림1](https://github.com/user-attachments/assets/a5bcd201-0779-4ea3-a985-880a78aff180)


본 프로젝트는 2024년 [프로보노 ICT멘토링](https://www.hanium.or.kr/portal/index.do)으로 진행된 프로젝트 입니다.<br>
This project is part of the 2024 Pro Bono ICT Mentoring program.<br><br>
 
- Project Name : **ChatGPT 기반 장애인의 생활 불편 해소 AI 음성비서 서비스**
 (AI Voice Assistant Service Based on Chat GPT to Assist People with Disabilities)
- Objective : **시각장애인 혼자서도 불편함 없이 생활할 수 있는 서비스 구현**
(To implement a service that enables visually impaired individuals to live independently without inconvenience)
- Duration : `2024.04.01` ~ `2024.10.31` <br>

- Members<br>
  + [고형석](https://github.com/hyeongseokgo) : `Object Recognition`, `Face Recognition`
  
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
▶ [Full Demo Video](https://youtu.be/qjB4XeM9WYE?si=yhnpIZsHjzvN_7i6)
<br>
![online-video-cutter com-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/0412e828-f968-43ed-8b68-21bca587ebf5)


<br>


<br><br>

## System Architecture
![그림1](https://github.com/user-attachments/assets/f79c73a4-6e6c-4771-bf3a-a840064b2df4)


<br><br>

## Folder structure
```
# Documents
Docs                # 보고서 파일
└── ...

# Face Recognition
face_recognition
├── img             # 예시 이미지
└── face_recog      # 얼굴 이미지 묘사 

# Face Storage
face_storage
├── img             # 예시 이미지
└── face_save       # 얼굴 이미지 묘사 

# Text Recognition
text_recognition
├── img             # 예시 이미지
└── text_recog      # OCR 이미지-텍스트 변환


# AWS Lambda functions
App_Inventor
  ├── lambda_functions  # AWS Lambda functions
  │    ├── face.py         # 얼굴 인식
  │    ├── face_check.py   # 얼굴 존재 여부 확인
  │    ├── face_save.py    # 얼굴 저장
  │    ├── object.py       # 사물 묘사
  │    ├── text.py         # 텍스트 인식
  │    ├── transcribe.py   # 음성->텍스트 변환
  │    └── tts.py          # tts
  └── LifEye_no_url.aia # App Inventor project file
```



## How to Launch Our App
1. Download the `LifEye_no_url.aia` file.
2. Access **App Inventor** and import the project from your computer.
3. Enter the URLs set for each function in App Inventor.

## Reference
huggingface/transformers (https://github.com/huggingface/transformers)

<br><br><br><br><br>
