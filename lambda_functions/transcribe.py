import boto3
import json
import base64
import speech_recognition as sr
from pydub import AudioSegment
import io

AudioSegment.ffmpeg = "/opt/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/bin/ffprobe"
def lambda_handler(event, context):
    try:
        recognizer = sr.Recognizer()
        data = base64.b64decode(event['body'])
        data = base64.b64decode(data)
        
        audio_io = io.BytesIO(data)
        
        audio_segment = AudioSegment.from_file(audio_io, format='3gp')
        wav_io = io.BytesIO()
        audio_segment.export(wav_io, format="wav")
        wav_io.seek(0)
    except Exception as e:
        return {
            'statusCode' : 400,
            'body' : json.dumps(f"파일 처리 오류, {e}", ensure_ascii=False)
        }
    
    try:
        with sr.AudioFile(wav_io) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='ko-KR')
        
        return {
            'statusCode' : 200,
            'body' : json.dumps(text, ensure_ascii=False)
        }
    except sr.UnknownValueError:
        return {
            'statusCode' : 500,
            'body' : json.dumps("음성을 인식할 수 없습니다.", ensure_ascii=False)
        }
    except sr.RequestError as e:
        return {
            'statusCode' : 500,
            'body' : json.dumps("하루 요청 횟수가 만료되었습니다.", ensure_ascii=False)
        }
    except:
        return {
            'statusCode' : 500,
            'body' : json.dumps("음성 인식 오류", ensure_ascii=False)
        }
