# 먼저 컴퓨터 마이크로 실행되게 코드 짜봄
# 1. 파이썬 내장 라이브러리에 speech_recognition으로 마이크로 음성을 입력받는다.
# 2. 받은 음성 파일을 speech_recognition에 내장되어있는 recognize_google로 한글로 변환한다.
# 말만 google api이지 그냥 무료버전 느낌.

# 근데 서버에서는 마이크로 음성을 받는 것을 직접하기에는 힘들기 때문에 이런 순서로 진행하면 될 듯.
# 앱 인벤터의 기능 중 SoundRecorder 컴포넌트로 음성을 녹음 -> 음성 파일을 람다서버로 전송 ->
# 람다서버에서 그 음성을 recognition_google로 한글 변환 -> 변환된 값을 앱으로 return
# 이런 과정으로 하면 될듯함. 람다서버에서 파일 처리는 도움이 되었으면 해서 gpt한테 물어보고서 나온 코드를 주석으로 남겨놓을게.


# 컴퓨터 버전의 음성 받기
import speech_recognition as sr

# 음성 인식기 초기화
recognizer = sr.Recognizer()

def recognize_name_from_microphone():
    # 마이크로부터 음성 입력 받기
    with sr.Microphone() as source:
        print("음성 입력을 시작합니다. 이름을 말해주세요.")
        recognizer.adjust_for_ambient_noise(source)  # 소음 보정
        audio = recognizer.listen(source)  # 음성 듣기

    try:
        # 음성을 텍스트로 변환
        print("음성을 텍스트로 변환 중입니다...")
        text = recognizer.recognize_google(audio, language='ko-KR')  # Google API 사용
        print(f"이름: {text}")

    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"서비스에 접근할 수 없습니다: {e}")

# 함수 실행
recognize_name_from_microphone()


# 람다함수에 음성파일 받았을때 적용되는 코드 예시
# import speech_recognition as sr
#
#
# def lambda_handler(event, context):
#     # App Inventor에서 전송한 파일을 받기
#     audio_file = event['audio_file']
#
#     recognizer = sr.Recognizer()
#
#     with sr.AudioFile(audio_file) as source:
#         audio = recognizer.record(source)
#         text = recognizer.recognize_google(audio, language="ko-KR")
#
#     return {
#         'statusCode': 200,
#         'body': text
#     }
