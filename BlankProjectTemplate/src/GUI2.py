## @file GUI.py
## @brief Following module handles the graphical user interface for the checkers game
#  @author Dylan, Thaneegan, Ardhendu
#  @date March 3 2021
import pygame
from board2 import *
from constants import *
from pieces2 import *

screen_dimensions = (1060, 720)


class GUI:
    ## @brief The init method loads the graphics, sets the dimensions of the
    #         board and calls make_display()
    def __init__(self):
        #import images
        self.board_img = pygame.image.load('./img/board.png')
        self.red_piece = pygame.image.load('./img/red_man.png')
        self.white_piece = pygame.image.load('./img/white_man.png')
        self.red_king = pygame.image.load('./img/red_king.png')
        self.white_king = pygame.image.load('./img/white_king.png')
        self.new_game_button = pygame.image.load('./img/btn_new_game.png')
        self.tutorial_button = pygame.image.load('./img/btn_tutorial.png')
        #get dimensions of board
        self.board_height = self.board_img.get_height()
        self.board_width = self.board_img.get_width()
        self.screen = None
        self.message = "Welcome to Checkers, hit start game to begin."
        print(self.message)
        self.make_display()

    ## @brief make_display() creates the screen, sets the caption and adds
    #         the buttons to the screen
    def make_display(self):
        self.screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption('Checkers')
        self.screen.fill((0,0,0))
        self.screen.blit(self.new_game_button, (720,0))
        self.screen.blit(self.tutorial_button, (720,80))

    ## @brief Given the state of a board, displays the board on the screen
    #  @details Loops through the board_state and calls display_piece to display
    #           the pieces
    #  @param board_state Two dimensional array representing the state of the board
    def display_board(self, board_state):
        self.screen.blit(self.board_img, (0, 0))
        #Adding pieces
        y = 0
        for col in board_state:
            x = 0
            for row in col:
                self.display_piece(row,x,y)
                x+=1
            y+=1
        # x = 0
        # for row in board_state:
        #     # print('row is ', row)
        #     # break
        #     y = 0
        #     for col in row:
        #         # print('col is ', col)
        #         self.display_piece(col,x,y)
        #         y+=1
        #     x+=1
        pygame.display.update()

    ## @brief Sets the message to be displayed
    #  @param message The message to be displayed
    def update_message(self, message):
        self.message = message

    ## @brief Displays a piece of the colour given, in the row and collumn given
    #  @param colour The colour of the piece to be displayed
    #  @param row The row to display the piece
    #  @param col The collumn to display the piece
    def display_piece(self,colour, row, col):
        if colour == 0:
            pass
        elif colour.color == 'RED':
            if colour.king:
                self.screen.blit(self.red_king, self.calc_pos(row, col))
            else:
                self.screen.blit(self.red_piece, self.calc_pos(row, col))
        elif colour.color == 'WHITE':
            if colour.king:
                self.screen.blit(self.white_king, self.calc_pos(row, col))
            else:
                self.screen.blit(self.white_piece, self.calc_pos(row, col))

    ## @brief Calculates the position on the screen of the top left corner of
    #         the square given
    #  @details This function will be used by display piece to determine where
    #           on the screen to place the image
    #  @param row The row number of the square
    #  @param col The collumn number of the square
    #  @return (x,y) the coordinates of the top left corner of the square on the
    #          screen
    def calc_pos(self, row, col):
        x = row * self.board_width/COLS
        y = col * self.board_height/ROWS
        return (x,y)

    ## @brief get_clicked_object() is passed the position of a mouseclick and
    #         returns what was clicked on
    #  @param pos The tuple representing the mouseclick location on the screen
    #  @return A string indicating what was clicked
    def get_clicked_object(self, pos):
        x,y = pos
        if x <= 720 and y <= 720:
            return "board"
        elif x > 720 and y <= 70:
            print("New")
            print(x, y)
            return "new"
        elif x > 720 and y >= 80 and y <= 150:
            print("Tutorial")
            print(x, y)
            return "tutorial"
        else:
            print(x, y)
            return "nothing"

    ## @brief get_square_clicked() is called when the user clicks on the board.
    #  @details When the user clicks on the board the tuple containing the
    #           row and collumn of the corresponding square clicked on is returned
    #  @param pos The position of the mouseclick
    #  @return (col,row) The row and collumn corresponding to the square the User
    #          clicked on
    def get_square_clicked(self, pos):
        x, y = pos
        row = x // (self.board_height/ROWS)
        col = y // (self.board_width/COLS)
        return (int(col), int(row))

# # # testing
# b = [[0,piece(0,1,"WHITE",1),0,piece(0,3,"WHITE",1),0,piece(0,5,"WHITE",1),0,piece(0,7,"WHITE",1)],\
#                     [piece(1,0,"WHITE",1),0,piece(1,2,"WHITE",1),0,piece(1,4,"WHITE",1),0,piece(1,6,"WHITE",1),0],\
#                     [0,piece(2,1,"WHITE",1),0,piece(2,3,"WHITE",1),0,piece(2,5,"WHITE",1),0,piece(2,7,"WHITE",1)],\
#                     [0,0,0,0,0,0,0,0],\
#                     [0,0,0,0,0,piece(4,5,"RED",1),0,0],\
#                     [piece(5,0,"RED",1),0,0,0,piece(5,4,"RED",1),0,piece(5,6,"RED",1),0],\
#                     [0,piece(6,1,"RED",1),0,piece(6,3,"RED",1),0,piece(6,5,"RED",1),0,piece(6,7,"RED",1)],\
#                     [piece(7,0,"RED",1),0,piece(7,2,"RED",1),0,piece(7,4,"RED",1),0,piece(7,6,"RED",1),0]]
#
# gui = GUI()
#
# run = True
# clock = pygame.time.Clock()
# while run:
#     #slows down the while loop to make it run the same speed on diff computers
#     clock.tick(60)
#     pass
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pass
#         else:
#             pass
#     b[0][1].make_king()
#     b[7][0].make_king()
#     gui.display_board(b)
#
# #closes screen when the loop ends
# #loop ends when we the "x" on the screen is clicked
# pygame.quit()