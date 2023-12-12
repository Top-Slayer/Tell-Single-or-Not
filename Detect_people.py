import cv2
import os
import time
import pygame
import random
import face_recognition as fr
from threading import Thread

from gtts import gTTS
from datetime import datetime


# Variables
# ------------------------------------------------------
status_voice = True
status_compare_img = True

first_check = True

# ------------------------------------------------------


# Objects
# ------------------------------------------------------
cap = cv2.VideoCapture(0)  # dont forget to change to 0 for webcam equipment

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# ------------------------------------------------------


# All function for processing
# Play sound function
# ------------------------------------------------------
def play_sound(value, sound_text, save_status):
    pygame.mixer.init()

    print("--> Talking...")

    myobj = gTTS(text=sound_text, lang="th", slow=False)
    myobj.save("output.wav")

    my_sound = pygame.mixer.Sound("output.wav")
    my_sound.play()
    pygame.time.wait(int(my_sound.get_length() * 1000))

    check_pic = cv2.imread("check_Picture.png")
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    formatted_time_str = str(formatted_time)

    image_path = str()

    # options to talking out
    # ------------------------------------------------------------------
    if value == 0 and save_status == True:
        image_path = f"types/คนเจ้าชู้/{formatted_time_str}.png"

    elif value == 1 and save_status == True:
        image_path = f"types/คนรักเดียวใจเดียว/{formatted_time_str}.png"

    elif value == 2 and save_status == True:
        image_path = f"types/คนโสด/{formatted_time_str}.png"

    elif value == 3 and save_status == True:
        image_path = f"types/คุณดูเหมือนคนเจ้าชู้อ่ะหยอกเล่น/{formatted_time_str}.png"

    elif value == 4 and save_status == True:
        image_path = f"types/คนอะไรน่ารักจัง/{formatted_time_str}.png"
    # ------------------------------------------------------------------

    if save_status == True:
        print("\n--> Image path: " + image_path)
    else:
        print("\n--> Image path: This image is existed")

    try:
        if save_status == True:
            cv2.imwrite(image_path, check_pic)
            print("--> Image saved successfully!")
    except Exception as e:
        print(f"--> Error saving image: {e}")

    global status_voice
    status_voice = True


# ------------------------------------------------------


# Detect same faces function
# ------------------------------------------------------
def detect_same_faces():
    start_time = time.time()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    check_image = cv2.imread("check_Picture.png")
    folder = [
        r"types\คนเจ้าชู้",
        "types\คนรักเดียวใจเดียว",
        "types\คนโสด",
        "types\คุณดูเหมือนคนเจ้าชู้อ่ะหยอกเล่น",
        "types\คนอะไรน่ารักจัง",
    ]
    score_folders = [0, 0, 0, 0, 0]
    indexOfScore_folders = score_folders.index(min(score_folders))

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    formatted_time_str = str(formatted_time)

    i = int(0)
    while i < len(folder):
        for filename in os.listdir(folder[i]):
            find_image = cv2.imread(os.path.join(folder[i], filename))

            gray_image1 = cv2.cvtColor(check_image, cv2.COLOR_BGR2GRAY)
            gray_image2 = cv2.cvtColor(find_image, cv2.COLOR_BGR2GRAY)

            faces1 = face_cascade.detectMultiScale(
                gray_image1, scaleFactor=1.1, minNeighbors=5
            )
            faces2 = face_cascade.detectMultiScale(
                gray_image2, scaleFactor=1.1, minNeighbors=5
            )

            if len(faces1) == 1 and len(faces2) == 1:
                x1, y1, w1, h1 = faces1[0]
                x2, y2, w2, h2 = faces2[0]

                face1 = gray_image1[y1 : y1 + h1, x1 : x1 + w1]
                face2 = gray_image2[y2 : y2 + h2, x2 : x2 + w2]

                avg_intensity1 = face1.mean()
                avg_intensity2 = face2.mean()

                compare_face_value = round(abs(avg_intensity1 - avg_intensity2), 2)
                threshold = 20

                print(
                    "\n> Face comparing value: ",
                    compare_face_value,
                )

                if compare_face_value < threshold:
                    print(f"=> Faces match: [ {folder[i][6:]} ]")

                if score_folders[i] < compare_face_value:
                    score_folders[i] = compare_face_value
        i += 1

    # if os.listdir(folder[0]) == []:
    #     rand_num = random.randint(0, len(folder) - 1)
    #     play_sound(rand_num, folder[rand_num][6:], True)

    print("\n> Searching... ", score_folders)
    print(
        f"=> Procress first folder: {folder[indexOfScore_folders][6:]} - Index[ {indexOfScore_folders} ]"
    )

    global first_check

    # if first_check == True:
    #     first_check = False
    #     rand_num = random.randint(0, len(folder) - 1)
    #     play_sound(rand_num, folder[rand_num][6:], True)
    # else:
    rand_num = random.randint(0, len(folder) - 1)
    play_sound(rand_num, folder[rand_num][6:], False)

    global status_compare_img
    status_compare_img = True

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n--> Compare-Faces end times: {elapsed_time:.2f} seconds")


# ------------------------------------------------------


print("Processing...")
# ------------------------------------------------------

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    # main processing
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    # Draw rectangles around detected faces
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 106, 42), 2)

        position_circle = (x + w // 2, y + h // 2)
        position_start_line = (320, 240)
        cv2.line(frame, position_start_line, position_circle, (0, 0, 255), 1)
        cv2.circle(frame, position_circle, 3, (0, 255, 0), 2)
        total = position_circle[0] - position_start_line[0]

        text = "Detecting-Face"

        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (47, 173, 255),
            2,
        )

        if status_voice and status_compare_img:
            status_voice = False
            status_compare_img = False
            Thread(target=detect_same_faces).start()
            cv2.imwrite("check_Picture.png", frame)

            print("-----------------------------------------------------")

    # display camera
    cv2.imshow("Detect people", frame)

    # wait for pressed q letter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("\nEnding...")
        break

cap.release()
cv2.destroyAllWindows()
