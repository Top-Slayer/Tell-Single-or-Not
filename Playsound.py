import pygame
import random
import cv2
from gtts import gTTS
from datetime import datetime

random_text = ["คนรักเดียวใจเดียว", "คนเจ้าชู้", "คนโสด"]
rand_num = random.randrange(0, len(random_text))


pygame.mixer.init()

print(rand_num)

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

if rand_num == 0:
    image_path = f"types/คนรักเดียวใจเดียว/{formatted_time_str}.png"

elif rand_num == 1:
    image_path = f"types/คนเจ้าชู้/{formatted_time_str}.png"

elif rand_num == 2:
    image_path = f"types/คนโสด/{formatted_time_str}.png"

print(image_path)

try:
    cv2.imwrite(image_path, check_pic)
    print("Image saved successfully!")
except Exception as e:
    print(f"Error saving image: {e}")
