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
    def __init__(self, color, *groups, pos=(50, 50)):
        """
        Initialize a new Balloon instance.

        Args:
            color (Color): The color of the balloon.
            *groups (pg.sprite.Group): Groups to which the balloon belongs.
            pos (tuple): The initial position of the balloon.
        """
        super().__init__(f"src/assets/balloons/{color.name}.png", (25, 35), pos, *groups)
        self.color = color

