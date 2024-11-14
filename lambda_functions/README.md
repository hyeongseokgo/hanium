# 얼굴 인식 Lambda 함수 (face.py)

이 AWS Lambda 함수는 이미지에서 얼굴을 감지하고, 성별, 연령, 감정 등의 속성을 분석하며 Amazon Rekognition 컬렉션에서 일치하는 얼굴을 검색한다. 일치하는 얼굴이 발견되면 해당 인물의 이름을 반환한다. 이 함수는 AWS Rekognition을 사용하며, 이미지가 base64로 인코딩된 문자열로 HTTP POST 요청을 통해 전달될 것으로 기대한다.

## 요구 사항

이 함수를 사용하려면 다음이 필요하다:
- AWS 계정
- Amazon Rekognition 컬렉션 (얼굴 매칭용)
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `boto3` 라이브러리

## 설정

1. **AWS 자격 증명 및 Rekognition 컬렉션**: Lambda 함수가 Rekognition을 사용할 수 있도록 필요한 AWS 자격 증명 및 권한을 부여해야 한다. Rekognition 컬렉션을 사전에 생성해야 한다.

2. **환경 변수**: `face.py` 파일 내의 변수를 사용자에 맞는 값으로 업데이트한다.
   - `ACCESS_KEY`: Rekognition 권한이 있는 AWS 액세스 키
   - `SECRET_KEY`: AWS 비밀 액세스 키
   - `REGION`: Rekognition 서비스가 호스팅된 AWS 리전
   - `collection_id`: 얼굴 매칭에 사용될 Rekognition 컬렉션 ID

## 코드 설명

- **`lambda_handler` 함수**: 이미지를 처리하고 얼굴 감지 및 인식 결과를 반환하는 주요 함수다.

### 주요 코드 섹션

- **데이터 디코딩**: 이벤트 본문에서 base64로 인코딩된 이미지를 디코딩한다.
- **얼굴 감지**: Rekognition의 `detect_faces` 메서드를 사용하여 얼굴을 감지하고 성별, 연령, 감정 등의 속성을 분석한다.
- **얼굴 매칭**: Rekognition 컬렉션에서 `search_faces_by_image` 메서드를 사용하여 감지된 얼굴을 검색해 등록된 인물의 이름을 식별한다.
- **현지화**: `eng_to_kor` 딕셔너리는 응답을 위해 영어 레이블을 한국어 레이블로 변환한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 이미지)

함수는 `body` 파라미터에 base64로 인코딩된 이미지가 포함된 HTTP POST 요청을 받는다.

#### 응답 예시 (얼굴 감지됨)

```json
{
  "statusCode": 200,
  "body": "20~30세 정도의 남성이 행복한 표정을 하고있어요"
}


# Face Detection Lambda Function (face_check.py)

이 AWS Lambda 함수는 Amazon Rekognition의 `detect_faces` 기능을 이용해 이미지에서 얼굴을 감지하고, 감지된 얼굴의 수를 반환한다. 이 함수는 base64로 인코딩된 이미지 데이터를 HTTP POST 요청을 통해 입력받으며, Rekognition을 사용해 얼굴이 몇 개 있는지 계산하여 반환한다.

## 요구 사항

이 함수를 사용하려면 다음이 필요하다:
- AWS 계정
- Amazon Rekognition 권한이 있는 IAM 사용자 또는 역할
- AWS Lambda 및 API Gateway (함수 배포 및 엔드포인트 노출용)
- Python 3.x 및 `boto3` 라이브러리

## 설정

1. **AWS 자격 증명 설정**: `face_check.py` 파일의 AWS 자격 증명을 자신의 환경에 맞게 설정한다.
   - `ACCESS_KEY`: Rekognition 권한이 있는 AWS 액세스 키
   - `SECRET_KEY`: AWS 비밀 액세스 키
   - `REGION`: Rekognition 서비스가 설정된 AWS 리전

2. **AWS 서비스 권한**: 이 Lambda 함수는 Rekognition 서비스를 호출할 수 있어야 하므로, Rekognition 권한이 포함된 IAM 역할을 Lambda 함수에 설정한다.

## 코드 설명

- **`lambda_handler` 함수**: 이미지 데이터를 받아 얼굴 감지 요청을 실행하고, 감지된 얼굴의 수를 반환하는 주요 함수다.

### 주요 코드 섹션

- **데이터 디코딩**: Lambda 함수가 base64로 인코딩된 데이터를 event에서 받아 이중 디코딩한다.
- **얼굴 감지**: Rekognition의 `detect_faces` 메서드를 호출하여 이미지에서 얼굴을 감지하고, 감지된 얼굴의 개수를 반환한다.

### 예시 요청 및 응답

#### 요청 (Base64 인코딩 이미지)

Lambda 함수는 `body` 파라미터에 base64로 인코딩된 이미지가 포함된 HTTP POST 요청을 기대한다.

#### 응답 예시 (얼굴 수 감지)

```json
{
  "statusCode": 200,
  "body": "3"
}
