## @file board.py
#  @author Ardhendu, Dylan, Thaneegan
#  @brief Class to represent the board of the checkers game.
#  @date March 16th 2021

# coding: utf-8
# Game board. It needs a height and a width in order
# to be instantiated
from tkinter import *
from tkinter import messagebox

class board(object):

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

    ## @brief Iterates through the white pieces array to generate moves for white pieces.
    def iterWhiteMoves(self):
        """
            Main generator for white moves
        """
        for piece in self.whitelist:
            for move in self.iterWhitePiece(piece):
                yield move

    ## @brief Iterates through the black pieces array to generate moves for black pieces.
    def iterBlackMoves(self):
        """
            Main Generator for black moves
        """
        for piece in self.blacklist:
            for move in self.iterBlackPiece(piece):
                yield move

    ## @brief Checks for possible moves for the selected piece
    #  @param piece The piece to be moved
    #  @return Returns the location of the possible move of the selected piece
    def iterWhitePiece(self, piece):
        """
            Generates possible moves for a white piece
        """
        # return self.iterBoth(piece, ((-1,-1),(1,-1)))
        return self.iterBoth(piece, ((-1,1),(-1,-1)))

    ## @brief Checks for possible moves for the selected piece
    #  @param piece The piece to be moved
    #  @return Returns the location of the valid move of the selected piece
    def iterBlackPiece(self, piece):
        """
            Generates possible moves for a black piece
        """
        # return self.iterBoth(piece, ((-1,1),(1,1)))
        return self.iterBoth(piece, ((1,-1),(1,1)))

    ## @brief Checks for possible moves for the selected piece
    #  @param piece The piece to be moved
    #  @param moves The set of possible moves
    #  @return Returns the location of the valid moves of the selected piece
    def iterBoth(self, piece, moves):
        """
            Handles the actual generation of moves for either black or white pieces
        """
        print('moves ae piece ', piece, moves)
        for move in moves:
            # Regular Move
            print('moce s ', move)
            targetx = piece[0] + move[0]
            targety = piece[1] + move[1]
            # print(f'targetx is {targetx} and targety is {targety}' )
            # If the move is out of bounds don't move
            if targetx < 0 or targetx >= self.width or targety < 0 or targety >= self.height:
                continue
            target = (targetx, targety)
            print('target is ', target)
            # Check that there is nothing in the way of moving to the target
            black = target in self.blacklist
            white = target in self.whitelist
            if not black and not white:
                yield (piece, target, self.NOTDONE)
            # There was something in the way, can we jump it?
            else:
                # It has to be of the opposing color to jump
                if self.turn == self.RED and black:
                    continue
                elif self.turn == self.WHITE and white:
                    continue
                # Jump proceeds by adding the same movement in order to jump over the opposing
                # piece on the checkerboard
                jumpx = target[0] + move[0]
                jumpy = target[1] + move[1]
                # If the jump is going to be out of bounds don't do it.
                if jumpx < 0 or jumpx >= self.width or jumpy < 0 or jumpy >= self.height:
                    continue
                jump = (jumpx, jumpy)
                # Check that there is nothing in the jumpzone
                black = jump in self.blacklist
                white = jump in self.whitelist
                if not black and not white:
                    yield (piece, jump, self.turn)

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
            # print('piece is  ', piece)
            self.boardState[piece[0]][piece[1]] = 'WHITE'
        for piece in self.whitelist:
            self.boardState[piece[0]][piece[1]] = 'BLACK'

    ## @brief Moves a black piece, calls the updateboard method, determines if black piece player has won or loss (sets the turn to white after)
    #  @param moveFrom The location of the piece to be moved
    #  @param moveTo The location of where the piece has to be moved to
    def moveSilentBlack(self, moveFrom, moveTo, winLoss):
        """
            Move black piece without printing
        """
        if moveTo[0] < 0 or moveTo[0] >= self.width or moveTo[1] < 0 or moveTo[1] >= self.height:
            raise Exception("That would move black piece", moveFrom, "out of bounds")
        black = moveTo in self.blacklist
        white = moveTo in self.whitelist
        if( not(black or white) and ( (moveTo == (moveFrom[0]-1,moveFrom[1]+1)) or  (moveTo == (moveFrom[0]-1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]+1)) )):
            self.blacklist[self.blacklist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.WHITE
            self.gameWon = winLoss
        else:
            raise Exception

    ## @brief Moves a white piece, calls the updateboard method, determines if white piece player has won or loss (sets the turn to black after)
    #  @param moveFrom The location of the piece to be moved
    #  @param moveTo The location of where the piece has to be moved to
    def moveSilentWhite(self, moveFrom, moveTo, winLoss):
        """
            Move white piece without printing
        """
        if moveTo[0] < 0 or moveTo[0] >= self.width or moveTo[1] < 0 or moveTo[1] >= self.height:
            raise Exception("That would move white piece", moveFrom, "out of bounds")

        black = moveTo in self.blacklist
        white = moveTo in self.whitelist
        print('move pair is ', (moveFrom, moveTo))
        if( (moveTo == (moveFrom[0]-1,moveFrom[1]+1)) or  (moveTo == (moveFrom[0]-1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]+1)) ):
            print('Trueeee')

        if( not(black or white) and ( (moveTo == (moveFrom[0]-1,moveFrom[1]+1)) or  (moveTo == (moveFrom[0]-1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]+1)) )):
            self.whitelist[self.whitelist.index(moveFrom)] = moveTo
            self.updateBoard()
            self.turn = self.RED
            self.gameWon = winLoss
        else:
            raise Exception

    ## @brief Moves a black piece, calls the updateboard method, determines if black piece player has won or loss (sets the turn to white after)
    #  @param moveFrom The location of the piece to be moved
    #  @param moveTo The location of where the piece has to be moved to
    def moveBlack(self, moveFrom, moveTo, winLoss):
        """
            Move a black piece from one spot to another. \n winLoss is passed as either 0(white)
            or 1(black) if the move is a jump
        """
        self.moveSilentBlack(moveFrom, moveTo, winLoss)

    ## @brief Moves a white piece, calls the updateboard method, determines if white piece player has won or loss (sets the turn to black after)
    #  @param moveFrom The location of the piece to be moved
    #  @param moveTo The location of where the piece has to be moved to
    def moveWhite(self, moveFrom, moveTo, winLoss):
        """
            Move a white piece from one spot to another. \n winLoss is passed as either 0(white)
            or 1(black) if the move is a jump
        """
        self.moveSilentWhite(moveFrom, moveTo, winLoss)

    #Prints the game board to stdout
    def printBoard(self):
        """
            Prints the game board to stdout
        """
        print(str(self.boardState))
