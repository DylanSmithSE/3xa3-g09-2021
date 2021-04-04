## @file game.py
## @brief Following module handles the logic of the game.
## @details The logic of the game includes initializing the board and gui and 
#           handling the turns of users/AI.
#  @author Ardhendu, Dylan, Thaneegan
#  @date April 4th 2021

from board2 import *
from constants import *
from minmax2 import *
from menu2 import *
import time

class Game():
    ## @brief The init method for Game loads the board and gui to start a new game
    #  @param gui The gui class is used to handle the display/graphics
    def __init__(self,gui):
        self.board = Board(gui)
        self.gui = gui
        self.reset_game()

    ## @brief reset_game Initalizes the game to a new game and resets all
    #         current variables to initial state
    def reset_game(self):
        self.gui.reset_validMoves()
        self.gui.reset_selected()
        self.gui.start_game = 1
        self.gui.selected = None
        self.gui.validMoves = {}
        self.selected = None
        self.validMoves = {}
        self.winner = ""

    ## @brief start_AI kickstarts the game if it is AI's turn first
    #  @details If the game mode is 1-Player and user's color is white, 
    #           then AI must move first. start_AI is called for that purpose.
    def start_AI(self):
        #time.sleep(1)
        self.board = minmax(self.board,True,3)[1]

    ## @brief select method handles the turns of the user(s)/AI
    #  @details Handles/Requests the moves of the user(s) and AI based on whos turn it is
    #           and based on the game-mode+color selected. Also checks if game has ended yet
    #           or not.
    #  @param square The current square that is selected on the board
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
