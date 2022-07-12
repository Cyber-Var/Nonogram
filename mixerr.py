import pygame
from tkinter import *


def play():
    pygame.mixer.music.load('iaa.wav')
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def sound():
    pygame.mixer.Sound.play(sound_effect)


pygame.init()
sound_effect = pygame.mixer.Sound('crash.wav')


root = Tk()
root.geometry('180x200')

myFrame = Frame(root)
myFrame.pack()

myLabel = Label(myFrame, text="Pygame Mixer")
myLabel.pack()

button1 = Button(myFrame, text="Play", command=play, width=15)
button1.pack(pady=5)
button2 = Button(myFrame, text="Sound", command=sound, width=15)
button2.pack(pady=5)
button3 = Button(myFrame, text="Unpause", command=unpause, width=15)
button3.pack(pady=5)
button4 = Button(myFrame, text="Pause", command=pause, width=15)
button4.pack(pady=5)

root.mainloop()
