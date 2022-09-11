import unittest
import slider
from pynput.keyboard import Key

class SliderUnitTest():
    def __init__(self):
        pass

    def test_getkpos(self):
        # Test that getpos() correctly finds the cursor
        pass

    def test_movement(self):
        # Test whether each of the movment functions move the cursor as intended
        # Test that range-checking works (ie. doesnt move if cursor is on the edge of a board) 
        pass
    
    def test_boardgen(self):
        # Tests board size, dimentions. Does the board generate 
        pass

    def test_handle_keypress(self):
        # Test that tha keyboard input callback function correctly handles inputs
        pass

    def test_check_win(self):
        # Test that game correctly checks for win condition (and that the win condition is correctly generated) 
        pass


if __name__ == "__main__":
    pass