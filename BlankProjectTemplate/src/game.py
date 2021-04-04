from board2 import *
from constants import *
from minmax2 import *
from menu2 import *
import time

class Game():
    def __init__(self,gui):
        self.board = Board(gui)
        self.gui = gui
        self.reset_game()

    def reset_game(self):
        self.gui.reset_validMoves()
        self.gui.reset_selected()
        self.gui.start_game = 1
        self.gui.selected = None
        self.gui.validMoves = {}
        self.selected = None
        self.validMoves = {}
        self.winner = ""

    def start_AI(self):
        #time.sleep(1)
        self.board = minmax(self.board,True,3)[1]

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
                self.gui.display_board(self.board.boardState, self.board.turn)
                time.sleep(0.1)

                if self.gui.single_player == 1 and self.gui.color_selected == "RED":
                    self.board = minmax(self.board,True,3)[1]
                elif self.gui.single_player == 1 and self.gui.color_selected == "WHITE":
                    self.board = minmax(self.board,False,3)[1]                    

                if(self.board.checkGameEnd()):
                    print("GAME OVER")
                    self.gui.display_winner(self.board.winner)
                    self.reset_game()
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
