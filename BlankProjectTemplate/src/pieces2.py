## @file pieces.py
#  @author Ardhendu, Dylan, Thaneegan
#  @brief Class to represent a checkers piece.
#  @date March 15th 2021

import pygame
class piece:

    ## @brief Class to represent a checkers piece.
    #  @param row The row location of the piece.
    #  @param col The column location of the piece.
    #  @param color The color of the piece.
    def __init__(self, row, col, color, direction):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.direction = direction

    ## @brief Represent a checkers king piece.
    def makeKing(self):
        self.king = True

    ## @brief Move the checkers piece to the desired location.
    #  @param row The row location of the move.
    #  @param col The column location of the move.
    def move(self, row, col):
        self.row = row
        self.col = col