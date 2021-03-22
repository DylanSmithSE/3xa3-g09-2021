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
                    p = piece(x,y,"WHITE",1)
                    self.boardState[x][y] = p
                    self.white_pieces.append(p)
                else:
                    pass
                y = y + 1
            x = x + 1
        self.boardState[0][1].makeKing()
        self.boardState[7][0].makeKing()

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
        direction = piece.direction
        if not piece.king:
            self.checkLeft(row,col,colour,direction,False,False,[],moves)
            self.checkRight(row,col,colour,direction,False,False,[],moves)
        else:
            self.checkLeft(row,col,colour,-1*direction,True,False,[],moves)
            self.checkRight(row,col,colour,-1*direction,True,False,[],moves)
            self.checkLeft(row,col,colour,direction,True,False,[],moves)
            self.checkRight(row,col,colour,direction,True,False,[],moves)
        return moves


    def checkLeft(self,row,col,colour,direction,isKing,haveSkipped,captures,moves):
        skipped = []
        #need this or else all entries of moves will have the same skipped list
        for tup in captures:
            skipped.append(tup)
        if row+direction>=0 and row+direction<8 and col-1>=0:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row+direction][col-1] == 0:
                    if not (row+direction,col-1) in moves:
                        moves[(row+direction,col-1)] = []
                elif self.boardState[row+direction][col-1].color != colour:
                    self.checkLeftSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row+direction][col-1] == 0:
                    pass
                elif self.boardState[row+direction][col-1].color != colour:
                    self.checkLeftSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass

    def checkLeftSkip(self,row,col,colour,direction,isKing,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if (row+(2*direction))>=0 and (row+(2*direction)<8) and col-2>=0:
            #if we can skip the piece we do and then check if we can continue
            if self.boardState[row+(2*direction)][col-2] == 0:
                skipped.append((row+direction,col-1))
                if not (row+(2*direction),col-2) in moves:
                    moves[(row+(2*direction),col-2)] = skipped
                if not isKing:
                    self.checkLeft(row+(2*direction),col-2,colour,direction,False,True,skipped,moves)
                    self.checkRight(row+(2*direction),col-2,colour,direction,False,True,skipped,moves)
                else:
                    self.checkLeft(row+(2*direction),col-2,colour,direction,True,True,skipped,moves)
                    self.checkRight(row+(2*direction),col-2,colour,direction,True,True,skipped,moves)
                    self.checkLeft(row+(-2*direction),col-2,colour,-1*direction,True,True,skipped,moves)
                    self.checkRight(row+(-2*direction),col-2,colour,-1*direction,True,True,skipped,moves)
            else:
                pass


    def checkRight(self,row,col,colour,direction,isKing,haveSkipped,captures,moves):
        skipped = []
        for tup in captures:
            skipped.append(tup)
        if row+direction>=0 and row+direction<8 and col+1<8:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row+direction][col+1] == 0:
                    if not (row+direction,col+1) in moves:
                        moves[(row+direction,col+1)] = []
                elif self.boardState[row+direction][col+1].color != colour:
                    self.checkRightSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row+direction][col+1] == 0:
                    pass
                elif self.boardState[row+direction][col+1].color != colour:
                    self.checkRightSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass

    def checkRightSkip(self,row,col,colour,direction,isKing,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if (row+(2*direction))>=0 and (row+(2*direction)<8) and col+2<8:
            if self.boardState[row+(2*direction)][col+2] == 0:
                skipped.append((row+direction,col+1))
                if not (row+(2*direction),col+2) in moves:
                    moves[(row+(2*direction),col+2)] = skipped
                if not isKing:
                    self.checkRight(row+(2*direction),col+2,colour,direction,False,True,skipped,moves)
                    self.checkLeft(row+(2*direction),col+2,colour,direction,False,True,skipped,moves)
                else:
                    self.checkRight(row+(2*direction),col+2,colour,direction,True,True,skipped,moves)
                    self.checkLeft(row+(2*direction),col+2,colour,direction,True,True,skipped,moves)
                    self.checkRight(row+(-2*direction),col+2,colour,-1*direction,True,True,skipped,moves)
                    self.checkLeft(row+(-2*direction),col+2,colour,-1*direction,True,True,skipped,moves)
            else:
                pass



dic = {(1,1):2,(1,3):[(1,2),(2,3)],(2,2):4,(2,3):5}
a = dic.get((1,3))
print(a)
