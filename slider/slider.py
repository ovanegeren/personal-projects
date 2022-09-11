import random
# from shutil import move
from pynput.keyboard import Key, Listener
# from sqlite3 import Row
# from tkinter import N


class Slider:
    def __init__(self):
        # variables related to game structure and generation
        self.pop = None
        self.win_condition = None
        self.gamestate = None
        self.width = 4
        self.height = 4

        # row/column position of cursor (note: when accessing gamestate use format [row][col] due to how gamestate is formatted)
        self.row_pos = None
        self.col_pos = None

        # variables containng game stats
        self.win = False
        self.game_over = False
        self.moves = 0
        self.generate_gamestate()
        self.getpos()
        self.generate_board()

    def generate_gamestate(self):
        self.pop = list(range(1, self.width * self.height))
        self.pop.append('*')
        self.win_condition = self.format_pop()               # easier to store game winning condition on initialization than sorting a mixed type list later
        print(self.win_condition)
        random.shuffle(self.pop)
        print(self.win_condition)
        self.gamestate = self.format_pop()
        print(self.gamestate)

    def format_pop(self):                       # created a function thats formats self.pop into a list because i need to do it twice
        out = []
        for row in range(self.height):
            i = row*self.width
            val = self.pop[i:(i+self.width)]
            out.append(val)
        return out

    def generate_board(self):
        print("")
        for row in range(self.height):
            row_str = ""
            for col in range(self.width):
                num = self.gamestate[row][col]
                row_str += " | " + str(num)
                try:                            # will always throw type error for '*' character
                    if (num <= 9 ) and ((self.width * self.height - 1) > 9): 
                        row_str += " "
                except TypeError:
                    if ((self.width * self.height - 1) > 9):
                        row_str += " "
            row_str += " | "
            print(row_str)
    

    def moveup(self):
        row = self.row_pos - 1
        if self.checkrange(row, 'h'):
            num = self.gamestate[row][self.col_pos]
            self.gamestate[row][self.col_pos] = self.gamestate[self.row_pos][self.col_pos]
            self.gamestate[self.row_pos][self.col_pos] = num
            self.row_pos = row
            return True
        return False

    def movedown(self):
        row = self.row_pos + 1
        if self.checkrange(row, 'h'):
            num = self.gamestate[row][self.col_pos]
            self.gamestate[row][self.col_pos] = self.gamestate[self.row_pos][self.col_pos]
            self.gamestate[self.row_pos][self.col_pos] = num
            self.row_pos = row
            return True
        return False        

    def moveleft(self):
        col = self.col_pos - 1
        if self.checkrange(col, 'h'):
            num = self.gamestate[self.row_pos][col]
            self.gamestate[self.row_pos][col] = self.gamestate[self.row_pos][self.col_pos]
            self.gamestate[self.row_pos][self.col_pos] = num
            self.col_pos = col

    def moveright(self):
        col = self.col_pos + 1
        if self.checkrange(col, 'h'):
            num = self.gamestate[self.row_pos][col]
            self.gamestate[self.row_pos][col] = self.gamestate[self.row_pos][self.col_pos]
            self.gamestate[self.row_pos][self.col_pos] = num
            self.col_pos = col

    def cheat(self):
        self.game_over = True
        self.win = True

    def handle_keypress(self, input):
        moved = False
        match input:
            case Key.esc:
                self.game_over = True
            case Key.up:
                moved = self.moveup()
            case Key.down:
                moved = self.movedown()
            case Key.left:
                moved = self.moveleft()
            case Key.right:
                moved = self.moveright()
            case Key.caps_lock:
                print("Cheater!")
                self.cheat()

        if moved:
            self.moves += 1
            

    def checkrange(self, num, type=None):
        if (type == 'width') or (type == 'w'):
            return num >= 0 and num < self.width
        elif (type == 'height') or (type == 'h'):
            return num >= 0 and num < self.width
        else:
            raise ValueError("type must be 'width', 'w', 'height', or 'h'")

    def checkwin(self):
        if self.gamestate == self.win_condition:
            self.win = True
            self.game_over = True
            return True
        else:
            return False

    def getpos(self):
        for row in range(self.height):
            for col in range(self.width):
                if(self.gamestate[row][col] == '*'):
                    self.row_pos = row
                    self.col_pos = col

    def gameloop(self, input):
        self.handle_keypress(input)
        self.generate_board()
        self.checkwin()
        # print(self.win_condition)
        # print(self.gamestate)
        return not self.game_over               # Return True (ie. "keep listening to keyboard") as long as game is not over               


c = Slider()
with Listener(on_press=c.gameloop) as listener:
    listener.join()         # listener is blocking, must be ended through c.gameloop

    # check for victory upon completion of a game
    if c.win:
        print("You won! You finished in ", c.moves, " moves.")
    else:
        print("Game Over.")





#     c.scan_input()

# print(c.row_pos, c.col_pos)
# c.generate_board()
# c.moveleft()
# print()
# print(c.row_pos, c.col_pos)
# c.generate_board()
