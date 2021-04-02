import pytest
from pieces2 import *

#most of the logic for valid moves will be tested in the board2 class
#here we are simply testing that the piece method fuction as expected
class TestPieces2:
    def setup_method(self, method):
        self.piece1 = piece(0, 1, "WHITE", 1, king = False)
        self.piece2 = piece(5, 4, "RED", -1, king = False)
        self.piece3 = piece(6, 5, "RED", -1, king = True)

    def test_constructor(self):
        #testing constructor for the first piece
        assert self.piece1.row == 0
        assert self.piece1.col == 1
        assert self.piece1.color == "WHITE"
        assert self.piece1.king == False
        assert self.piece1.direction == 1
        #testing constructor for the third piece
        assert self.piece3.row == 6
        assert self.piece3.col == 5
        assert self.piece3.color == "RED"
        assert self.piece3.king == True
        assert self.piece3.direction == -1

    def test_makeKing(self):
        #testing makeKing for the first piece
        assert self.piece1.king == False
        self.piece1.makeKing()
        assert self.piece1.king == True
        #testing makeKing for the first piece
        assert self.piece2.king == False
        self.piece2.makeKing()
        assert self.piece2.king == True


    def test_move(self):
        assert self.piece1.row == 0
        assert self.piece1.col == 1
        self.piece1.move(4,5)
        assert self.piece1.row == 4
        assert self.piece1.col == 5

    def teardown_method(self, method):
        self.piece1 = None
        self.piece2 = None
        self.piece3 = None
