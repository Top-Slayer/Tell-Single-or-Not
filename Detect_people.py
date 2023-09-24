import cv2
from playsound import playsound
from gtts import gTTS

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

text = "hello"

# all function for processing
def detectFace(text):
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 106, 42), 2)
        cv2.circle(frame, (w/2, h/2), 1, (0,255,0), 2)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (47, 173, 255), 2)


myobj = gTTS(text="Hello how are you", lang='th', slow=False)
myobj.save("output.mp3")

audio_file_path = r"C:\Education about Programming - TOP\Python\Detect_Single_or_NotSingle_AI\Tell-Single-or-Not\output.mp3"
# playsound(audio_file_path)

print("Processing...");

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # main processing
    detectFace(text)

    # display camera
    cv2.imshow("Detect people", frame)
    # wait for pressed q letter 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Ending...")
        break

cap.release()
cv2.destroyAllWindows()