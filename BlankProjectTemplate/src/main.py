# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These
# Main class runs the game
from board import *
from game import *
#from minmax2 import *
from GUI import *
from menu import *
# Setup variables
width = 8
height = 8
firstPlayer = 0

### MAIN PROGRAM ###
gui = GUI()
game = Game(gui)
clock = pygame.time.Clock()
moves = []

while game.board.gameWon == -1:
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
pygame.quit()