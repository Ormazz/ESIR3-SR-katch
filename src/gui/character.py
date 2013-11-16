import pygame
from gui import updatable

class Character(updatable.Updatable):

    _ip = None
    _sprite = None
    _screen = None
    _x = None
    _y = None
    _next_image = None
    _surface = None

    _up_img = []
    _down_img = []
    _left_img = []
    _right_img = []

    def __init__(self, screen, image, x, y, ip):
        self._ip = ip
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

    def create_image(self, surface):
        self._down_img.append(surface.subsurface((0,0, 23, 23)))
        self._down_img.append(surface.subsurface((23,0, 23, 23)))

        self._up_img.append(surface.subsurface((46,0, 23, 23)))
        self._up_img.append(surface.subsurface((69,0, 23, 23)))

        self._left_img.append(surface.subsurface((92,0, 23, 23)))
        self._left_img.append(surface.subsurface((115,0, 23, 23)))

        self._right_img.append(surface.subsurface((138,0, 23, 23)))
        self._right_img.append(surface.subsurface((161,0, 23, 23)))

    def update(self):
        tmp_image = self._sprite.image
        self._sprite.image = self._next_image
        self._next_image = tmp_image

        self._sprite.rect = self._sprite.image.get_rect()
        self._sprite.rect.topleft = [self._x, self._y]

        self._screen.blit(self._sprite.image, self._sprite.rect)

    def up(self):
        print("UP " + self._ip)
        self._sprite.image = self._surface.subsurface((46,0, 23, 23))
        self._next_image = self._surface.subsurface((69,0, 23, 23))
        self.set_position(self._x, self._y - 10)

    def down(self):
        print("DOWN " + self._ip)
        self._sprite.image = self._surface.subsurface((0,0, 23, 23))
        self._next_image = self._surface.subsurface((23,0, 23, 23))
        self.set_position(self._x, self._y + 10)

    def left(self):
        print("LEFT " + self._ip)
        self._sprite.image = self._surface.subsurface((92,0, 23, 23))
        self._next_image = self._surface.subsurface((115,0, 23, 23))
        self.set_position(self._x - 10, self._y)

    def right(self):
        print("RIGHT " + self._ip)
        self._sprite.image = self._surface.subsurface((138,0, 23, 23))
        self._next_image = self._surface.subsurface((161,0, 23, 23))
        self.set_position(self._x + 10, self._y)

    def set_position(self, x=-1, y=-1):
        if x != -1:
            self._x = x
        if y != -1:
            self._y = y
        self._sprite.rect.topleft = [self._x, self._y]
