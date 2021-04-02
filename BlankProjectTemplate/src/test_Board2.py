import pytest
from board2 import *
from GUI2 import *
from testBoards import *

class TestBoard2:
    def setup_method(self, method):
        gui = GUI()
        self.board1 = Board(gui,B1,"RED")
        self.board2 = Board(gui,B2,"RED")
        self.board3 = Board(gui,B3,"WHITE")

    def test_getDimensionsOfFace(self):
        pass

    def teardown_method(self, method):
        self.board1 = None
        self.board2 = None
        self.board3 = None
