from board import *
from game import *
from GUI import *
from menu import *

gui = GUI()
game = Game(gui)
clock = pygame.time.Clock()
running = True

#start the app
while running:
    clock.tick(60)
    gui.display_board(game.board.boardState, game.board.turn)

    for event in pygame.event.get():
        #if the user wants to exit the app end loop
        if event.type == pygame.QUIT:
            running = False

        #get click and determine what was clicked
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
                menu().start_game(game)
            elif clicked_object == "nothing":
                pass

            gui.display_board(game.board.boardState, game.board.turn)
pygame.quit()