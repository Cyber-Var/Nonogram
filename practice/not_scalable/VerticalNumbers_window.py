import pygame


'''class VerticalNumbers:

    pygame.init()

    surface = pygame.Surface((100, 500))
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (100, 100, 100)
    COLOR_BLACK = (0, 0, 0)

    rows = []

    def __init__(self, difficulty, arr):
        self.difficulty = difficulty
        for n in range(self.difficulty):
            self.rows.append([])
        self.arr = arr
        self.initialise()
        self.set_rows()
        self.draw()

    def initialise(self):
        self.surface.set_alpha(150)
        self.surface.fill(self.COLOR_WHITE)

    def draw(self):
        font = pygame.font.SysFont('arial', 25)

        wh = 500 / self.difficulty
        for i in range(self.difficulty):
            pygame.draw.line(self.surface, self.COLOR_GRAY, (0, i * wh), (100, i * wh), 1)

            text = " "
            for num in self.rows[i]:
                text += str(num) + " "
            numbers = font.render(text, True, self.COLOR_BLACK)
            self.surface.blit(numbers, (10, i*wh + wh/2 - 10))

        pygame.draw.line(self.surface, self.COLOR_GRAY, (0, 499), (100, 499), 1)

    def get_surface(self):
        return self.surface

    def set_rows(self):
        summ = 0
        for i in range(self.difficulty):
            for j in range(self.difficulty):
                if self.arr[i][j] == 1:
                    summ += 1
                if (summ != 0 and self.arr[i][j] == 0) or (self.arr[i][j] == 1 and j == self.difficulty - 1):
                    self.rows[i].append(summ)
                    summ = 0'''
