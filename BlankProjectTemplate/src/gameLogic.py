## @file gameLogic.py
#  @author Carson Wilcox, Thaneegan, Dylan, Ardhendu  
#  @brief Provides logic for game (including making moves)
#  @date 3/17/2021

## @brief Iterates through the white pieces array to generate moves for white pieces.
#  @param board The state of the current board
#  @return Returns the location of the possible move of the selected piece
def iterWhiteMoves(board):
    """
        Main generator for white moves
    """
    for piece in board.whitelist:
        for move in iterWhitePiece(board, piece):
            yield move

## @brief Iterates through the black pieces array to generate moves for black pieces.
#  @param board The state of the current board
#  @return Returns the location of the possible move of the selected piece
def iterBlackMoves(board):
    """
        Main Generator for black moves
    """
    for piece in board.blacklist:
        for move in iterBlackPiece(board, piece):
            yield move
    print('blacklist is ', board.blacklist)

## @brief Checks for possible moves for the selected piece
#  @param board The state of the current board
#  @param piece The piece to be moved
#  @return Returns the location of the possible move of the selected piece
def iterWhitePiece(board, piece):
    """
        Generates possible moves for a white piece
    """
    # return board.iterBoth(piece, ((-1,-1),(1,-1)))
    return iterBoth(board, piece, ((-1,1),(-1,-1)))

## @brief Checks for possible moves for the selected piece
#  @param board The state of the current board
#  @param piece The piece to be moved
#  @return Returns the location of the valid move of the selected piece
def iterBlackPiece(board, piece):
    """
        Generates possible moves for a black piece
    """
    # return board.iterBoth(piece, ((-1,1),(1,1)))
    return iterBoth(board, piece, ((1,-1),(1,1)))

## @brief Checks for possible moves for the selected piece
#  @param board The state of the current board
#  @param piece The piece to be moved
#  @param moves The set of possible moves
#  @return Returns the location of the valid moves of the selected piece
def iterBoth(board, piece, moves):
    """
        Handles the actual generation of moves for either black or white pieces
    """
    #print('piece is ', piece)
    for move in moves:
        # Regular Move
        targetx = piece[0] + move[0]
        targety = piece[1] + move[1]
        #print(f'targetx is {targetx} and targety is {targety}' )
        # If the move is out of bounds don't move
        if targetx < 0 or targetx >= board.width or targety < 0 or targety >= board.height:
            continue
        target = (targetx, targety)
        # Check that there is nothing in the way of moving to the target
        black = target in board.blacklist
        white = target in board.whitelist
        if not black and not white:
            #print('p and t is ', piece, target)
            yield (piece, target, board.NOTDONE)
        # There was something in the way, can we jump it?
        else:
            print('in ese')
            # It has to be of the opposing color to jump
            if board.turn == board.RED and black:
                continue
            elif board.turn == board.WHITE and white:
                continue
            # Jump proceeds by adding the same movement in order to jump over the opposing
            # piece on the checkerboard
            jumpx = target[0] + move[0]
            jumpy = target[1] + move[1]
            # If the jump is going to be out of bounds don't do it.
            if jumpx < 0 or jumpx >= board.width or jumpy < 0 or jumpy >= board.height:
                continue
            jump = (jumpx, jumpy)
            # Check that there is nothing in the jumpzone
            black = jump in board.blacklist
            white = jump in board.whitelist
            if not black and not white:
                yield (piece, jump, board.turn)

## @brief Moves a black piece, calls the updateboard method, determines if black piece player has won or loss (sets the turn to white after)
#  @param board The state of the current board
#  @param moveFrom The location of the piece to be moved
#  @param moveTo The location of where the piece has to be moved to
def moveSilentBlack(board, moveFrom, moveTo, winLoss):
    """
        Move black piece without printing
    """
    if moveTo[0] < 0 or moveTo[0] >= board.width or moveTo[1] < 0 or moveTo[1] >= board.height:
        raise Exception("That would move black piece", moveFrom, "out of bounds")
    black = moveTo in board.blacklist
    white = moveTo in board.whitelist
    moveT1 = (moveTo == (moveFrom[0]-1,moveFrom[1]+1))
    moveT2 = (moveTo == (moveFrom[0]-1,moveFrom[1]-1))
    moveT3 = (moveTo == (moveFrom[0]+1,moveFrom[1]-1))
    moveT4 = (moveTo == (moveFrom[0]+1,moveFrom[1]+1))
    moveT5 = (moveTo == (moveFrom[0]-2,moveFrom[1]+2))
    moveT6 = (moveTo == (moveFrom[0]-2,moveFrom[1]-2))
    moveT7 = (moveTo == (moveFrom[0]+2,moveFrom[1]-2))
    moveT8 = (moveTo == (moveFrom[0]+2,moveFrom[1]+2))
    if( not(black or white) and ( moveT1 or  moveT2 or moveT3 or moveT4 or moveT5 or moveT6 or moveT7 or moveT8 )):
        board.blacklist[board.blacklist.index(moveFrom)] = moveTo
        board.updateBoard()
        board.turn = board.WHITE
        board.gameWon = winLoss
    else:
        raise Exception

## @brief Moves a white piece, calls the updateboard method, determines if white piece player has won or loss (sets the turn to black after)
#  @param board The state of the current board
#  @param moveFrom The location of the piece to be moved
#  @param moveTo The location of where the piece has to be moved to
def moveSilentWhite(board, moveFrom, moveTo, winLoss):
    """
        Move white piece without printing
    """
    #print("movesillentwhite ", moveFrom, moveTo)
    if moveTo[0] < 0 or moveTo[0] >= board.width or moveTo[1] < 0 or moveTo[1] >= board.height:
        raise Exception("That would move white piece", moveFrom, "out of bounds")

    black = moveTo in board.blacklist
    white = moveTo in board.whitelist
    #print('move pair is ', (moveFrom, moveTo))
    # if( (moveTo == (moveFrom[0]-1,moveFrom[1]+1)) or  (moveTo == (moveFrom[0]-1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]-1)) or (moveTo == (moveFrom[0]+1,moveFrom[1]+1)) ):
    #     print('Trueeee')
    moveT1 = (moveTo == (moveFrom[0]-1,moveFrom[1]+1))
    moveT2 = (moveTo == (moveFrom[0]-1,moveFrom[1]-1))
    moveT3 = (moveTo == (moveFrom[0]+1,moveFrom[1]-1))
    moveT4 = (moveTo == (moveFrom[0]+1,moveFrom[1]+1))
    moveT5 = (moveTo == (moveFrom[0]-2,moveFrom[1]+2))
    moveT6 = (moveTo == (moveFrom[0]-2,moveFrom[1]-2))
    moveT7 = (moveTo == (moveFrom[0]+2,moveFrom[1]-2))
    moveT8 = (moveTo == (moveFrom[0]+2,moveFrom[1]+2))
    if( not(black or white) and ( moveT1 or  moveT2 or moveT3 or moveT4 or moveT5 or moveT6 or moveT7 or moveT8 ) ):
        print("movesillentwhite ", moveFrom, moveTo)
        board.whitelist[board.whitelist.index(moveFrom)] = moveTo
        board.updateBoard()
        board.turn = board.RED
        board.gameWon = winLoss
    else:
        print('invalid moce is ', moveFrom, moveTo)
        raise Exception

## @brief Moves a black piece, calls the updateboard method, determines if black piece player has won or loss (sets the turn to white after)
#  @param board The state of the current board
#  @param moveFrom The location of the piece to be moved
#  @param moveTo The location of where the piece has to be moved to
#  @param winLoss The state of the game
def moveBlack(board, moveFrom, moveTo, winLoss):
    """
        Move a black piece from one spot to another. \n winLoss is passed as either 0(white)
        or 1(black) if the move is a jump
    """
    moveSilentBlack(board, moveFrom, moveTo, winLoss)

## @brief Moves a white piece, calls the updateboard method, determines if white piece player has won or loss (sets the turn to black after)
#  @param board The state of the current board
#  @param moveFrom The location of the piece to be moved
#  @param moveTo The location of where the piece has to be moved to
#  @param winLoss The state of the game
def moveWhite(board, moveFrom, moveTo, winLoss):
    """
        Move a white piece from one spot to another. \n winLoss is passed as either 0(white)
        or 1(black) if the move is a jump
    """
    moveSilentWhite(board, moveFrom, moveTo, winLoss)