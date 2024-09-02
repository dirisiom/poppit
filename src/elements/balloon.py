import pygame as pg
from src.elements.element import Element
from enum import Enum

class Color(Enum):
    red = 1
    blue = 2
    green = 3
    purple = 4
    pink = 5


# noinspection PyCompatibility
class Balloon(Element):
    def __init__(self, color, index, img_size=(25, 35), *groups):
        """
        Initialize a new Balloon instance.

        Args:
            color (Color): The color of the balloon.
            *groups (pg.sprite.Group): Groups to which the balloon belongs.
            pos (tuple): The initial position of the balloon.
        """
        super().__init__(f"src/assets/balloons/{color.name}.png", img_size, *groups, pos=(0,0))
        self.color = color
        self.index = index
        self.set_index(index)

    def set_index(self, index):
        self.index = index
        # calculate the position from the index
        self.pos = pg.math.Vector2((120 + self.index[1] * 50, 50 + self.index[0] * 50))
        self.rect = self.image.get_rect(center=self.pos)

    def move_up(self, spaces):
        if spaces == 0:
            return
        self.set_index((self.index[0] - spaces, self.index[1]))

