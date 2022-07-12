import pygame
import sys
import time
from pygame.locals import *

pygame.init()

pygame.mixer.music.load('crash.wav')
pygame.mixer.music.play()

pygame.mixer.music.pause()
time.sleep(3)
pygame.mixer.music.unpause()

pygame.mixer.music.queue('fall.wav')
pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == SONG_END:
            print("end")
