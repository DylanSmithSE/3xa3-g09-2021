# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These
# Main class runs the game
from board2 import *
from game import *
#from minmax2 import *
from GUI2 import *
from menu2 import *
# Setup variables
width = 8
height = 8
firstPlayer = 0

### MAIN PROGRAM ###
gui = GUI()
game = Game(gui)
clock = pygame.time.Clock()
moves = []

while game.board.gameWon == True:
    clock.tick(60)
    gui.display_board(game.board.boardState, game.board.turn)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.board.gameWon = 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_object = gui.get_clicked_object(pos)
            if clicked_object == "board" and game.gui.start_game == 0:
                game.select(gui.get_square_clicked(pos))
            elif clicked_object == "new":
                menu().new_game(game)
            elif clicked_object == "tutorial":
                menu().tutorial(game)
            elif clicked_object == "1-player mode":
                menu().select_game_mode(game, 1)
            elif clicked_object == "2-player mode":
                menu().select_game_mode(game, 2)
            elif clicked_object == "white":
                menu().select_color(game, "white")
            elif clicked_object == "red":
                menu().select_color(game, "red")
            elif clicked_object == "start":
                menu().start_game(game, width, height, firstPlayer)
            elif clicked_object == "nothing":
                print("You didn't click on anything")

            gui.display_board(game.board.boardState, game.board.turn)

    #
    # if len(moves) == 1 and not(moves[0] in board.whitelist):
    #     gui.update_message("That is not one of your pieces. Choose a white piece.")
    #     moves = []
    # elif len(moves) == 2:
    #     userMove = (moves[0], moves[1], board.NOTDONE)
    #     # board.moveWhite(*userMove)
    #     try:
    #         moveWhite(board, *userMove)
    #     except Exception as e:
    #         print(e)
    #         moves = []
    #         gui.update_message("Invalid move, try again")
    #         continue

        # temp = minMax2(board)
        # board = temp[0]
        # if board.gameWon == board.WHITE:
        #     print("White Wins\nGame Over")
        #     break
        # elif board.gameWon == board.RED:
        #     print("Red Wins\nGame Over")
        #     break
pygame.quit()





# # Main game loop
# while b.gameWon == -1:
#     # First it is the users turn
#     userMove = getUserMove(b)
#     try:
#         b.moveWhite(*userMove)
#     except Exception:
#         print("Invalid move")
#         continue
#
#     # Then it is the computers turn
#     temp = minMax2(b)
#     b = temp[0]
#     print("**********COMPUTER MOVE**********")
#     b.printBoard()
#     if b.gameWon == b.WHITE:
#         print("White Wins\nGame Over")
#         break
#     elif b.gameWon == b.BLACK:
#         print("Black Wins\nGame Over")
#         break

# # Gets the move from the User
# def getUserMove(b):
#     statement1 = "Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1])
#     print(statement1)
#     while True: # Loop until proper input
#         move = []
#         move = input().lower().split()
#         if not(len(move) == 2):
#             print("That is not a valid move, try again.")
#             continue
#         moveFromTup = (int(move[0][1]), ord(move[0][0]) - 97)
#         moveToTup = (int(move[1][1]), ord(move[1][0]) - 97)
#         # Is the piece we want to move one we own?
#         if not (moveFromTup in b.whitelist):
#             print(("You do not own", moveFromTup, "please select one of.", b.whitelist))
#             continue
#         break
#     move = (moveFromTup, moveToTup, b.NOTDONE)
#     return move
