import pygame
from gui import updatable

class Message(updatable.Updatable):

    _screen = None
    _sprite = None
    _x = 0
    _y = 0

    _next_image = None

    def __init__(self, screen, image, x ,y):
        self._screen = screen
        self._sprite = pygame.sprite.Sprite()

        surface = pygame.image.load(image).convert()
        surface.set_colorkey(pygame.Color(0,0,0,0))
        self._sprite.image = surface.subsurface((0,0, 200, 53))
        self._next_image = surface.subsurface(200, 0, 200, 53)
        self._sprite.rect = self._sprite.image.get_rect()
        self._screen = screen
        self._sprite.rect.topleft = [x, y]
        self._x = x
        self._y = y

    def update(self):
        tmp_image = self._sprite.image
        self._sprite.image = self._next_image
        self._next_image = tmp_image

        self._sprite.rect = self._sprite.image.get_rect()
        self._sprite.rect.topleft = [self._x, self._y]

        self._screen.blit(self._sprite.image, self._sprite.rect)
