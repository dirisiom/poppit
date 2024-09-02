import pygame as pg
# make element a subclass of pygame.sprite.Sprite for other current elements to inherit from
class Element(pg.sprite.Sprite):
    def __init__(self, img_path, img_size, pos, *groups):
        """
        Initialize a new Element instance.

        Args:
            *groups (pg.sprite.Group): Groups to which the element belongs.
        """
        pg.sprite.Sprite.__init__(self, *groups)
        img = pg.image.load(img_path)
        self.image = pg.transform.scale(img.subsurface(img.get_bounding_rect()), img_size)
        self.pos = pg.math.Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = pg.math.Vector2(0, 0)
        self.destination = None

    def update(self):
        """
        Update the element's position based on its speed.
        """
        self.pos += self.speed
        self.rect.center = self.pos
        # stop if destination is reached
        # check if the current location is beyond the destination, with the logic depending on the speed
        if self.destination:
            if self.speed.x > 0 and self.pos.x >= self.destination.x:
                self.pos = self.destination
                self.stop()
            elif self.speed.x < 0 and self.pos.x <= self.destination.x:
                self.pos = self.destination
                self.stop()
            elif self.speed.y > 0 and self.pos.y >= self.destination.y:
                self.pos = self.destination
                self.stop()
            elif self.speed.y < 0 and self.pos.y <= self.destination.y:
                self.pos = self.destination
                self.stop()

    def draw(self, screen):
        """
        Draw the element on the screen.

        Args:
            screen (pg.Surface): The surface on which to draw the element.
        """
        screen.blit(self.image, self.rect)

    def move_towards(self, target):
        """
        Move the element towards a target position.

        Args:
            target (pg.math.Vector2): The target position to move towards.
        """
        if target == self.pos:
            return
        self.destination = target
        direction = target - self.pos
        self.speed = direction.normalize()

    def stop(self):
        """
        Stop the element's movement.
        """
        self.speed = pg.math.Vector2(0, 0)
        self.destination = None