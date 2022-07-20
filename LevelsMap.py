import pygame
from pygame.locals import *
import sys

from Game import Game


class Levels:
    pygame.init()
    surface = pygame.display.set_mode((605, 700), pygame.SRCALPHA)

    bg_image = pygame.image.load('resources/levels_map_background.jpeg')
    bg_image = pygame.transform.scale(bg_image, (605, 700))

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.loop()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def loop(self):
        while 1:
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit_game()
                if event.type == MOUSEBUTTONDOWN:
                    Game(self.difficulty)
                    if 80 <= mouse[0] <= 150 and 50 <= mouse[1] <= 140:
                        print("tunnel")
                    elif 530 <= mouse[0] <= 580 and 120 <= mouse[1] <= 170:
                        print("rocks")
                    elif 5 <= mouse[0] <= 85 and 300 <= mouse[1] <= 415:
                        print("house")
                    elif 185 <= mouse[0] <= 270 and 200 <= mouse[1] <= 310:
                        print("tree")
                    elif 440 <= mouse[0] <= 495 and 315 <= mouse[1] <= 385:
                        print("crystal")
                    elif 230 <= mouse[0] <= 290 and 405 <= mouse[1] <= 525:
                        print("statue")
                    elif 525 <= mouse[0] <= 605 and 440 <= mouse[1] <= 540:
                        print("fisher")
                    elif 375 <= mouse[0] <= 465 and 590 <= mouse[1] <= 665:
                        print("car")

            self.surface.blit(self.bg_image, (0, 0))
            # tunnel:
            pygame.draw.rect(self.surface, (255, 255, 255), [80, 50, 70, 90], 1)
            # rocks:
            pygame.draw.rect(self.surface, (255, 255, 255), [530, 120, 50, 50], 1)
            # house:
            pygame.draw.rect(self.surface, (255, 255, 255), [5, 300, 80, 115], 1)
            # tree:
            pygame.draw.rect(self.surface, (255, 255, 255), [185, 200, 85, 110], 1)
            # crystal:
            pygame.draw.rect(self.surface, (255, 255, 255), [440, 315, 55, 70], 1)
            # statue:
            pygame.draw.rect(self.surface, (255, 255, 255), [230, 405, 60, 120], 1)
            # fisher
            pygame.draw.rect(self.surface, (255, 255, 255), [525, 440, 80, 100], 1)
            # car:
            pygame.draw.rect(self.surface, (255, 255, 255), [375, 590, 90, 75], 1)

            pygame.display.update()
