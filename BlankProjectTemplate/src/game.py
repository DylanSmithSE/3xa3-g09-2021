from board2 import *
from constants import *

class Game():
    def __init__(self,gui):
        self.board = Board()
        self.gui = gui
        self.selected = None
        self.turn = "RED"


    def select(self, square):
        row = square[0]
        col = square[1]

        if self.selected == None:
            if self.board.boardState[row][col] != 0:
                print("Selecting")
                self.selected = self.board.boardState[row][col]
                print(self.board.getValidMoves(self.selected))
            else:
                pass
        else:
            if self.board.boardState[row][col] != 0:
                print("Can't move there")
                self.selected = None
            else:
                print("moving")
                self.board.move(self.selected,row,col)
                self.selected = None



    def changeTurn(self):
        if self.turn == "RED":
            self.turn == "WHITE"
        else:
            self.turn == "RED"
