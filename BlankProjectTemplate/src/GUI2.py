#reference: https://github.com/binary-b/python-checkers/tree/master/img
## @file GUI.py
## @brief Following module handles the graphical user interface for the checkers game
#  @author Dylan, Thaneegan, Ardhendu
#  @date March 3 2021
import pygame
import time
from board2 import *
from constants import *
from pieces2 import *
screen_dimensions = (1060, 720)


class GUI:
    ## @brief The init method loads the graphics, sets the dimensions of the
    #         board and calls make_display()
    def __init__(self):
        self.new_game = 0
        self.tutorial = False
        self.start_game = 1
        self.single_player = 1
        self.color_selected = "RED"
        self.selected = []
        self.moves = {}
        self.board_height = board_img.get_height()
        self.board_width = board_img.get_width()
        self.screen = None
        self.make_display()

    ## @brief make_display() creates the screen, sets the caption and adds
    #         the buttons to the screen
    def make_display(self):
        self.screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption('Checkers')
        self.screen.fill((0,0,0))

    def display_menu(self):
        self.screen.blit(black_screen, (720,0))
        self.screen.blit(new_game_button, (720,0))
        self.screen.blit(tutorial_button, (720,80))

    ## @brief Given the state of a board, displays the board on the screen
    #  @details Loops through the board_state and calls display_piece to display
    #           the pieces
    #  @param board_state Two dimensional array representing the state of the board
    def display_board(self, board_state, turn):
        self.screen.blit(board_img, (0, 0))
        #Adding pieces
        y = 0
        for col in board_state:
            x = 0
            for row in col:
                self.display_piece(row,x,y)
                x+=1
            y+=1

        if self.start_game == 1:
            #Blur out the board and display the start button
            self.display_start()
            #Display the game mode options when a new game is selected
            self.display_choose_game_mode()
            #Display the game options when a new game is selectd
            self.display_choose_color()
        else:
            #Display the menu options (new game, tutorial)
            self.display_menu()

        #Display the tutorial image if selected
        self.display_tutorial()
        #Display new game countdown if selected
        self.display_newgame()
        #Display the selected piece if any
        self.display_selected(turn)
        #Display valid moves if there are any
        self.display_validMoves()

        pygame.display.update()
    
    def display_start(self):
        self.tutorial = False
        self.screen.blit(black_screen, (720,0))
        self.screen.blit(start_button, (OPTION_COLOR_RED[0], OPTION_COLOR_RED[1] + 100))  
        self.screen.blit(board_img_blurry, (0,0))  

    #Loads the game mode options on screen
    def display_choose_game_mode(self):
        self.screen.blit(title_choose_game_mode, (OPTION_MODE_ONE[0], OPTION_MODE_ONE[1] - 60))
        self.screen.blit(one_players, (OPTION_MODE_ONE))
        self.screen.blit(two_players, (OPTION_MODE_TWO))
        
        #Highlights the option if based on game mode selected
        if self.single_player == 1:
            self.screen.blit(one_players_selected, (OPTION_MODE_ONE))
            self.screen.blit(two_players, (OPTION_MODE_TWO))  
        else:
            self.screen.blit(two_players_selected, (OPTION_MODE_TWO))
            self.screen.blit(one_players, (OPTION_MODE_ONE))       

    #Loads the color options on screen
    def display_choose_color(self):
        self.screen.blit(title_choose_color, (OPTION_COLOR_RED[0], OPTION_COLOR_RED[1] - 60))
        
        #Highlights the option if white or red option is selected
        if self.color_selected == "WHITE":
            self.screen.blit(selected_white, (OPTION_COLOR_WHITE))  
            self.screen.blit(select_red, (OPTION_COLOR_RED)) 
        else: 
            self.screen.blit(selected_red, (OPTION_COLOR_RED))
            self.screen.blit(select_white, (OPTION_COLOR_WHITE))   

    #Highlight the selected piece on board
    def display_selected(self, turn):
        if self.selected:
            if turn == "RED":
                if self.selected[2] == True:
                    self.screen.blit(valid_move, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(red_king, self.calc_pos(self.selected[1], self.selected[0]))
                else:
                    #self.screen.blit(highlighted_red_piece, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(valid_move, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(red_piece, self.calc_pos(self.selected[1], self.selected[0]))
            elif turn == "WHITE":
                if self.selected[2] == True:
                    self.screen.blit(valid_move, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(white_king, self.calc_pos(self.selected[1], self.selected[0]))
                else:
                    #self.screen.blit(highlighted_red_piece, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(valid_move, self.calc_pos(self.selected[1], self.selected[0]))
                    self.screen.blit(white_piece, self.calc_pos(self.selected[1], self.selected[0]))        

    #Reset the selected piece to empty at end of turn
    def reset_selected(self):
        self.selected = []

    #Take in the user's selected piece
    def pass_selected(self, piece):
        self.selected = [piece.row, piece.col]
        self.selected.append(piece.king)

    #Iterate through the valid moves and highlight them on the board
    def display_validMoves(self):
        if self.moves:
            for (row,col) in self.moves.keys():
                self.screen.blit(valid_move, self.calc_pos(col, row))

    #Reset the valid moves dictionary to empty at end of turn
    def reset_validMoves(self):
        self.moves = {}

    #Take in the valid moves for the user's selected piece
    def pass_validMoves(self, moves):
        self.moves = moves

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
                self.screen.blit(red_king, self.calc_pos(row, col))
            else:
                self.screen.blit(red_piece, self.calc_pos(row, col))
        elif colour.color == 'WHITE':
            if colour.king:
                self.screen.blit(white_king, self.calc_pos(row, col))
            else:
                self.screen.blit(white_piece, self.calc_pos(row, col))

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
        elif self.start_game == 0:
            if x > 720 and y <= 70:
                print("New")
                print(x, y)
                return "new"
            elif x > 720 and y >= 80 and y <= 150:
                print("Tutorial")
                print(x, y)
                return "tutorial"
        elif self.start_game == 1:
            if x > OPTION_MODE_ONE[0] and x < OPTION_MODE_TWO[0] and y >= OPTION_MODE_ONE[1] and y <= OPTION_MODE_ONE[1]+35:
                print("1-player mode selected")
                print(x, y)
                return "1-player mode"
            elif x >= OPTION_MODE_TWO[0] and y >= OPTION_MODE_TWO[1] and y <= OPTION_MODE_TWO[1]+35:
                print("2-player mode selected")
                print(x, y)
                return "2-player mode"
            elif x >= OPTION_COLOR_RED[0] and x < OPTION_COLOR_WHITE[0] and y >= OPTION_COLOR_RED[1] and y <= OPTION_COLOR_RED[1]+35:
                print("red selected")
                print(x, y)
                return "red"
            elif x > OPTION_COLOR_WHITE[0] and y >= OPTION_COLOR_WHITE[1] and y <= OPTION_COLOR_WHITE[1]+35:
                print("white selected")
                print(x, y)
                return "white"
            elif x >= OPTION_COLOR_WHITE[0] and y >= OPTION_COLOR_WHITE[1]+100 and y <= OPTION_COLOR_RED[1]+135:
                print("start game selected")
                print(x, y)
                return "start"
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

    def display_tutorial(self):
        if self.tutorial:
            self.screen.blit(tutorial_image, (720,145))
        elif self.start_game == 0 and not self.tutorial:
            self.screen.blit(black_screen, (720,145))
    
    def display_newgame(self):
        if self.new_game == 3:
            self.screen.blit(new_game_countdown_3, (720,650))
            pygame.display.update()
            time.sleep(1)
        elif self.new_game == 2:
            self.screen.blit(new_game_countdown_2, (720,650))
            pygame.display.update()
            time.sleep(1)
        elif self.new_game == 1:
            self.screen.blit(new_game_countdown_1, (720,650))
            pygame.display.update()
            time.sleep(1)
            self.screen.blit(new_game_countdown_0, (720,650))