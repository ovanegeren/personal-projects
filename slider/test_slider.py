import unittest
import slider
from pynput.keyboard import Key

class SliderTestSuite(unittest.TestCase):
    def __init__(self, test_width, test_height):
        super(SliderTestSuite, self).__init__()
        self.s = slider.Slider(test_width, test_height)
        pass

    def test_getpos(self):
        ### Test that getpos() correctly finds the cursor
        self.s.getpos()
        self.assertTrue(self.s.gamestate[self.s.row_pos][self.s.col_pos] == '*')
        pass

    def test_movement(self):
        ### Test whether each of the movment functions move the cursor as intended
        ### Test that range-checking works (ie. doesnt move if cursor is on the edge of a board) 
        self.test_getpos()                                          # movement test depends on get_pos to find correct cursor position
        # self.s.gamestate
        pass
    
    def test_boardgen(self):
        ### Tests board size, dimentions, and generation of win condition
        self.assertEqual(self.s.height * self.s.width, len(self.s.pop))         # Are there enough elements to fit the dimensions?
        # self.assertEqual(len(self.s.win_condition), len(self.s.gamestate))      # (imprefect) are the win condition and gamestate the same dimensions?
        self.assertEqual(self.s.height, len(self.s.gamestate))        # verify height, then use it to iterate
        for row in range(self.s.height):
            self.assertEqual(self.s.width, len(self.s.gamestate[row]))
            # self.assertEqual(len(self.s.win_condition[row]), len(self.s.gamestate[row]))
        pass

    def test_handle_keypress(self):
        
        ### Test that tha keyboard input callback function correctly handles inputs
        pass

    def test_check_win(self):
        ### Test that game correctly checks for win condition (and that the win condition is correctly generated)
        ### assumption: a randomly generated game will not result in a win
        self.s.generate_gamestate()
        self.s.get_pos()
        self.assertFalse(self.s.checkwin())
        
        pass


if __name__ == "__main__":
    t = SliderTestSuite(4,4)
    # t.test_boardgen()
    t.test_getpos()
    pass