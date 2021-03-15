## @file Menu.py
#  @author Ardhendu, Dylan, Thaneegan
#  @brief This class represents the Menu for the game. The menu contains the functionality for Tutorial and New Game. 
#  @date March 15th 2021

import pygame
from board import *
from tkinter import *
from tkinter import messagebox

class menu:
    
    ## @brief Class to display the message box (utilizing Tinker library) for the Tutorial once called upon.
    def tutorial(self):
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('Tutorial', 'CHECKERS TUTORIAL: \n - The aim of checkers is to capture all the pieces of your opponent! \n - You control the red pieces, while the computer controls the white pieces. \n - Click on a red piece to select the piece, then click on a diagonal space to move the piece. \n - Upon completing your turn, wait for the computer (white piece) to make its move. \n - Once the computer has made their move, you can now make your move. \n - Please learn more about Checkers Rules via this link: https://www.ducksters.com/games/checkers_rules.php')
    
    ## @brief Resets the game by reseting the pieces back to original spots.
    #  @param board The game board to be reset
    #  @param width The width of the game board
    #  @param height The height of the game baord
    #  @param firstPlayer The ID of the player
    def newgame(self, board, width, height, firstPlayer):
        board.resetBoard(width, height, firstPlayer)