## @file Menu.py
#  @author Ardhendu, Dylan, Thaneegan
#  @brief This class represents the Menu for the game. The menu contains the functionality for Tutorial and New Game.
#  @date March 15th 2021

import pygame
from board2 import *
from tkinter import *
from tkinter import messagebox
class menu:

    ## @brief Class to display the message box (utilizing Tinker library) for the Tutorial once called upon.
    def tutorial(self, game):
        if game.gui.tutorial:
            game.gui.tutorial = False
        else:
            game.gui.tutorial = True

    ## @brief Resets the game by reseting the pieces back to original spots.
    #  @param board The game board to be reset
    #  @param width The width of the game board
    #  @param height The height of the game baord
    #  @param firstPlayer The ID of the player
    def new_game(self, game):
        game.resetGame()
        game.gui.start_game = 1
        
    
    def start_game(self, game, width, height, firstPlayer):
        game.gui.new_game = 3
        while game.gui.new_game > 0:
            game.gui.display_newgame()
            game.gui.new_game = game.gui.new_game - 1
        game.gui.start_game = 0

    def select_game_mode(self, game, mode):
        if mode == 1:
            game.gui.single_player = 1
        else:
            game.gui.single_player = 0

    def select_color(self, game, color):
        if color == 'white':
            game.gui.color_selected = "WHITE"
            game.board.turn = game.gui.color_selected
        else:
            game.gui.color_selected = "RED"
            game.board.turn = game.gui.color_selected