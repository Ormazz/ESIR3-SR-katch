import pygame
from gui import updatable

class Entity(updatable.Updatable):

    _sprite = None
    _screen = None

    _x = None
    _y = None
    _next_image = None

    def init(self, screen, image, x, y):
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
        tmp_image = self._sprite.image
        self._sprite.image = self._next_image
        self._next_image = tmp_image

        self._sprite.rect = self._sprite.image.get_rect()
        self._sprite.rect.topleft = [self._x, self._y]

        self._screen.blit(self._sprite.image, self._sprite.rect)
