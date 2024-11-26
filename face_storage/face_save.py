import face_recognition
import cv2
import os
import pickle

# 저장할 얼굴 데이터 파일 경로
face_data_file = 'face_data.pkl'


# 얼굴 데이터를 저장할 함수
def save_face_data(name, encoding):
    if os.path.exists(face_data_file):
        with open(face_data_file, 'rb') as f:
            face_data = pickle.load(f)
    else:
        face_data = {}

    face_data[name] = encoding
    with open(face_data_file, 'wb') as f:
        pickle.dump(face_data, f)
    print(f"얼굴이 {name}로 저장되었습니다.")


# 저장된 이름 리스트를 출력하는 함수
def list_saved_names():
    face_data_file = 'face_data.pkl'

    if os.path.exists(face_data_file):
        with open(face_data_file, 'rb') as f:
            face_data = pickle.load(f)

        if face_data:
            print("저장된 사람들:")
            for name in face_data.keys():
                print(f"- {name}")
        else:
            print("저장된 얼굴 데이터가 없습니다.")
    else:
        print("face_data.pkl 파일이 없습니다.")


# 저장된 얼굴 데이터 로드 함수
def load_face_data():
    if os.path.exists(face_data_file):
        with open(face_data_file, 'rb') as f:
            return pickle.load(f)
    else:
        return {}


# 얼굴을 저장하는 기능
def save_face():
    # 사진 요청
    file_path = input("사진 파일 경로를 입력하세요: ")
    image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    if len(face_encodings) > 0:
        encoding = face_encodings[0]
        name = input("이 사람의 이름은 무엇입니까?: ")
        save_face_data(name, encoding)
    else:
        print("사진에서 얼굴을 인식하지 못했습니다.")


# 얼굴을 인식하는 기능
def recognize_face():
    # 사진 요청
    file_path = input("사진 파일 경로를 입력하세요: ")
    image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # 사진에서 얼굴이 있는가 ?
    if len(face_encodings) > 0:
        face_data = load_face_data()
        tolerance = 0.5  # 유사도 비교를 위한 tolerance 값
        found_any_match = False  # 적어도 한 명의 얼굴이 일치하는가?

        if face_data:
            for encoding in face_encodings:
                # 각 얼굴의 인코딩을 저장된 얼굴들과 비교
                for name, saved_encoding in face_data.items():
                    face_distance = face_recognition.face_distance([saved_encoding], encoding)

                    if face_distance[0] < tolerance:
                        print(f"이 사진에 {name}가 있습니다.")
                        found_any_match = True  # 적어도 한 명의 얼굴이 일치함
                        break

            # 일치하는 얼굴이 없는 경우에만 메시지 출력
            if not found_any_match:
                print("유사한 얼굴이 없습니다.")
        else:
            print("저장된 얼굴 데이터가 없습니다.")
    else:
        print("사진에서 얼굴을 인식하지 못했습니다.")


# 메인
print("1. 얼굴 저장")
print("2. 얼굴 인식 촬영")
print("3. 저장된 이름 확인")

choice = input("선택하세요 : ")
if choice == '1':
    save_face()
elif choice == '2':
    recognize_face()
elif choice == '3':
    list_saved_names()
else:
    print("잘못된 입력입니다.")

