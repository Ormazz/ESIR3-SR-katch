class Player:

    _x = 0
    _y = 0
    _score = 0
    _ip = None

    _scope = 10

    _up = 0
    _down = 1
    _left = 2
    _right = 3

    def __init__(self, ip):
        self._ip = ip

    def move(self, direction):
        if direction == self._up:
            self._y = self._y - self._scope
        elif direction == self._down:
            self._y = self._y + self._scope
        elif direction == self._right:
            self._x == self._x + self._scope
        elif direction == self._left:
            self._x == self._x - self._scope