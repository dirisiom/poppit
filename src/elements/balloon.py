import pygame as pg
from enum import Enum

class Color(Enum):
    red = 1
    blue = 2
    green = 3
    purple = 4
    pink = 5



class Balloon(pg.sprite.Sprite):
    def __init__(self, color, *groups, pos=(50, 50)):
        """
        Initialize a new Balloon instance.

        Args:
            color (Color): The color of the balloon.
            *groups (pg.sprite.Group): Groups to which the balloon belongs.
            pos (tuple): The initial position of the balloon.
        """
        pg.sprite.Sprite.__init__(self, *groups)
        img = pg.image.load(f"src/assets/balloons/{color.name}.png")
        self.image = pg.transform.scale(img.subsurface(img.get_bounding_rect()), (25, 35))
        self.rect = self.image.get_rect(center=pos)
        self.speed = pg.math.Vector2(0, 0)
        self.pos = pg.math.Vector2(pos)
        self.color = color

    def update(self):
        """
        Update the balloon's position based on its speed.
        """
        self.pos += self.speed
        self.rect.center = self.pos

    def draw(self, screen):
        """
        Draw the balloon on the screen.

        Args:
            screen (pg.Surface): The surface on which to draw the balloon.
        """
        screen.blit(self.image, self.rect)

    def move_towards(self, target):
        """
        Move the balloon towards a target position.

        Args:
            target (pg.math.Vector2): The target position to move towards.
        """
        direction = target - self.pos
        self.speed = direction.normalize() * 2

    def stop(self):
        """
        Stop the balloon's movement.
        """
        self.speed = pg.math.Vector2(0, 0)