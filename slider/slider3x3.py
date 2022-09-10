import random
# from shutil import move
from pynput.keyboard import Key, Listener
# from sqlite3 import Row
# from tkinter import N


class Slider:
    def __init__(self):
        self.pop = None
        self.gamestate = None
        self.width = 3
        self.height = 3
        self.row_pos = None
        self.col_pos = None
        self.win = False
        self.moves = 0
        self.generate_gamestate()
        self.getpos()

    def generate_gamestate(self):
        self.pop = list(range(1, self.width * self.height))
        self.pop.append('*')
        random.shuffle(self.pop)
        self.gamestate = []
        for row in range(self.height):
            i = row*self.width
            val = self.pop[i:(i+self.width)]
            self.gamestate.append(val)
            
        print(self.gamestate)

    def generate_board(self):
        print("")
        for row in range(self.height):
            row_str = ""
            for col in range(self.width):
                row_str += " | " + str(self.gamestate[row][col])
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

    def handle_keypress(self, input):
        moved = False
        match input:
            case Key.esc:
                return False
            case Key.up:
                moved = self.moveup()
            case Key.down:
                moved = self.movedown()
            case Key.left:
                moved = self.moveleft()
            case Key.right:
                moved = self.moveright()
        if moved:
            self.moves += 1
        return True
            

    def checkrange(self, num, type=None):
        if type == 'width' or type == 'w':
            return num >= 0 and num < self.width
        elif type == 'height' or type == 'h':
            return num >= 0 and num < self.width
        else:
            raise ValueError("type must be 'width', 'w', 'height', or 'h'")

    def checkwin(self):
        pass 

    def getpos(self):
        for row in range(self.height):
            for col in range(self.width):
                if(self.gamestate[row][col] == '*'):
                    self.row_pos = row
                    self.col_pos = col

    def gameloop(self, input):
        if input != None:
            ret = self.handle_keypress(input)
        self.generate_board()
        self.checkwin()
        return ret


c = Slider()
with Listener(on_press=c.gameloop) as listener:
    listener.join()
    while c.win != True:
        pass
    
    listener.stop()





#     c.scan_input()

# print(c.row_pos, c.col_pos)
# c.generate_board()
# c.moveleft()
# print()
# print(c.row_pos, c.col_pos)
# c.generate_board()
