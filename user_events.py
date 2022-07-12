import pygame
from pygame.locals import *

pygame.init()

print_message = pygame.USEREVENT
pygame.time.set_timer(print_message, 3000)

while True:
    for event in pygame.event.get():
        if event.type == print_message:
            print("Hello, World!")
