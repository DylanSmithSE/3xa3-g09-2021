import pygame

SCREEN_DIMENSIONS = (1060, 720)
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
board_img = pygame.image.load('./img/Board.png')
board_img_blurry = pygame.image.load('./img/BoardBlurry.png')
red_piece = pygame.image.load('./img/RedMan.png')
white_piece = pygame.image.load('./img/WhiteMan.png')
highlighted_red_piece = pygame.image.load('./img/HighlightedRedMan.jpg')
highlighted_white_piece = pygame.image.load('./img/HighlightedWhiteMan.jpg')
red_king = pygame.image.load('./img/RedKing.png')
white_king = pygame.image.load('./img/WhiteKing.png')
highlighted_red_king = pygame.image.load('./img/HighlightedRedKing.jpg')
highlighted_white_king = pygame.image.load('./img/HighlightedWhiteKing.jpg')
valid_move = pygame.image.load('./img/ValidMove.png')
black_screen = pygame.image.load('./img/BlackScreen.png')
new_game_button = pygame.image.load('./img/ButtonNewGame.png')
new_game_countdown_3 = pygame.image.load('./img/Countdown3.png')
new_game_countdown_2 = pygame.image.load('./img/Countdown2.png')
new_game_countdown_1 = pygame.image.load('./img/Countdown1.png')
new_game_countdown_0 = pygame.image.load('./img/Countdown0.png')
tutorial_button = pygame.image.load('./img/ButtonTutorial.png')
tutorial_image = pygame.image.load('./img/FullTutorial.png')
start_button = pygame.image.load('./img/ButtonStartGame.png')
title_choose_game_mode = pygame.image.load('./img/SelectGameMode.png')
one_players = pygame.image.load('./img/1Player.png')
two_players = pygame.image.load('./img/2Player.png')
one_players_selected = pygame.image.load('./img/1PlayerSelected.png')
two_players_selected = pygame.image.load('./img/2PlayerSelected.png')
title_choose_color = pygame.image.load('./img/ChooseColor.png')
select_white = pygame.image.load('./img/ButtonWhite.png')
selected_white = pygame.image.load('./img/ButtonWhiteSelected.png')
select_red = pygame.image.load('./img/ButtonRed.png')
selected_red = pygame.image.load('./img/ButtonRedSelected.png')
winner_red = pygame.image.load('./img/GameoverRedWins.png')
winner_white = pygame.image.load('./img/GameoverWhiteWins.png')
