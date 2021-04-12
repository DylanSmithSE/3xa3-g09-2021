## @file piece.py
#  @brief Class to represent a checkers piece.
#  @author Ardhendu, Dylan, Thaneegan
#  @date April 4th 2021

import pygame
class piece:

    ## @brief Class to represent a checkers piece.
    #  @param row The row location of the piece.
    #  @param col The column location of the piece.
    #  @param color The color of the piece.
    #  @param direction The direction of the piece.
    #  @param king Boolean whether the piece is a king or not
    def __init__(self, row, col, color, direction, king = False):
        self.row = row
        self.col = col
        self.color = color
        self.king = king
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
