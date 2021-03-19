## @file minmax.py
#  @author Carson Wilcox, Thaneegan, Dylan, Ardhendu  
#  @date 3/5/2021

# Provides the minmax functionality as well as static evaluation
from copy import deepcopy

## @brief Function to check if game is won
#  @details Function takes in board object and returns bool
#  @param board board object cotaining the state
def is_won(board):
    return board.gameWon != board.NOTDONE
        
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
        print('bestboard and bestval is ', (bestBoard, bestVal))
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
    return maxMinBoard(maxBoard, currentDepth-1, float('-inf'))
    
## @brief Function to calculate and predict best move from perspective of the player
#  @details Function takes in board object as well as currentdepth to return best move for the AI
#  @param maxBoard board object with final state after completeing all the possible moves
#  @param currentDepth depth for the AI to predict best player move
def minMove2(minBoard, currentDepth):
    return maxMinBoard(minBoard, currentDepth-1, float('inf'))

## @brief Function to calculate and predict best move from perspective of the player
#  @details Function takes in board object as well as currentdepth to return best move for the AI
#  @param maxBoard board object with final state after completeing all the possible moves
#  @param currentDepth depth for the AI to predict best player move
def maxMinBoard(board, currentDepth, bestMove):
    print('yeeee this being acacaalalallalal')

    if is_won(board) or currentDepth <= 0:
        return (board, staticEval2(board))

    best_move = bestMove
    best_board = None    

    if bestMove == float('-inf'):
        # Create the iterator for the Moves
        moves = board.iterBlackMoves()
        for move in moves:
            maxBoard = deepcopy(board)
            maxBoard.moveSilentBlack(*move)
            value = minMove2(maxBoard, currentDepth-1)[1]
            if value > best_move:
                best_move = value
                best_board = maxBoard         

    elif bestMove == float('inf'):
        moves = board.iterWhiteMoves()
        for move in moves:
            minBoard = deepcopy(board)
            minBoard.moveSilentWhite(*move)
            value = maxMove2(minBoard, currentDepth-1)[1]
            if value < best_move:
                best_move = value
                best_board = minBoard
  
    else:
        raise Exception("bestMove is set to something other than inf or -inf")
  
    return (best_board, best_move)

## @brief Function to evaluate the board state and which player is favoured to win to assess AI move
#  @param evalBoard board that needs to be evaluated
def staticEval2(evalBoard):
    if evalBoard.gameWon == evalBoard.RED:
        return float('inf')  
    elif evalBoard.gameWon == evalBoard.WHITE:
        return float('-inf')

    score = 0
    pieces = None   
    if evalBoard.turn == evalBoard.WHITE:
        pieces = evalBoard.whitelist
        scoremod = -1
    elif evalBoard.turn == evalBoard.RED:
        pieces = evalBoard.blacklist
        scoremod = 1

    distance = 0
    for piece1 in pieces:
        for piece2 in pieces:
            if piece1 == piece2:
                continue
            dx = abs(piece1[0] - piece2[0])
            dy = abs(piece1[1] - piece2[1])
            distance += dx**2 + dy**2
    distance /= len(pieces)
    score = 1.0/distance * scoremod
    
    
    return score
