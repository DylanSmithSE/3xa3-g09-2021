## @file minmax.py
#  @author Carson Wilcox, Thaneegan, Dylan, Ardhendu  
#  @brief Provides the minmax functionality  for AI as well as static evaluation
#  @date 3/17/2021

from copy import deepcopy
#from gameLogic import *
from game import *
from board2 import *
#from board import *

# ## @brief Function to check if game is won
# #  @details Function takes in board object and returns bool
# #  @param board board object cotaining the state
# def is_won(board):
#     return board.gameWon != -1
        
## @brief Main minimax algorithm function for AI
#  @details Function takes in board object and returns most appropirate move for the AI
#  @param board board object cotaining the state
def minMax2(board):
    bestBoard = None
    currentDepth = board.maxDepth + 1
    while not bestBoard and currentDepth > 0:
        currentDepth -= 1
        # Get the best move and it's value from maxMinBoard (minmax handler)
        (bestBoard, bestVal) = maxMove2(board, currentDepth)

    # If we got a NUll board raise an exception
    if not bestBoard:
        raise Exception("Could only return null boards")
    # Otherwise return the board and it's value
    else:
        return (bestBoard, bestVal)

## @brief Function to calculate best move for AI
#  @details Function takes in board object as well as currentdepth to return best move for the AI
#  @param maxBoard board object with final state after completeing all the possible moves
#  @param currentDepth depth for the AI to predict best move
def maxMove2(maxBoard, currentDepth):
    # return maxMinBoard(maxBoard, currentDepth-1, float('-inf'))
    return maxMinBoard(maxBoard, currentDepth-1, float('inf'))
    
## @brief Function to calculate and predict best move from perspective of the player
#  @details Function takes in board object as well as currentdepth to return best move for the AI
#  @param maxBoard board object with final state after completeing all the possible moves
#  @param currentDepth depth for the AI to predict best player move
def minMove2(minBoard, currentDepth):
    # return maxMinBoard(minBoard, currentDepth-1, float('inf'))
    return maxMinBoard(minBoard, currentDepth-1, float('-inf'))

## @brief Function to calculate and predict best move from perspective of the player
#  @details Function takes in board object as well as currentdepth to return best move for the AI
#  @param maxBoard board object with final state after completeing all the possible moves
#  @param currentDepth depth for the AI to predict best player move
def maxMinBoard(board, currentDepth, bestMove):

    if board.checkGameEnd() or currentDepth <= 0:
        return (board, staticEval2(board))

    best_move = bestMove
    best_board = None  

    if bestMove == float('-inf'):
        # Create the iterator for the Moves

        red_position = []
        move_skipped_1 = []
        moves_1 = []
        piece_at = []
        for i in board.red_pieces:
            red_position.append(board.getValidMoves(i))
        idx = 0
        for i in red_position:
            if(i == {}):
                continue
            for x in list(i.keys()):
                piece_at.append(idx)
                moves_1.append(((board.red_pieces[idx].row, board.red_pieces[idx].col), x))
            move_skipped_1.extend(list(red_position[idx].values()))
            idx += 1

        idx = 0

        for move, move_skip in zip(moves_1, move_skipped_1):
            maxBoard = deepcopy(board)
            print('cor obj ', (maxBoard.red_pieces[piece_at[idx]].row, maxBoard.red_pieces[piece_at[idx]].col))
            maxBoard.move(maxBoard.red_pieces[piece_at[idx]], move[1][0], move[1][1], move_skip)
            #moveSilentBlack(maxBoard, *move)
            value = minMove2(maxBoard, currentDepth-1)[1]
            if value > best_move:
                best_move = value
                best_board = maxBoard
            idx += 1       

    elif bestMove == float('inf'):
        white_position = []
        move_skipped_2 = []
        moves_2 = []
        wpiece_at = []
        for i in board.white_pieces:
            white_position.append(board.getValidMoves(i))
        idx = 0
        for i in white_position:
            if(i == {}):
                idx += 1
                continue
            for x in list(i.keys()):
                wpiece_at.append(idx)
                moves_2.append(((board.white_pieces[idx].row, board.white_pieces[idx].col), x))
            move_skipped_2.extend(list(white_position[idx].values()))
            idx += 1

        idx = 0
        #moves = iterWhiteMoves(board)
        for move, move_skip in zip(moves_2, move_skipped_2):
            minBoard = deepcopy(board)
            minBoard.move(minBoard.white_pieces[wpiece_at[idx]],  move[1][0], move[1][1], move_skip)
            value = maxMove2(minBoard, currentDepth-1)[1]
            if value < best_move:
                best_move = value
                best_board = minBoard
            idx += 1
  
    else:
        raise Exception("bestMove is set to something other than inf or -inf")
  
    return (best_board, best_move)

## @brief Function to evaluate the board state and which player is favoured to win to assess AI move
#  @param evalBoard board that needs to be evaluated
def staticEval2(evalBoard):

    dist = len(evalBoard.white_pieces)- len(evalBoard.red_pieces)
    if(evalBoard.turn == "WHITE"):
        return -1*dist
    else:
        return dist
    # # if evalBoard.gameWon == evalBoard.RED:
    # #     return float('inf')  
    # # elif evalBoard.gameWon == evalBoard.WHITE:
    # #     return float('-inf')

    # score = 0
    # pieces = None   
    # if evalBoard.turn == "WHITE":
    #     pieces = evalBoard.white_pieces
    #     scoremod = -1
    # elif evalBoard.turn == "RED":
    #     pieces = evalBoard.red_pieces
    #     scoremod = 1

    # distance = 0
    # for piece1 in pieces:
    #     for piece2 in pieces:
    #         if piece1 == piece2:
    #             continue
    #         dx = abs(piece1.row - piece2.row)
    #         dy = abs(piece1.col - piece2.col)
    #         distance += dx**2 + dy**2
    # distance /= len(pieces)
    # score = 1.0/distance * scoremod
    
    
    # return score
