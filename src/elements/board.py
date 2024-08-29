import pygame as pg
import random
from src.elements.balloon import Balloon, Color

# define constants for num of balloons in a row (15) and num in a column (10)
ROW_LEN = 15  # num of columns
COL_LEN = 10  # num of rows

# "game board" that contains all the balloons, as well as powerups (Eventually)
def create_balloon(pos):
    return Balloon(random.choice(list(Color)), pos=pos)

class Board:
    def __init__(self):
        self.table = []
        self.gifts = set()

        position = (120, 50)
        for i in range(COL_LEN):
            self.table.append([])
            for j in range(ROW_LEN):
                self.table[i].append(create_balloon(position))
                position = (position[0] + 50, position[1])
            position = (120, position[1] + 50)

        for i in range(15):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 14)
                if (x, y) not in self.gifts:
                    self.gifts.add((x, y))
                    break


    def draw(self, screen):
        for row in self.table:
            for balloon in row:
                balloon.draw(screen)

