import pygame
import sys
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((300, 300))

while 1:
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_a] and pressed_keys[K_b]:
        print("Keys A and B have been pressed")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Key A has been pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("Key A has been released")
