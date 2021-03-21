## @file board.py
#  @author Carson Wilcox, Ardhendu, Dylan, Thaneegan
#  @brief Class to represent the board and handle the state of the board of the checkers game.
#  @date March 16th 2021

# coding: utf-8
# Game board. It needs a height and a width in order
# to be instantiated
from tkinter import *
from tkinter import messagebox

class board():

    RED = 1
    WHITE = 0
    NOTDONE = -1

    ## @brief Initialize the board with the default state
    #  @param height The height of the board
    #  @param width The width of the board
    #  @param firstPlayer The current turn (who goes first)
    def __init__(self, height, width, firstPlayer):
        """
            Constructs a board, right now maxDepth is statically assigned
        """
        # Set the height and width of the game board
        self.width = width
        self.height = height
        # Create two lists which will contain the pieces each player posesses
        self.blacklist = []
        self.whitelist = []
        # Set default piece positions
        self.blacklist = [(0,1), (0,3), (0,5), (0,7), (1,0), (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (2,7)]
        self.whitelist = [(5,0), (5,2), (5,4), (5,6), (6,1), (6,3), (6,5), (6,7), (7,0), (7,2), (7,4), (7,6)]
        # for i in range(width):
        #     print(i, (i, (i+1)%2), (i, height - (i%2) - 1) )
        #     self.blacklist.append((i, (i+1)%2))
        #     self.whitelist.append((i, height - (i%2) - 1))
        # boardState contains the current state of the board for printing/eval
        self.boardState = [[' '] * self.width for x in range(self.height)]
        self.updateBoard()
        self.gameWon = self.NOTDONE
        self.turn = firstPlayer
        self.maxDepth = 5

        print('black list is ', self.blacklist)
        print('white list is ', self.whitelist)

    ## @brief Used to reset the board to the original state.
    #  @param height The height of the board
    #  @param width The width of the board
    #  @param firstPlayer The current turn (who goes first)
    def resetBoard(self, height, width, firstPlayer):
        # Create two lists which will contain the pieces each player posesses
        self.blacklist = []
        self.whitelist = []
        # Set default piece positions
        # for i in range(self.width):
        #     print(i, (i, (i+1)%2), (i, self.height - (i%2) - 1) )
        #     self.blacklist.append((i, (i+1)%2))
        #     self.whitelist.append((i, self.height - (i%2) - 1))
        # boardState contains the current state of the board for printing/eval
        self.blacklist = [(0,1), (0,3), (0,5), (0,7), (1,0), (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (2,7)]
        self.whitelist = [(5,0), (5,2), (5,4), (5,6), (6,1), (6,3), (6,5), (6,7), (7,0), (7,2), (7,4), (7,6)]
        self.boardState = [[' '] * self.width for x in range(self.height)]
        self.updateBoard()
        self.gameWon = self.NOTDONE
        self.turn = firstPlayer
        self.maxDepth = 10
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('Starting new game...','New game selected, enjoy!')

    ## @brief Updates the board with the current state after a move is made by the user or AI
    def updateBoard(self):
        """
            Updates the array containing the board to reflect the current state of the pieces on the
            board
        """
        # for i in range(self.width):
        #     for j in range(self.height):
        #         self.boardState[i][j] = "Null"
        # for piece in self.blacklist:
        #     self.boardState[piece[1]][piece[0]] = 'WHITE'
        # for piece in self.whitelist:
        #     self.boardState[piece[1]][piece[0]] = 'BLACK'

        for i in range(self.height):
            for j in range(self.width):
                self.boardState[i][j] = "Null"
        for piece in self.blacklist:
            self.boardState[piece[0]][piece[1]] = 'WHITE'
        for piece in self.whitelist:
            self.boardState[piece[0]][piece[1]] = 'BLACK'

    # #Prints the game board to stdout
    # def printBoard(self):
    #     """
    #         Prints the game board to stdout
    #     """
    #     print(str(self.boardState))
