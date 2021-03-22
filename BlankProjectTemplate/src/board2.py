## @file board.py
#  @author Carson Wilcox, Ardhendu, Dylan, Thaneegan
#  @brief Class to represent the board and handle the state of the board of the checkers game.
#  @date March 16th 2021

from pieces2 import *
from constants import *

class Board():
    def __init__(self):
        self.turn = "RED"
        self.gameWon = -1
        self.boardState = [[0] * ROWS for x in range(COLS)]
        self.red_pieces = []
        self.white_pieces = []
        self.setBoard()


    def resetBoard(self):
        self.turn = "RED"

        self.updateBoard()
        print("new game")
        # Tk().wm_withdraw() #to hide the main window
        # messagebox.showinfo('Starting new game...','New game selected, enjoy!')

    def setBoard(self):
        x = 0
        for row in SETUP:
            y = 0
            for col in row:
                if col == "RED":
                    p = piece(x,y,"RED",-1)
                    self.boardState[x][y] = p
                    self.red_pieces.append(p)
                elif col == "WHITE":
                    p = piece(x,y,"WHITE",-1)
                    self.boardState[x][y] = p
                    self.white_pieces.append(p)
                else:
                    pass
                y = y + 1
            x = x + 1
        print(self.red_pieces)

    #replace piece with 0 and then moves the piece to the new location
    def move(self, piece, toRow, toCol):
        self.boardState[piece.row][piece.col] = 0
        self.boardState[toRow][toCol] = piece
        piece.move(toRow,toCol)

    #replaces piece with 0 in boardstate
    def remove(self, piece):
        self.boardState[piece.row][piece.col] = 0
        self.red_pieces.remove(piece)
        self.white_pieces.remove(piece)

    def getValidMoves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        colour = piece.color
        self.checkUpLeft(row,col,colour,False,[],moves)
        self.checkUpRight(row,col,colour,False,[],moves)
        return moves


    def checkUpLeft(self, row, col, colour, haveSkipped, captures,moves):
        skipped = []
        for tup in captures:
            skipped.append(tup)
        if row-1>=0 and col-1>=0:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row-1][col-1] == 0:
                    if not (row-1,col-1) in moves:
                        moves[(row-1,col-1)] = []
                elif self.boardState[row-1][col-1].color != colour:
                    self.checkUpLeftSkip(row,col,colour,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row-1][col-1] == 0:
                    pass
                elif self.boardState[row-1][col-1].color != colour:
                    self.checkUpLeftSkip(row,col,colour,skipped,moves)
                else:
                    pass

    def checkUpLeftSkip(self,row,col,colour,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if row-2>=0 and col-2>=0:
            if self.boardState[row-2][col-2] == 0:
                skipped.append((row-1,col-1))
                if not (row-2,col-2) in moves:
                    moves[(row-2,col-2)] = skipped
                self.checkUpLeft(row-2,col-2,colour,True,skipped,moves)
                self.checkUpRight(row-2,col-2,colour,True,skipped,moves)
            else:
                pass


    def checkUpRight(self, row, col, colour, haveSkipped, captures,moves):
        skipped = []
        for tup in captures:
            skipped.append(tup)
        if row-1>=0 and col+1<8:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row-1][col+1] == 0:
                    if not (row-1,col+1) in moves:
                        moves[(row-1,col+1)] = []
                elif self.boardState[row-1][col+1].color != colour:
                    self.checkUpRightSkip(row,col,colour,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row-1][col+1] == 0:
                    pass
                elif self.boardState[row-1][col+1].color != colour:
                    self.checkUpRightSkip(row,col,colour,skipped,moves)
                else:
                    pass

    def checkUpRightSkip(self,row,col,colour,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if row-2>=0 and col+2<8:
            if self.boardState[row-2][col+2] == 0:
                skipped.append((row-1,col+1))
                if not (row-2,col+2) in moves:
                    moves[(row-2,col+2)] = skipped
                self.checkUpRight(row-2,col+2,colour,True,skipped,moves)
                self.checkUpLeft(row-2,col+2,colour,True,skipped,moves)
            else:
                pass



dic = {(1,1):2,(1,3):4,(2,2):4,(2,3):5}
if not (1,1) in dic:
    dic[(1,1)] = 6
print(dic)
