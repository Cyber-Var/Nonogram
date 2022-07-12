import logging
import pygame
import sys
from pygame.locals import *

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

class Menu:

    pygame.init()

    def __init__(self, display):
        logging.info("Menu scene created.")
        self.display = display
        self.draw_buttons()

    def draw_buttons(self):



