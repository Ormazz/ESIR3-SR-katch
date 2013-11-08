import pygame
from gui import updatable

class Character(updatable.Updatable):

    _surface = None
    _sprite = None
    _screen = None
    _x = None
    _y = None
    _current_image = None
    _next_image = None

    def __init__(self, screen, image, x, y):
        self._sprite = pygame.sprite.Sprite()
        surface = pygame.image.load(image).convert()
        self._surface = surface
        surface.set_colorkey(pygame.Color(255,0,255,0))
        self._sprite.image = surface.subsurface((0,0, 23, 23))
        self._current_image = self._sprite.image
        self._next_image = surface.subsurface((23,0, 23, 23))
        self._sprite.rect = self._sprite.image.get_rect()
        self._screen = screen
        self._sprite.rect.topleft = [x, y]
        self._x = x
        self._y = y

    def update(self):
        self._current_image = self._next_image
        self._next_image = self._sprite.image
        self._sprite.image = self._current_image
        self._sprite.rect = self._sprite.image.get_rect()
        self._sprite.rect.topleft = [self._x, self._y]

        self._screen.blit(self._sprite.image, self._sprite.rect)

    def up(self):
        self._sprite.image = self._surface.subsurface((46,0, 23, 23))
        self._current_image = self._sprite.image
        self._next_image = self._surface.subsurface((69,0, 23, 23))

        self._sprite.rect.topleft = [self._x, self._y-10]
        self._y -= 10

    def down(self):
        self._sprite.image = self._surface.subsurface((0,0, 23, 23))
        self._current_image = self._sprite.image
        self._next_image = self._surface.subsurface((23,0, 23, 23))

        self._sprite.rect.topleft = [self._x, self._y+10]
        self._y += 10

    def left(self):
        self._sprite.image = self._surface.subsurface((92,0, 23, 23))
        self._current_image = self._sprite.image
        self._next_image = self._surface.subsurface((115,0, 23, 23))

        self._sprite.rect.topleft = [self._x-10, self._y]
        self._x -= 10

    def right(self):
        self._sprite.image = self._surface.subsurface((0,0, 23, 23))
        self._current_image = self._sprite.image
        self._next_image = self._surface.subsurface((23,0, 23, 23))

        self._sprite.rect.topleft = [self._x+10, self._y]
        self._x += 10


