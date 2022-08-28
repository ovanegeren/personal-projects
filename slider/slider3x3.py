import random


class Slider:
    def __init__(self):
        self.pop = [0, 1, 2, 3, 4, 5, 6, 7, 8, '*']
        self.gamestate = []
        pass
        
    def generate_gamestate(self):
        self.gamestate = random.sample(self.pop, len(self.pop))
        print(self.gamestate)

    # def print_game():


c = Slider()
c.generate_gamestate()




