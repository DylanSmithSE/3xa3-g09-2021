import pygame
from tkinter import *
from tkinter import messagebox

class tutorial:
    def __init__(self):
        self.screen = None
        self.tutorial_img = pygame.image.load('./img/white_man.png')
        self.message = "Displaying tutorial for Checkers game."
        print(self.message)
        self.make_display()

    def make_display(self):
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('Tutorial', 
        'CHECKERS TUTORIAL: \n - The aim of checkers is to capture all the pieces of your opponent! \n - You control the red pieces, while the computer controls the white pieces. \n - Click on a red piece to select the piece, then click on a diagonal space to move the piece. \n - Upon completing your turn, wait for the computer (white piece) to make its move. \n - Once the computer has made their move, you can now make your move. \n - Please learn more about Checkers Rules via this link: https://www.ducksters.com/games/checkers_rules.php')