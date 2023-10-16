from threading import Thread

import cv2
import os
import time
import pygame
import random
from gtts import gTTS
from datetime import datetime


# Variables
# ------------------------------------------------------
status = True

# ------------------------------------------------------


# Objects
# ------------------------------------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap = cv2.VideoCapture(0)  # dont forget to change to 0 for webcam equipment
# ------------------------------------------------------


# All function for processing
# Play sound function
# ------------------------------------------------------
def play_sound():
    random_text = ["คนรักเดียวใจเดียว", "คนเจ้าชู้", "คนโสด"]
    rand_num = random.randrange(0, len(random_text))

    pygame.mixer.init()

    print(f"[ {rand_num} ]  {random_text[rand_num]}")
    print("--> Talking...")

    myobj = gTTS(text=random_text[rand_num], lang="th", slow=False)
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
    if rand_num == 0:
        image_path = f"types/คนรักเดียวใจเดียว/{formatted_time_str}.png"

    elif rand_num == 1:
        image_path = f"types/คนเจ้าชู้/{formatted_time_str}.png"

    elif rand_num == 2:
        image_path = f"types/คนโสด/{formatted_time_str}.png"
    # ------------------------------------------------------------------

    print("\n--> Image path: " + image_path)

    try:
        cv2.imwrite(image_path, check_pic)
        print("--> Image saved successfully!")
    except Exception as e:
        print(f"--> Error saving image: {e}")

    global status
    status = True


# ------------------------------------------------------


print("Processing...")

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

        text = "Human-Face"

        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (47, 173, 255),
            2,
        )

        if status:
            Thread(target=play_sound).start()
            cv2.imwrite("check_Picture.png", frame)
            status = False

        print(".", end=(" "))

    # display camera
    cv2.imshow("Detect people", frame)

    # wait for pressed q letter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("\nEnding...")
        break

cap.release()
cv2.destroyAllWindows()
