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
    def move(self, piece, move, skipped):
        self.boardState[piece.row][piece.col] = 0
        self.boardState[move[0]][move[1]] = piece
        #if a piece reaches the end of the board they become a king
        if move[0] == 7 or move[0] ==0:
            if piece.king:
                pass
            else:
                piece.makeKing()
        piece.move(move[0],move[1])
        #if there were any pieces skipped we need them removed
        for p in skipped:
            self.remove(self.boardState[p[0]][p[1]])
        self.changeTurn()

    def remove(self, piece):
        self.boardState[piece.row][piece.col] = 0
        if piece in self.red_pieces:
            self.red_pieces.remove(piece)
        if piece in self.white_pieces:
            self.white_pieces.remove(piece)

    def changeTurn(self):
        if self.turn == "RED":
            self.turn = "WHITE"
        else:
            self.turn = "RED"

    def checkGameEnd(self):
        moves = {}
        if self.turn == "RED":
            for piece in self.red_pieces:
                moves.update(self.getValidMoves(piece))
                #if red has any valid moves then white has not won
                if moves:
                    break
            #if moves is empty then white wins
            if not moves:
                self.winner = "WHITE"
                print("white Wins!")
                return True
            else:
                return False
        else:
            for piece in self.white_pieces:
                moves.update(self.getValidMoves(piece))
                #if white has any valid moves then red has not won
                if moves:
                    break
            #if moves is empty then red wins
            if not moves:
                self.winner = "RED"
                print("Red Wins!")
                return True
            else:
                return False

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

    def evaluateBoard(self):
        return self.white_pieces.length() - self.red_pieces.length()

    def getPieces(self, colour):
        if colour == "RED":
            return self.red_pieces
        else:
            return self.white_pieces

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
