import pytest
from board import *
from GUI import *
from testBoards import *

class TestBoard2:
    def setup_method(self, method):
        gui = GUI()
        self.board1 = Board(gui,B1)
        self.board2 = Board(gui,B2)
        self.board3 = Board(gui,B1,"WHITE")
        self.board4 = Board(gui,B3)
        self.board5 = Board(gui,B4)
        self.board6 = Board(gui,B5)
        self.board7 = Board(gui,B6)
        self.board8 = Board(gui,B6,"WHITE")
        self.board9 = Board(gui,B7,"WHITE")
        self.board10 = Board(gui,B8)

    #testing that the default turn is red
    def test_constructor(self):
        assert self.board1.turn == "RED"
        assert self.board2.turn == "RED"

    #testing that the boardState and piece arrays are initialized correctly
    def test_setBoard(self):
        for p in self.board1.red_pieces:
            assert p.color == B1[p.row][p.col]
        for p in self.board1.white_pieces:
            assert p.color == B1[p.row][p.col]
        for row in self.board1.boardState:
            for p in row:
                if p != 0:
                    assert p.color == B1[p.row][p.col]

    #test that the turn is changed
    def test_changeTurn(self):
        assert self.board1.turn == "RED"
        self.board1.changeTurn()
        assert self.board1.turn == "WHITE"
        assert self.board3.turn == "WHITE"
        self.board3.changeTurn()
        assert self.board3.turn == "RED"

    #test that the given piece is removed
    def test_remove(self):
        #remove a white piece
        assert self.board1.boardState[0][1] != 0
        assert self.board1.boardState[0][1] in self.board1.white_pieces
        self.board1.remove(self.board1.boardState[0][1])
        assert self.board1.boardState[0][1] == 0
        for p in self.board1.white_pieces:
            assert (p.row,p.col) != (0,1)
        #remove a red piece
        assert self.board1.boardState[7][4] != 0
        assert self.board1.boardState[7][4] in self.board1.red_pieces
        self.board1.remove(self.board1.boardState[7][4])
        assert self.board1.boardState[7][4] == 0
        for p in self.board1.red_pieces:
            assert (p.row,p.col) != (7,4)

    #test that the piece moves and all pieces in skipped are removed
    #test that the piece is kingged when it reaches the opposite end of board
    def test_move(self):
        p1 = self.board4.boardState[1][2]
        p2 = self.board4.boardState[3][4]
        p3 = self.board4.boardState[4][5]
        assert p1.color == "WHITE"
        assert p2.color == "WHITE"
        assert p3.color == "RED"

        self.board4.move(p3,(2,3),[(3,4)])
        assert p1 in self.board4.boardState[1]
        assert p2 not in self.board4.boardState[3]
        assert self.board4.boardState[2][3] == p3
        assert p3.king == False

        self.board4.move(p3,(0,1),[(1,2)])
        assert p1 not in self.board4.boardState[1]
        assert self.board4.boardState[0][1] == p3
        assert p3.king

    #make sure that all valid moves are found
    def test_getValidMoves(self):
        #testing normal piece moves ensuring you can't go off board
        assert self.board1.getValidMoves(self.board1.boardState[5][0]) == {(4,1):[]}
        assert self.board1.getValidMoves(self.board1.boardState[5][4]) == {(4,3):[],(4,5):[]}
        assert self.board1.getValidMoves(self.board1.boardState[2][7]) == {(3,6):[]}
        assert self.board1.getValidMoves(self.board1.boardState[2][3]) == {(3,2):[],(3,4):[]}
        assert self.board1.getValidMoves(self.board1.boardState[1][2]) == {}
        assert self.board1.getValidMoves(self.board1.boardState[6][1]) == {}

        #testing normal piece captures and double captures
        assert self.board5.getValidMoves(self.board5.boardState[1][6]) == {(2,5):[],(2,7):[]}
        assert self.board5.getValidMoves(self.board5.boardState[3][2]) == {(4,1):[],(5,4):[(4,3)]}
        assert self.board5.getValidMoves(self.board5.boardState[3][4]) == {(5,6):[(4,5)],(5,2):[(4,3)],(7,0):[(4,3),(6,1)]}
        assert self.board5.getValidMoves(self.board5.boardState[4][3]) == {(2,1):[(3,2)],(2,5):[(3,4)],(0,7):[(3,4),(1,6)]}
        assert self.board5.getValidMoves(self.board5.boardState[4][5]) == {(3,6):[],(2,3):[(3,4)]}
        assert self.board5.getValidMoves(self.board5.boardState[6][1]) == {(5,0):[],(5,2):[]}

        #testing the king captures to make sure it can go both directions
        self.board5.boardState[3][2].makeKing()
        self.board5.boardState[4][5].makeKing()
        assert self.board5.getValidMoves(self.board5.boardState[3][2]) == {(2,1):[],(2,3):[],(4,1):[],(5,4):[(4,3)],(3,6):[(4,3),(4,5)]}
        assert self.board5.getValidMoves(self.board5.boardState[4][5]) == {(5,4):[],(5,6):[],(3,6):[],(2,3):[(3,4)],(4,1):[(3,4),(3,2)]}

        #making sure not to capture two pieces in a row (must have a space between to double jump)
        #making sure you can't move into a square you already occupy
        assert self.board6.getValidMoves(self.board6.boardState[3][2]) == {(5,4):[(4,3)]}
        assert self.board6.getValidMoves(self.board6.boardState[3][4]) == {(5,6):[(4,5)],(5,2):[(4,3)]}
        assert self.board6.getValidMoves(self.board6.boardState[4][3]) == {(2,1):[(3,2)],(2,5):[(3,4)]}
        assert self.board6.getValidMoves(self.board6.boardState[4][5]) == {(2,3):[(3,4)]}
        self.board6.boardState[3][2].makeKing()
        self.board6.boardState[4][5].makeKing()
        assert self.board6.getValidMoves(self.board6.boardState[3][2]) == {(2,1):[],(2,3):[],(5,4):[(4,3)]}
        assert self.board6.getValidMoves(self.board6.boardState[4][5]) == {(5,4):[],(5,6):[],(2,3):[(3,4)]}

    #given a position test to see if the game is over
    def test_checkGameEnd(self):
        #check that game ends when all white pieces are captured
        assert self.board7.checkGameEnd() == False
        self.board7.move(self.board7.boardState[3][2],(1,4),[(2,3)])
        assert self.board7.checkGameEnd()
        assert self.board7.winner == "RED"

        #check that game ends when all red pieces are captured
        assert self.board8.checkGameEnd() == False
        self.board8.move(self.board8.boardState[2][3],(4,1),[(3,2)])
        assert self.board8.checkGameEnd()
        assert self.board8.winner == "WHITE"

        #check that if white runs out of moves then red wins
        #but if that piece has squares for a king to move then the game continues
        assert self.board9.checkGameEnd()
        assert self.board9.winner == "RED"
        self.board9.boardState[2][1].makeKing()
        assert self.board9.checkGameEnd() == False

        #check that if red runs out of moves then white wins
        #but if that piece has squares for a king to move then the game continues
        assert self.board10.checkGameEnd()
        assert self.board10.winner == "WHITE"
        self.board10.boardState[5][6].makeKing()
        assert self.board10.checkGameEnd() == False

    def teardown_method(self, method):
        self.board1 = None
        self.board2 = None
        self.board3 = None
        self.board4 = None
        self.board5 = None
        self.board6 = None
        self.board7 = None
        self.board8 = None
        self.board9 = None
        self.board10 = None
