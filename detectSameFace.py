import cv2
import os
import time

start_time = time.time()

chcek_image = cv2.imread("check_Picture.png")

folder = [r"types\คนเจ้าชู้", "types\คนรักเดียวใจเดียว", "types\คนโสด"]
i = int(0)
while i < len(folder):
    for filename in os.listdir(folder[i]):
        find_image = cv2.imread(os.path.join(folder[i], filename))

        gray_image1 = cv2.cvtColor(chcek_image, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(find_image, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        faces1 = face_cascade.detectMultiScale(
            gray_image1, scaleFactor=1.1, minNeighbors=5
        )
        faces2 = face_cascade.detectMultiScale(
            gray_image2, scaleFactor=1.1, minNeighbors=5
        )

        cv2.imshow("checking-picture", chcek_image)
        cv2.imshow("founded-picture", find_image)

        if len(faces1) == 1 and len(faces2) == 1:
            x1, y1, w1, h1 = faces1[0]
            x2, y2, w2, h2 = faces2[0]

            face1 = gray_image1[y1 : y1 + h1, x1 : x1 + w1]
            face2 = gray_image2[y2 : y2 + h2, x2 : x2 + w2]

            avg_intensity1 = face1.mean()
            avg_intensity2 = face2.mean()

            threshold = 20

            if abs(avg_intensity1 - avg_intensity2) < threshold:
                print(f"--> Faces match: [ {folder[i][6:]} ]")

                while True:
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
            else:
                print("--> Faces do not match.")
        else:
            print("--> Number of faces detected is not 1 in one or both images.")
    i += 1

end_time = time.time()
elapsed_time = end_time - start_time
print(f"--> Elapsed time: {elapsed_time:.2f} seconds")
