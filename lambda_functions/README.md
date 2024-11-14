# 얼굴 인식 및 감지 Lambda 함수 (face.py & face_check.py)

이 AWS Lambda 프로젝트는 Amazon Rekognition을 사용하여 이미지에서 얼굴을 감지하고 분석하는 두 가지 Lambda 함수를 포함한다. 이 함수들은 이미지에서 얼굴의 수를 감지하거나, 얼굴의 성별, 연령, 감정 등의 속성을 분석하며, 필요 시 Rekognition 컬렉션을 통해 일치하는 얼굴을 검색할 수도 있다. 이 두 함수는 base64로 인코딩된 이미지 데이터를 HTTP POST 요청으로 입력받아 동작한다.

## 요구 사항

이 Lambda 함수를 사용하려면 다음이 필요하다:
- AWS 계정
- Amazon Rekognition 컬렉션 (얼굴 매칭용)
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `boto3` 라이브러리

## 설정

1. **AWS 자격 증명 및 Rekognition 컬렉션**: Lambda 함수가 Rekognition을 사용할 수 있도록 필요한 AWS 자격 증명 및 권한을 부여해야 한다. Rekognition 컬렉션을 사전에 생성해야 한다.

2. **환경 변수 설정**: `face.py` 및 `face_check.py` 파일 내의 변수들을 사용자의 환경에 맞게 설정한다.
   - `ACCESS_KEY`: Rekognition 권한이 있는 AWS 액세스 키
   - `SECRET_KEY`: AWS 비밀 액세스 키
   - `REGION`: Rekognition 서비스가 설정된 AWS 리전
   - `collection_id` (face.py에서 사용): 얼굴 매칭에 사용될 Rekognition 컬렉션 ID

## 코드 설명

### face_check.py

- **기능**: Rekognition의 `detect_faces` 기능을 이용해 이미지에서 얼굴을 감지하고, 감지된 얼굴의 수를 반환한다.

- **`lambda_handler` 함수**: 이미지 데이터를 받아 이중 base64 디코딩 후 Rekognition을 통해 얼굴을 감지하여 감지된 얼굴의 개수를 반환한다.

### face.py

- **기능**: Rekognition을 사용해 이미지에서 얼굴을 감지하고 성별, 연령, 감정 등의 속성을 분석하며, Rekognition 컬렉션에서 일치하는 얼굴을 검색하여 인물 이름을 반환할 수 있다.

- **`lambda_handler` 함수**: 이미지 데이터를 처리하고 얼굴 속성을 분석하여 감지된 얼굴의 성별, 연령, 감정을 반환하고, Rekognition 컬렉션에서 일치하는 얼굴이 있으면 해당 인물의 이름을 반환한다.

### 주요 코드 설명

- **데이터 디코딩**: Lambda 함수는 event에서 base64로 인코딩된 이미지를 받으며, 이를 이중 디코딩하여 Rekognition API 요청에 사용한다.
- **얼굴 감지**: `detect_faces` 메서드를 사용하여 얼굴을 감지하고, 감지된 얼굴 수 및 각 얼굴의 성별, 연령, 감정 정보를 분석한다.
- **얼굴 매칭 (face.py에서만 사용)**: Rekognition 컬렉션의 `search_faces_by_image` 메서드를 통해 얼굴 매칭을 수행하여 인식된 인물 이름을 식별할 수 있다.
- **현지화 (face.py에서만 사용)**: `eng_to_kor` 딕셔너리를 사용하여 영어 레이블을 한국어 레이블로 변환한다.

## 예시 요청 및 응답

### 요청 (Base64 인코딩 이미지)

Lambda 함수는 `body` 파라미터에 base64로 인코딩된 이미지가 포함된 HTTP POST 요청을 기대한다.

### 응답 예시

#### face_check.py (얼굴 수 감지)

```json
{
  "statusCode": 200,
  "body": "3"
}
```

# 얼굴 등록 Lambda 함수 (face_save.py)

이 Lambda 함수는 Amazon Rekognition의 `index_faces` 기능을 사용하여 얼굴을 등록하고, 이름과 이미지를 기반으로 Rekognition 컬렉션에 얼굴 데이터를 저장한다. HTTP POST 요청을 통해 base64로 인코딩된 이미지와 인물 이름을 입력받아 얼굴을 Rekognition 컬렉션에 저장한다.

## 요구 사항

이 Lambda 함수를 사용하려면 다음이 필요하다:
- AWS 계정
- Amazon Rekognition 컬렉션 (얼굴 저장용)
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `boto3` 라이브러리

## 설정

1. **AWS 자격 증명 및 Rekognition 컬렉션**: `face_save.py` 파일 내의 AWS 자격 증명을 설정하고, 사용자의 AWS 환경에 맞는 Rekognition 컬렉션 ID를 지정한다.
   - `ACCESS_KEY`: Rekognition 권한이 있는 AWS 액세스 키
   - `SECRET_KEY`: AWS 비밀 액세스 키
   - `REGION`: Rekognition 서비스가 설정된 AWS 리전
   - `collection_id`: 얼굴 데이터를 저장할 Amazon Rekognition 컬렉션 ID

2. **AWS 서비스 권한**: 이 Lambda 함수는 Rekognition 서비스를 호출할 수 있어야 하므로, Rekognition 권한이 포함된 IAM 역할을 Lambda 함수에 설정한다.

## 코드 설명

- **`lambda_handler` 함수**: HTTP POST 요청에서 이미지와 인물 이름을 받아 얼굴을 등록하는 함수다.

### 주요 코드 설명

- **데이터 디코딩**: Lambda 함수는 event에서 전달된 base64로 인코딩된 이미지와 이름 데이터를 받아 디코딩한다.
- **이름 인코딩**: 얼굴 데이터를 Rekognition 컬렉션에 저장하기 전에, UTF-8로 인코딩한 이름을 hex로 변환하여 `ExternalImageId`로 설정한다.
- **얼굴 등록**: Rekognition의 `index_faces` 메서드를 사용해 컬렉션에 얼굴 데이터를 저장한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 이미지 및 이름)

Lambda 함수는 `body` 파라미터로 JSON 형식의 `image`와 `name` 데이터를 포함한 HTTP POST 요청을 기대한다.

```json
{
  "image": "<base64_encoded_image_data>",
  "name": "<base64_encoded_name>"
}
```
# 객체 감지 및 번역 Lambda 함수 (object.py)

이 Lambda 함수는 외부 객체 감지 API와 Googletrans 라이브러리를 사용하여 이미지에서 객체를 감지하고 결과를 한국어로 번역하는 기능을 제공한다. 클라이언트로부터 base64로 인코딩된 이미지를 HTTP POST 요청으로 받아 객체 감지 API를 호출하고, 반환된 텍스트를 한국어로 번역하여 응답한다.

## 요구 사항

이 Lambda 함수를 사용하려면 다음이 필요하다:
- 외부 객체 감지 API 엔드포인트
- API 호출에 필요한 헤더 정보
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `requests`, `googletrans` 라이브러리

## 설정

1. **외부 객체 감지 API 설정**: 객체 감지 API의 엔드포인트 URL을 `API_URL` 변수에 설정하고, 필요한 인증 정보를 `headers`에 설정한다.
   - `API_URL`: 객체 감지 API의 엔드포인트 URL
   - `headers`: API 호출 시 필요한 인증 헤더

2. **AWS 환경 설정**: 이 Lambda 함수를 AWS에 배포하고, API Gateway를 통해 엔드포인트를 설정하여 HTTP POST 요청을 받을 수 있도록 한다.

## 코드 설명

- **`lambda_handler` 함수**: 이 함수는 이미지 데이터를 받아 객체 감지 API를 호출하고, 응답을 한국어로 번역하여 클라이언트에 반환한다.

### 주요 코드 설명

- **데이터 디코딩**: Lambda 함수는 event에서 전달된 base64로 인코딩된 이미지를 받아 이중 디코딩하여 객체 감지 API에 전달할 준비를 한다.
- **객체 감지**: `requests.post()` 메서드를 통해 객체 감지 API를 호출하고, API의 응답 JSON에서 `generated_text` 필드를 추출한다.
- **번역**: Googletrans 라이브러리를 사용하여 객체 감지 결과를 한국어로 번역한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 이미지)

Lambda 함수는 `body` 파라미터에 base64로 인코딩된 이미지가 포함된 HTTP POST 요청을 기대한다.

```json
{
  "image": "<base64_encoded_image_data>"
}
```

# 문서 텍스트 감지 Lambda 함수 (text.py)

이 Lambda 함수는 Google Cloud Vision API를 사용하여 이미지를 분석하고, 이미지 내의 문자를 추출하는 기능을 제공한다. 클라이언트로부터 base64로 인코딩된 이미지를 HTTP POST 요청으로 받아 Google Vision API의 `document_text_detection` 기능을 호출하여 문서를 감지하고, 그 결과를 반환한다.

## 요구 사항

이 Lambda 함수를 사용하려면 다음이 필요하다:
- Google Cloud Vision API 활성화
- Google Cloud 서비스 계정 키 (JSON 형식)
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `google-cloud-vision` 라이브러리

## 설정

1. **Google Cloud 서비스 계정 키**: Google Cloud의 Vision API를 사용하려면 서비스 계정 키를 생성하여 `GOOGLE_APPLICATION_CREDENTIALS` 환경 변수에 설정해야 한다.
   - `GOOGLE_APPLICATION_CREDENTIALS`: Google Cloud Vision API를 호출할 때 사용할 서비스 계정 JSON 키 파일의 경로

2. **AWS 환경 설정**: 이 Lambda 함수를 AWS에 배포하고, API Gateway를 통해 엔드포인트를 설정하여 HTTP POST 요청을 받을 수 있도록 한다.

## 코드 설명

- **`lambda_handler` 함수**: 이 함수는 클라이언트로부터 받은 base64로 인코딩된 이미지를 디코딩한 후, Google Cloud Vision API를 호출하여 문서 내 텍스트를 감지한다.

### 주요 코드 설명

- **데이터 디코딩**: Lambda 함수는 `event`에서 전달된 base64로 인코딩된 이미지 데이터를 받아 디코딩한다.
- **Google Vision API 호출**: `vision.ImageAnnotatorClient()`를 사용하여 Google Cloud Vision API의 `document_text_detection` 메서드를 호출한다.
- **텍스트 추출**: `response.full_text_annotation`을 통해 이미지 내의 문자를 추출하고, 이를 응답으로 반환한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 이미지)

Lambda 함수는 `body` 파라미터에 base64로 인코딩된 이미지가 포함된 HTTP POST 요청을 기대한다.

```json
{
  "image": "<base64_encoded_image_data>"
}
```

# 음성 인식 Lambda 함수 (transcribe.py)

이 Lambda 함수는 음성 파일을 받아 Google Speech Recognition API를 사용하여 음성을 텍스트로 변환한다. 클라이언트로부터 base64로 인코딩된 음성 데이터를 HTTP POST 요청으로 받아, 이를 WAV 형식으로 변환 후 텍스트로 변환하여 반환한다.

## 요구 사항

이 Lambda 함수를 사용하려면 다음이 필요하다:
- Python 3.x
- `speechrecognition`, `pydub`, `boto3` 패키지
- `ffmpeg` 및 `ffprobe` 바이너리 (Lambda 함수 실행 환경에 포함되어야 함)
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)

## 설정

1. **음성 파일 포맷**: Lambda 함수는 `.3gp` 형식의 음성 파일을 받아 처리하며, 이를 WAV 형식으로 변환 후 인식한다. 다른 포맷을 사용하려면 코드에서 적절한 형식으로 수정이 필요하다.

2. **`ffmpeg` 설정**: `pydub` 라이브러리는 `ffmpeg`를 사용하여 음성 파일을 처리한다. `ffmpeg`는 Lambda의 `/opt/bin/` 경로에 위치해야 한다.

3. **AWS Lambda 배포**: Lambda 함수에서 `speechrecognition`, `pydub`, `boto3` 라이브러리와 `ffmpeg`, `ffprobe` 바이너리 파일을 포함하여 배포해야 한다. 이를 위해 Lambda 함수 배포 패키지에 필요한 라이브러리와 바이너리를 함께 포함시켜야 한다.

## 코드 설명

- **`lambda_handler` 함수**: 이 함수는 Lambda 이벤트에서 전달된 base64로 인코딩된 음성 파일을 처리하고, 이를 WAV 형식으로 변환 후 Google Speech Recognition API를 호출하여 음성을 텍스트로 변환한다.

### 주요 코드 설명

- **데이터 디코딩**: Lambda 함수는 `event`에서 전달된 base64로 인코딩된 음성 데이터를 받아 디코딩하고 `io.BytesIO` 객체로 변환하여 처리한다.
- **음성 파일 변환**: `pydub.AudioSegment`를 사용하여 `.3gp` 형식의 음성 파일을 WAV 형식으로 변환한다.
- **음성 인식**: `speechrecognition.Recognizer` 객체를 사용하여 Google Speech Recognition API로 음성을 텍스트로 변환한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 음성 파일)

Lambda 함수는 `body` 파라미터에 base64로 인코딩된 음성 파일이 포함된 HTTP POST 요청을 기대한다.

```json
{
  "audio": "<base64_encoded_audio_data>"
}
```
