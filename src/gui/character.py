from gui import entity

class Character(entity.Entity):
    """Players display in the game. Has two positions to simulate a walking move.

    Members :
        * ip : id used to identify the player
        * sprite : picture of the character
        * screen : game display
        * x : lateral position, from left
        * y : vertical position, from top
        * next_image : picture to display at the next update
        * surface : map where the characters are positioned
        * scope : size of the character (heigth and width)
        * up/down/left/righ_img : PyGame wants them to be updated at each update (WORK IN PROGRESS)
    """

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
        """Set the character's image"""
        # Only one of these paragraph should be used if PyGame worked properly
        self._down_img.append(surface.subsurface((0,0, 23, 23)))
        self._down_img.append(surface.subsurface((23,0, 23, 23)))

        self._up_img.append(surface.subsurface((46,0, 23, 23)))
        self._up_img.append(surface.subsurface((69,0, 23, 23)))

        self._left_img.append(surface.subsurface((92,0, 23, 23)))
        self._left_img.append(surface.subsurface((115,0, 23, 23)))

        self._right_img.append(surface.subsurface((138,0, 23, 23)))
        self._right_img.append(surface.subsurface((161,0, 23, 23)))

    def up(self):
        """Changes the orientation of the character"""
        self._sprite.image = self._surface.subsurface((46,0, 23, 23))
        self._next_image = self._surface.subsurface((69,0, 23, 23))
        self.set_position(self._x, self._y - self._scope)

    def down(self):
        """Changes the orientation of the character"""
        self._sprite.image = self._surface.subsurface((0,0, 23, 23))
        self._next_image = self._surface.subsurface((23,0, 23, 23))
        self.set_position(self._x, self._y + self._scope)

    def left(self):
        """Changes the orientation of the character"""
        self._sprite.image = self._surface.subsurface((92,0, 23, 23))
        self._next_image = self._surface.subsurface((115,0, 23, 23))
        self.set_position(self._x - self._scope, self._y)

    def right(self):
        """Changes the orientation of the character"""
        self._sprite.image = self._surface.subsurface((138,0, 23, 23))
        self._next_image = self._surface.subsurface((161,0, 23, 23))
        self.set_position(self._x + self._scope, self._y)

    def set_position(self, x=-1, y=-1):
        """Set the character position in the map"""
        if x != -1:
            self._x = x
        if y != -1:
            self._y = y
        self._sprite.rect.topleft = [self._x, self._y]
