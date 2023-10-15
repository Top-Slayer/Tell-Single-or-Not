from threading import Thread

import cv2
import os
import time
import pygame
import random
from gtts import gTTS

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

# detectFace function
# ------------------------------------------------------
def detectFace():
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

        Thread(target=play_sound).start()
        cv2.imwrite("check_Picture.png", frame)

        if total > 0:
            return True
        else:
            return False
# ------------------------------------------------------


# Play sound function
# ------------------------------------------------------
def play_sound():
    exec(open("Playsound.py").read())
# ------------------------------------------------------


print("Processing...")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    # main processing
    # print("Right: True") if detectFace() == True else print("Left: False")
    detectFace()

    # display camera
    cv2.imshow("Detect people", frame)

    # wait for pressed q letter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Ending...")
        break

cap.release()
cv2.destroyAllWindows()
