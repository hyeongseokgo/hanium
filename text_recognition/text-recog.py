import os
import io
from google.cloud import vision

# 환경 변수 설정: Google Cloud 인증 파일 경로 지정
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Your API'

# 클라이언트 객체 생성
client = vision.ImageAnnotatorClient()

# 이미지 파일 경로
image_path = os.path.abspath('2.jpg')  # 분석할 이미지 파일 이름을 'image_with_text.jpg'로 가정

# 이미지 파일을 열고 바이너리 데이터를 Vision API로 전송
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# OCR 요청 보내기
response = client.document_text_detection(image=image)
document = response.full_text_annotation

# 전체 텍스트 출력
if document.text:
    document_text = document.text
    print("\nFull Text:\n", document_text)

    # 페이지 단위로 텍스트 정보 출력
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])

                    # 경계 상자 정보
                    vertices = (['({},{})'.format(vertex.x, vertex.y)
                                for vertex in word.bounding_box.vertices])

                    # 확신도 점수 (심볼 수준에서 평균 계산)
                    symbol_confidences = [symbol.confidence for symbol in word.symbols if hasattr(symbol, 'confidence')]
                    confidence = sum(symbol_confidences) / len(symbol_confidences) if symbol_confidences else 'N/A'

                    print(f'텍스트: "{word_text}" / "{confidence}"')
                    #print(f'경계 상자: {vertices}')
                    #print(f'확신도: {confidence}')

else:
    print('No text detected.')

# 에러 핸들링
if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(response.error.message))
