import pygame


''' pygame.init()
surface = pygame.display.set_mode((640, 480))

COLOR_TEXT = (250, 250, 250)
COLOR_RECT = (100, 100, 100)
small_font = pygame.font.SysFont('Corbel', 25)


class Entry:

    def __init__(self, x, y, width, height, insert=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = small_font.render(insert, True, COLOR_TEXT)

        self.insert = insert
        self.active = False

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.insert)
                    self.insert = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.insert = self.insert[:-1]
                else:
                    self.insert += event.unicode
                self.text = small_font.render(self.insert, True, COLOR_TEXT)

    def update(self):
        width = max(200, self.text.get_width() + 10)
        self.rect.w = width

    def draw(self, surface):
        surface.blit(self.text, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(surface, COLOR_RECT, self.rect, 2) '''


''' def main():
    clock = pygame.time.Clock()
    entry1 = Entry(100, 100, 140, 32)
    entry2 = Entry(100, 300, 140, 32)
    entries = [entry1, entry2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for entry in entries:
                entry.event(event)

        for entry in entries:
            entry.update()

        surface.fill((30, 30, 30))
        for entry in entries:
            entry.draw(surface)

        pygame.display.flip()
        clock.tick(30)

main() '''

