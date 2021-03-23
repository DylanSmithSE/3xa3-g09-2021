from copy import deepcopy
from board2 import *
import pygame

#takes in the board to consider, a boolean: true for maxplayer false for min player, recursion depth
def minmax(currentBoard,maxPlayer,depth):
    #if the we are at the furthest depth or the game is over we can return the boardScore
    if depth == 0 or currentBoard.checkGameEnd():
        return currentBoard.evaluateBoard(), currentBoard

    #get the best board at the current depth for max player
    if maxPlayer:
        maxScore = float('-inf')
        bestBoard = None
        #go through all possible moves get evaluation of the boards
        for board in getAllBoards(currentBoard):
            score = minmax(board,False,depth-1)[0]
            maxScore = max(maxScore,score)
            if maxScore == score:
                bestBoard = board
        return bestBoard.evaluateBoard(), bestBoard
    else:
        minScore = float('inf')
        bestBoard = None
        #go through all possible moves get evaluation of the boards
        for board in getAllBoards(currentBoard):
            score = minmax(board,True,depth-1)[0]
            minScore = min(minScore,score)
            if minScore == score:
                bestBoard = board
        return bestBoard.evaluateBoard(), bestBoard

#gets a board, based on the current turn. simulates all possible moves and returns a list of boards
def getAllBoards(currentBoard):
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
