from board2 import *
from constants import *
from minmax2 import *

class Game():
    def __init__(self,gui):
        self.board = Board()
        self.gui = gui
        self.selected = None
        self.validMoves = {}
        self.winner = ""

    def resetGame(self):
        self.gui.reset_validMoves()
        self.gui.reset_selected()
        self.board.resetBoard(self.gui)
        self.gui.selected = None
        self.gui.validMoves = {}
        self.selected = None
        self.validMoves = {}
        self.winner = ""

    def select(self, square):
        row = square[0]
        col = square[1]

        if self.selected == None:
            if self.board.boardState[row][col] != 0:
                if self.board.boardState[row][col].color == self.board.turn:
                    self.selected = self.board.boardState[row][col]
                    self.validMoves = self.board.getValidMoves(self.selected)
                    if self.gui.single_player == 1:
                        if self.board.turn == self.gui.color_selected:
                            self.gui.pass_selected(self.selected)
                            self.gui.pass_validMoves(self.validMoves)
                    else:
                        self.gui.pass_selected(self.selected)
                        self.gui.pass_validMoves(self.validMoves)
                else:
                    print("not your turn")
            else:
                pass
        else:
            if (row,col) in self.validMoves.keys():
                self.board.move(self.selected,(row,col),self.validMoves[(row,col)])
                self.selected = None
                self.validMoves = {}
                self.gui.reset_validMoves()
                self.gui.reset_selected()

                if self.gui.single_player == 1:
                    self.board = minmax(self.board,True,3)[1]

                if(self.board.checkGameEnd()):
                    print("GAME OVER")
            else:
                if self.board.boardState[row][col] != 0:
                    print('HEY')
                    print('1 Selected: ', self.selected.row, self.selected.col)
                    if self.board.boardState[row][col].color == self.board.turn:
                        print('HEY AGAIN')
                        self.selected = None
                        self.validMoves = {}
                        self.gui.reset_validMoves()
                        self.gui.reset_selected()
                        self.selected = self.board.boardState[row][col]
                        self.validMoves = self.board.getValidMoves(self.selected)
                        print('2 Selected: ', self.selected.row, self.selected.col)
                        if self.gui.single_player == 1:
                            if self.board.turn == self.gui.color_selected:
                                self.gui.pass_selected(self.selected)
                                self.gui.pass_validMoves(self.validMoves)
                        else:
                            self.gui.pass_selected(self.selected)
                            self.gui.pass_validMoves(self.validMoves)
                else:
                    print("Can't move there")
                    self.selected = None
                    self.validMoves = {}
                    self.gui.reset_validMoves()
                    self.gui.reset_selected()
