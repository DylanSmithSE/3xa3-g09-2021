from board2 import *
from constants import *

class Game():
    def __init__(self):
        self.board = Board()
        self.selected = None
        self.turn = "RED"
        self.validMoves = {}


    def select(self, square):
        row = square[0]
        col = square[1]

        if self.selected == None:
            if self.board.boardState[row][col] != 0:
                print("Selecting")
                self.selected = self.board.boardState[row][col]
                self.validMoves = self.board.getValidMoves(self.selected)
            else:
                pass
        else:
            if (row,col) in self.validMoves.keys():
                print("moving")
                print("Skipping: " + str(self.validMoves[(row,col)]))
                self.board.move(self.selected,row,col,self.validMoves[(row,col)])
                self.selected = None
                self.validMoves = {}
            else:
                print("Can't move there")
                self.selected = None
                self.validMoves = {}



    def changeTurn(self):
        if self.turn == "RED":
            self.turn == "WHITE"
        else:
            self.turn == "RED"
