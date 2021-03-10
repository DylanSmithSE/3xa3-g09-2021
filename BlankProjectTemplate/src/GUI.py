import pygame
from board import *

screen_dimensions = (1060, 720)

class GUI:
    def __init__(self):
        #import images
        self.board_img = pygame.image.load('./img/board.png')
        self.red_piece = pygame.image.load('./img/red_man.png')
        self.white_piece = pygame.image.load('./img/white_man.png')
        self.new_game_button = pygame.image.load('./img/btn_new_game.png')
        self.tutorial_button = pygame.image.load('./img/btn_tutorial.png')
        #get dimensions of board
        self.board_height = self.board_img.get_height()
        self.board_width = self.board_img.get_width()
        self.num_cols = 8
        self.num_rows = 8
        self.screen = None
        self.message = "Welcome to Checkers, hit start game to begin."
        print(self.message)
        self.make_display()

    def make_display(self):
        self.screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption('Checkers')
        self.screen.fill((0,0,0))
        self.screen.blit(self.new_game_button, (720,0))
        self.screen.blit(self.tutorial_button, (720,80))

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

    def update_message(self, message):
        self.message = message
        print(message)

    def display_piece(self,colour, row, col):
        # print('row and col is ', (row, col))
        # if colour == 'BLACK':
        #     self.screen.blit(self.red_piece, self.calc_pos(col, row))
        # elif colour == 'WHITE':
        #     self.screen.blit(self.white_piece, self.calc_pos(col, row))
        # else:
        #     pass
        if colour == 'BLACK':
            self.screen.blit(self.red_piece, self.calc_pos(row, col))
        elif colour == 'WHITE':
            self.screen.blit(self.white_piece, self.calc_pos(row, col))
        else:
            pass

    def calc_pos(self, row, col):
        x = row * self.board_width/self.num_cols
        y = col * self.board_height/self.num_rows
        return (x,y)

    #returns a string of what was clicked on
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

    #calculates the row and collumn if user clicks on board
    def get_square_clicked(self, pos):
        x, y = pos
        # row = y // (self.board_height/self.num_rows)
        # col = x // (self.board_width/self.num_cols)
        row = x // (self.board_height/self.num_rows)
        col = y // (self.board_width/self.num_cols)
        return (int(col),int(row))

#testing
# b = [['','W','','W','','W','','W'],\
#                 ['W','','W','','W','','W',''],\
#                 ['','W','','W','','W','','W'],\
#                 ['','','','','','','',''],\
#                 ['','','','','','','',''],\
#                 ['R','','R','','R','','R',''],\
#                 ['','R','','R','','R','','R'],\
#                 ['R','','R','','R','','R','']]
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
#     gui.display_board(b)
#
# #closes screen when the loop ends
# #loop ends when we the "x" on the screen is clicked
# pygame.quit()
