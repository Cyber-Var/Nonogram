import pygame
from pygame.locals import *
import sys

from GameField_window import Field
from HorizontalNumbers_window import HorizontalNumbers
from ScoreBoard_window import ScoreBoard
from VerticalNumbers_window import VerticalNumbers


arr = [[1, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 1, 1],
       [0, 1, 0, 1, 1, 0],
       [0, 1, 1, 1, 0, 0],
       [0, 1, 1, 1, 1, 0],
       [0, 0, 0, 1, 0, 0]]


pygame.init()

surface = pygame.display.set_mode((605, 700))
surface.fill((255, 255, 255))

field = Field(6)
field.set_squares(arr)
horizontal = HorizontalNumbers(6, [])
vertical = VerticalNumbers(6, [])
score = ScoreBoard(6)

smallfont = pygame.font.SysFont('Corbel', 25)
text = smallfont.render('Exit', True, (200, 200, 200))
pygame.draw.rect(surface, (100, 100, 100), [250, 635, 100, 30])
surface.blit(text, (280, 642))


def exit_game():
    pygame.quit()
    sys.exit()


while 1:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        if event.type == MOUSEBUTTONDOWN:
            if 250 <= mouse[0] <= 350 and 635 <= mouse[1] <= 665:
                exit_game()

    surface.blit(score.get_surface(), (0, 0))
    surface.blit(vertical.get_surface(), (0, 100))
    surface.blit(horizontal.get_surface(), (100, 0))
    surface.blit(field.get_surface(), (100, 100))

    pygame.display.update()
