from gui import updatable
import pygame

class Fireworks(updatable.Updatable):
    """A purple ball moving up until exploding."""

    _screen = None
    _sprite = None
    _surface = None
    _x = 0
    _y = 0

    _boom = False
    _mega_boom = False
    _end = False

    _need_err = True

    def __init__(self, screen, image, x, y):
        self._screen = screen

        self._sprite = pygame.sprite.Sprite()
        surface = pygame.image.load(image).convert()
        self._surface = surface

        surface.set_colorkey(pygame.Color(0,0,0,0))

        self._sprite.image = surface.subsurface((0,0, 8, 14))

        self._sprite.rect = self._sprite.image.get_rect()
        self._screen = screen
        self._sprite.rect.topleft = [x, y]
        self._x = x
        self._y = y

    def update(self):
        if not self._end:
            if self._end:
                self._sprite.image = self._surface.subsurface((78,0, 30, 21))
            elif self._mega_boom:
                self._sprite.image = self._surface.subsurface((46,0, 34, 34))
                self._end = True
            elif self._boom:
                self.correct_path()
                self._sprite.image = self._surface.subsurface((18,0, 28, 28))
                self._mega_boom = True
            elif self._y < 50:
                self._sprite.image = self._surface.subsurface((8,0, 10, 15))
                self._boom = True
            else:
                self._y = self._y - 10

            self._sprite.rect.topleft = [self._x, self._y]
            self._screen.blit(self._sprite.image, self._sprite.rect)

    def correct_path(self):
        self._x = self._x - 10