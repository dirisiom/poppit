import pygame as pg
from src.elements.element import Element
from src.loader import Loader

SPARTY_SIZE = (120, 200)
SPARTY_POS = (65, 650)


class Narrator(Element):
    def __init__(self, cache: Loader, *groups):
        """
        Initialize a new Narrator instance.

        Args:
            *groups (pg.sprite.Group): Groups to which the narrator belongs.
        """
        super().__init__(cache.get_narrator(), SPARTY_SIZE, SPARTY_POS, *groups)
