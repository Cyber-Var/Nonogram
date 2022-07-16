

class Square:

    def __init__(self, x, y):
        self.filled = False
        self.x = x
        self.y = y

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = True

    def unfill(self):
        self.filled = False
