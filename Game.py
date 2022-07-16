from tkinter import *


class Game(Frame):

    def __init__(self):
        root.title("Nonogram")

        self.canvas = Canvas(root, width=700, height=700, bg="white")
        self.canvas.pack()

        root.mainloop()


root = Tk()
game = Game()

