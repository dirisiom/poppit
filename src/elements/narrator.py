import pygame as pg
from src.elements.element import Element


class Narrator(Element):
    def __init__(self, *groups):
        """
        Initialize a new Narrator instance.

        Args:
            *groups (pg.sprite.Group): Groups to which the narrator belongs.
        """
        super().__init__("src/assets/sparty.png", (120, 200), (65, 650), *groups)
