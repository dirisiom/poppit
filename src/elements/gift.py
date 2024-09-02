import pygame as pg

from src.elements.element import Element

class Gift(Element):
    def __init__(self, pos, *groups):
        """
        Initialize a new Gift instance.

        Args:
            *groups (pg.sprite.Group): Groups to which the gift belongs.
        """
        super().__init__("src/assets/gifts/duck.jpg", (50, 50), (0, 0), *groups)
        self.pos = pg.math.Vector2((50, 50))
        self.rect = self.image.get_rect(center=self.pos)

    def set_pos(self, pos):
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)