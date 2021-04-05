## @file board.py
#  @title Board
#  @details Reference: https://github.com/techwithtim/Python-Checkers-AI
#  @author Ardhendu, Dylan, Thaneegan
#  @date April 5th 2021
from pieces2 import *
from constants import *

## @brief The Board class handles the state of the board. Its main function is to
#   determine where pieces of the board can move.
class Board():
    ## @brief The constructor initializes the member variables and calls setBoard
    #  @param gui The GUI is passed in to relay information stored withing the
    #   GUI class to the setBoard method
    def __init__(self, gui, board = None, turn = "RED"):
        ## turn stores the piece colour that can move
        self.turn = turn
        self.gameWon = -1
        ## boardState stores the state of the board.
        self.boardState = [[0] * ROWS for x in range(COLS)]
        ## red_pieces stores all the red pieces that remain
        self.red_pieces = []
        ## white_pieces stores all the white pieces that remain
        self.white_pieces = []
        ## stores the colour of the winner when the game ends
        self.winner = ""
        self.setBoard(gui, board)

    ## @brief resetBoard resets the member variables and calls setBoard
    #  @param gui The GUI is passed in to relay information stored withing the
    #   GUI class to the setBoard method
    def resetBoard(self, gui):
        self.turn = "RED"
        self.gameWon = -1
        self.boardState = [[0] * ROWS for x in range(COLS)]
        self.red_pieces = []
        self.white_pieces = []
        self.setBoard(gui)
        print("new game")
        # Tk().wm_withdraw() #to hide the main window
        # messagebox.showinfo('Starting new game...','New game selected, enjoy!')

    ## @brief setBoard sets the board state based on the colour of pieces the
    #   user chooses
    #  @param gui The GUI is passed in to relay the piece colour choice made by
    #   the user
    def setBoard(self, gui, board = None):
        #overloading the constructor to help with testing
        if board:
            load_setup = board
            red_increment = -1
            white_increment = 1

        else:
            load_setup = ""
            red_increment = 0
            white_increment = 0
            if gui.color_selected == "RED":
                print('RED SELECTED')
                load_setup = REGULAR_BOARD
                red_increment = -1
                white_increment = 1
            else:
                print('WHITE SELECTED')
                load_setup = FLIPPED_BOARD
                red_increment = 1
                white_increment = -1

        x = 0
        for row in load_setup:
            y = 0
            for col in row:
                if col == "RED":
                    p = piece(x,y,"RED",red_increment)
                    self.boardState[x][y] = p
                    self.red_pieces.append(p)
                elif col == "WHITE":
                    p = piece(x,y,"WHITE",white_increment)
                    self.boardState[x][y] = p
                    self.white_pieces.append(p)
                else:
                    pass
                y = y + 1
            x = x + 1

    ## @brief The move method takes a piece and moves it to the given location
    #  @details It must move the piece to the specified location and remove all
    #   all the pieces that are jumped along the way
    #  @param piece Is the piece that will be moving
    #  @param move (row,col) Is the location the piece will be moving to
    #  @param skipped [(row,col),(row,col),...] Is an array of the locations
    #   of the pieces that are jumped and need to be removed
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

    ## @brief The remove method takes a piece and removes it from the board
    #  @param piece The piece being removed
    def remove(self, piece):
        self.boardState[piece.row][piece.col] = 0
        if piece in self.red_pieces:
            self.red_pieces.remove(piece)
        if piece in self.white_pieces:
            self.white_pieces.remove(piece)

    ## @brief Changes the turn
    def changeTurn(self):
        if self.turn == "RED":
            self.turn = "WHITE"
        else:
            self.turn = "RED"

    ## @brief Checks to see if the boardState is in a win/loss state
    #  @details Checks to see if the player with the current turn has any moves
    #   remaining.
    #  @return True when the boardState is in a win/loss state
    #  @return False when the boardState is not in a win/loss state
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

    ## @brief Determines the score of a position. Is used by the minmax function
    #  @details Each player will try to maximize the difference in the number
    #   of pieces they have vs the number of pieces their opponent has
    def evaluateBoard(self):
        return len(self.white_pieces) - len(self.red_pieces)

    ## @brief Given a colour, returns all the pieces of that colour
    #  @param colour The colour of pieces to be returned
    #  @return Returns the array of pieces, of the specified colour
    def getPieces(self, colour):
        if colour == "RED":
            return self.red_pieces
        else:
            return self.white_pieces

    ## @brief Returns all of the valid moves that a piece can make
    #  @param piece The piece to determine the valid moves for
    #  @return moves {(row,col): [(row,col),...],...} A dictionary where the keys
    #   are the location (stored as a tuple) of all the valid moves the piece can make,
    #   the corresponding value is an array of locations (stored as tuples)
    #   representing the pieces that are jumped in making that move.
    def getValidMoves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        colour = piece.color
        direction = piece.direction
        if not piece.king:
            self._checkLeft(row,col,colour,direction,False,False,[],moves)
            self._checkRight(row,col,colour,direction,False,False,[],moves)
        else:
            self._checkLeft(row,col,colour,-1*direction,True,False,[],moves)
            self._checkRight(row,col,colour,-1*direction,True,False,[],moves)
            self._checkLeft(row,col,colour,direction,True,False,[],moves)
            self._checkRight(row,col,colour,direction,True,False,[],moves)
        return moves

    def _checkLeft(self,row,col,colour,direction,isKing,haveSkipped,captures,moves):
        #need this or else all entries of moves will have the same skipped list
        skipped = []
        for tup in captures:
            skipped.append(tup)

        #if the move is on the board still
        if row+direction>=0 and row+direction<8 and col-1>=0:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row+direction][col-1] == 0:
                    if not (row+direction,col-1) in moves:
                        moves[(row+direction,col-1)] = []
                elif self.boardState[row+direction][col-1].color != colour:
                    self._checkLeftSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row+direction][col-1] == 0:
                    pass
                elif self.boardState[row+direction][col-1].color != colour:
                    self._checkLeftSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass

    def _checkLeftSkip(self,row,col,colour,direction,isKing,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if (row+(2*direction))>=0 and (row+(2*direction)<8) and col-2>=0:
            #if we can skip the piece we do and then _check if we can continue
            if self.boardState[row+(2*direction)][col-2] == 0:
                #if we have not visited the square yet
                if not (row+(2*direction),col-2) in moves:
                    skipped.append((row+direction,col-1))
                    moves[(row+(2*direction),col-2)] = skipped
                    if not isKing:
                        self._checkLeft(row+(2*direction),col-2,colour,direction,False,True,skipped,moves)
                        self._checkRight(row+(2*direction),col-2,colour,direction,False,True,skipped,moves)
                    else:
                        self._checkLeft(row+(2*direction),col-2,colour,direction,True,True,skipped,moves)
                        self._checkRight(row+(2*direction),col-2,colour,direction,True,True,skipped,moves)
                        self._checkLeft(row+(2*direction),col-2,colour,-1*direction,True,True,skipped,moves)
                        self._checkRight(row+(2*direction),col-2,colour,-1*direction,True,True,skipped,moves)
            else:
                pass


    def _checkRight(self,row,col,colour,direction,isKing,haveSkipped,captures,moves):
        #need this or else all entries of moves will have the same skipped list
        skipped = []
        for tup in captures:
            skipped.append(tup)
        #if the move is on the board still
        if row+direction>=0 and row+direction<8 and col+1<8:
            #no captures have been made
            if not haveSkipped:
                if self.boardState[row+direction][col+1] == 0:
                    if not (row+direction,col+1) in moves:
                        moves[(row+direction,col+1)] = []
                elif self.boardState[row+direction][col+1].color != colour:
                    self._checkRightSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass
            #if a piece has been captured already
            else:
                if self.boardState[row+direction][col+1] == 0:
                    pass
                elif self.boardState[row+direction][col+1].color != colour:
                    self._checkRightSkip(row,col,colour,direction,isKing,skipped,moves)
                else:
                    pass

    def _checkRightSkip(self,row,col,colour,direction,isKing,captures,moves):
        skipped =[]
        for tup in captures:
            skipped.append(tup)
        if (row+(2*direction))>=0 and (row+(2*direction)<8) and col+2<8:
            #if we can skip the piece we do and then _check if we can continue
            if self.boardState[row+(2*direction)][col+2] == 0:
                #if we have not visited the square yet
                if not (row+(2*direction),col+2) in moves:
                    skipped.append((row+direction,col+1))
                    moves[(row+(2*direction),col+2)] = skipped
                    if not isKing:
                        self._checkRight(row+(2*direction),col+2,colour,direction,False,True,skipped,moves)
                        self._checkLeft(row+(2*direction),col+2,colour,direction,False,True,skipped,moves)
                    else:
                        self._checkRight(row+(2*direction),col+2,colour,direction,True,True,skipped,moves)
                        self._checkLeft(row+(2*direction),col+2,colour,direction,True,True,skipped,moves)
                        self._checkRight(row+(2*direction),col+2,colour,-1*direction,True,True,skipped,moves)
                        self._checkLeft(row+(2*direction),col+2,colour,-1*direction,True,True,skipped,moves)
            else:
                pass
