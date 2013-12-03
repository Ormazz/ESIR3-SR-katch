import pygame
from gui import updatable

class Entity(updatable.Updatable):
    """Each object in the game is an entity. It has a sprite, and an animation of two frames.

    Members :
        * sprite : picture representing currently the entity
        * screen : display zone where the entity is printed
        * x, y : position
        * next_image : picture to print on the next update
    """

    _sprite = None
    _screen = None

    _x = None
    _y = None
    _next_image = None

    def init(self, screen, image, x, y):
        """Set the entity attributes, and print it in the game display"""
        self._sprite = pygame.sprite.Sprite()
        surface = pygame.image.load(image).convert()
        self._surface = surface
        surface.set_colorkey(pygame.Color(255,0,255,0))

        #self.create_image(surface)

        self._sprite.image = surface.subsurface((0,0, 23, 23))
        self._next_image = surface.subsurface((23,0, 23, 23))

        self._sprite.rect = self._sprite.image.get_rect()
        self._screen = screen
        self._sprite.rect.topleft = [x, y]
        self._x = x
        self._y = y


    def update(self):
        """Switch to the next picture for the animation"""
        tmp_image = self._sprite.image
        self._sprite.image = self._next_image
        self._next_image = tmp_image

        self._sprite.rect = self._sprite.image.get_rect()
        self._sprite.rect.topleft = [self._x, self._y]

        self._screen.blit(self._sprite.image, self._sprite.rect)
