import pygame
from gui import entity

class Character(entity.Entity):

    _ip = None
    _sprite = None
    _screen = None
    _x = None
    _y = None
    _next_image = None
    _surface = None

    _scope = 23

    _up_img = []
    _down_img = []
    _left_img = []
    _right_img = []

    def __init__(self, screen, image, x, y, ip):
        self._ip = ip
        self.init(screen, image, x, y)

    def create_image(self, surface):
        self._down_img.append(surface.subsurface((0,0, 23, 23)))
        self._down_img.append(surface.subsurface((23,0, 23, 23)))

        self._up_img.append(surface.subsurface((46,0, 23, 23)))
        self._up_img.append(surface.subsurface((69,0, 23, 23)))

        self._left_img.append(surface.subsurface((92,0, 23, 23)))
        self._left_img.append(surface.subsurface((115,0, 23, 23)))

        self._right_img.append(surface.subsurface((138,0, 23, 23)))
        self._right_img.append(surface.subsurface((161,0, 23, 23)))

    def up(self):
        self._sprite.image = self._surface.subsurface((46,0, 23, 23))
        self._next_image = self._surface.subsurface((69,0, 23, 23))
        self.set_position(self._x, self._y - self._scope)

    def down(self):
        self._sprite.image = self._surface.subsurface((0,0, 23, 23))
        self._next_image = self._surface.subsurface((23,0, 23, 23))
        self.set_position(self._x, self._y + self._scope)

    def left(self):
        self._sprite.image = self._surface.subsurface((92,0, 23, 23))
        self._next_image = self._surface.subsurface((115,0, 23, 23))
        self.set_position(self._x - self._scope, self._y)

    def right(self):
        self._sprite.image = self._surface.subsurface((138,0, 23, 23))
        self._next_image = self._surface.subsurface((161,0, 23, 23))
        self.set_position(self._x + self._scope, self._y)

    def set_position(self, x=-1, y=-1):
        if x != -1:
            self._x = x
        if y != -1:
            self._y = y
        self._sprite.rect.topleft = [self._x, self._y]
