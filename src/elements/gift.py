import pygame as pg

from src.elements.element import Element

class Gift(Element):
    def __init__(self, pos, target, cache, *groups):
        """
        Initialize a new Gift instance.

        Args:
            *groups (pg.sprite.Group): Groups to which the gift belongs.
        """
        super().__init__(cache.get_gift("teddy.png"), (50, 50), pos=pos, *groups)
        self.move_towards(target)
        self.done = False


    def update(self):
        if not self.done:
            super().update()
        # eventually, this will make the gift float down a little slowly and oscillate back and forth like a parachute

    def stop(self):
        super().stop()
        self.done = True