import pygame

ROWS, COLS = 8,8
REGULAR_BOARD = [['','WHITE','','WHITE','','WHITE','','WHITE'],\
                    ['WHITE','','WHITE','','WHITE','','WHITE',''],\
                    ['','WHITE','','WHITE','','WHITE','','WHITE'],\
                    ['','','','','','','',''],\
                    ['','','','','','','',''],\
                    ['RED','','RED','','RED','','RED',''],\
                    ['','RED','','RED','','RED','','RED'],\
                    ['RED','','RED','','RED','','RED','']]
FLIPPED_BOARD = [['','RED','','RED','','RED','','RED'],\
                    ['RED','','RED','','RED','','RED',''],\
                    ['','RED','','RED','','RED','','RED'],\
                    ['','','','','','','',''],\
                    ['','','','','','','',''],\
                    ['WHITE','','WHITE','','WHITE','','WHITE',''],\
                    ['','WHITE','','WHITE','','WHITE','','WHITE'],\
                    ['WHITE','','WHITE','','WHITE','','WHITE','']]


OPTION_MODE_ONE = [720, 100]
OPTION_MODE_TWO = [890, 100]
OPTION_COLOR_RED = [720, 220]
OPTION_COLOR_WHITE = [890, 220]
board_img = pygame.image.load('./img/board.png')
board_img_blurry = pygame.image.load('./img/board_blurry.png')
red_piece = pygame.image.load('./img/red_man.png')
white_piece = pygame.image.load('./img/white_man.png')
highlighted_red_piece = pygame.image.load('./img/highlighted_red_man.jpg')
highlighted_white_piece = pygame.image.load('./img/highlighted_white_man.jpg')
red_king = pygame.image.load('./img/red_king.png')
white_king = pygame.image.load('./img/white_king.png')
highlighted_red_king = pygame.image.load('./img/highlighted_red_king.jpg')
highlighted_white_king = pygame.image.load('./img/highlighted_white_king.jpg')
valid_move = pygame.image.load('./img/valid_move.png')
black_screen = pygame.image.load('./img/blackScreen.png')
new_game_button = pygame.image.load('./img/btn_new_game.png')
new_game_countdown_3 = pygame.image.load('./img/countdown_3.png')
new_game_countdown_2 = pygame.image.load('./img/countdown_2.png')
new_game_countdown_1 = pygame.image.load('./img/countdown_1.png')
new_game_countdown_0 = pygame.image.load('./img/countdown_0.png')
tutorial_button = pygame.image.load('./img/btn_tutorial.png')
tutorial_image = pygame.image.load('./img/full_tutorial.png')
start_button = pygame.image.load('./img/btn_start_game.png')
title_choose_game_mode = pygame.image.load('./img/select_game_mode.png')
one_players = pygame.image.load('./img/1_player.png')
two_players = pygame.image.load('./img/2_player.png')
one_players_selected = pygame.image.load('./img/1_player_selected.png')
two_players_selected = pygame.image.load('./img/2_player_selected.png')
title_choose_color = pygame.image.load('./img/choose_color.png')
select_white = pygame.image.load('./img/btn_white.png')
selected_white = pygame.image.load('./img/btn_white_selected.png')
select_red = pygame.image.load('./img/btn_red.png')
selected_red = pygame.image.load('./img/btn_red_selected.png')
winner_red = pygame.image.load('./img/gameover_red_wins.png')
winner_white = pygame.image.load('./img/gameover_white_wins.png')
