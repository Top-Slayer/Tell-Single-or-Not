from Detect_people import detectFace
import pygame

print(detectFace())
pygame.mixer.init()
my_sound = pygame.mixer.Sound('output.wav')
my_sound.play()
pygame.time.wait(int(my_sound.get_length() * 1000))