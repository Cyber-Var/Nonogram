import pygame
import logging
import sys
from pygame.locals import *

pygame.init()


class Grid:

    logging.basicConfig()
    logging.root.setLevel(logging.NOTSET)
    logger = logging.getLogger("Grid.class")

    def __init__(self, width, height):
        self.logger.info("Grid class created.")
        self.width = width
        self.height = height
        self.draw_grid()

    def draw_grid(self):



