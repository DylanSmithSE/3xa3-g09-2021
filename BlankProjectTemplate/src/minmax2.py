## @file minmax2.py
#  @details Reference: https://github.com/techwithtim/Python-Checkers-AI
#  @author Ardhendu, Dylan, Thaneegan
#  @date April 5th 2021
from copy import deepcopy
from board2 import *
import pygame

## @brief Minmax determines the best move that a player can make
#  @param currentBoard Is a board object representing the state of the game to
#   be evaluated
#  @param maxPlayer is a boolean value. It is true when the player calling minmax
#   is the player maximizing the score (white pieces in our case). It is negative
#   when the player calling minmax is minimizing the score.
#  @param depth Is the recursive depth that the algorithm will search. It is an
#   exponential algorithm so the higher the recursive depth the slower the AI
#   performs.
#  @return bestBoard.evaluateBoard(), bestBoard The minmax function returns the
#   score of the best move, as well as the board after the best move has been made. 
def minmax(currentBoard,maxPlayer,depth):
    #if the we are at the furthest depth or the game is over we can return the boardScore
    if depth == 0 or currentBoard.checkGameEnd():
        return currentBoard.evaluateBoard(), currentBoard

    #get the best board at the current depth for max player
    if maxPlayer:
        maxScore = float('-inf')
        bestBoard = None
        #go through all possible moves get evaluation of the boards
        for board in _getAllBoards(currentBoard):
            score = minmax(board,False,depth-1)[0]
            maxScore = max(maxScore,score)
            if maxScore == score:
                bestBoard = board
        return bestBoard.evaluateBoard(), bestBoard
    else:
        minScore = float('inf')
        bestBoard = None
        #go through all possible moves get evaluation of the boards
        for board in _getAllBoards(currentBoard):
            score = minmax(board,True,depth-1)[0]
            minScore = min(minScore,score)
            if minScore == score:
                bestBoard = board
        return bestBoard.evaluateBoard(), bestBoard

#gets a board, based on the current turn. simulates all possible moves and returns a list of boards
def _getAllBoards(currentBoard):
    newBoards = []
    #for every piece on the board that can move
    for piece in currentBoard.getPieces(currentBoard.turn):
        #get all the moves the piece can make
        possibleMoves = currentBoard.getValidMoves(piece)
        #simulate all moves
        for move, captures in possibleMoves.items():
            #need to make copies so that the original board is not changed
            tempBoard = deepcopy(currentBoard)
            tempPiece = tempBoard.boardState[piece.row][piece.col]
            tempBoard.move(tempPiece,move,captures)
            newBoards.append(tempBoard)
    return newBoards
