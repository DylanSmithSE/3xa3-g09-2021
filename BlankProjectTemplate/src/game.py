from board2 import *
from constants import *

class Game():
    def __init__(self):
        self.board = Board()
        self.selected = None
        self.turn = "RED"
        self.validMoves = {}
        self.winner = ""


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
                print(self.turn)
                self.checkGameEnd()
                self.changeTurn()
                print(self.turn)
            else:
                print("Can't move there")
                self.selected = None
                self.validMoves = {}



    def changeTurn(self):
        if self.turn == "RED":
            self.turn = "WHITE"
        else:
            self.turn = "RED"

    def checkGameEnd(self):
        moves = {}
        if self.turn == "RED":
            for piece in self.board.red_pieces:
                moves.update(self.board.getValidMoves(piece))
                #if red has any valid moves then white has not won
                if moves:
                    break
            #if moves is empty then white wins
            if not moves:
                self.winner = "WHITE"
                print("white Wins!")
        else:
            for piece in self.board.white_pieces:
                moves.update(self.board.getValidMoves(piece))
                #if white has any valid moves then red has not won
                if moves:
                    break
            #if moves is empty then red wins
            if not moves:
                self.winner = "RED"
                print("Red Wins!")
