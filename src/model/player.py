import math

class Player(object):

    _x = 0
    _y = 0
    _ip = None

    score = 0

    _scope = 23

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, ip):
        self._ip = ip

    def move(self, direction):
        if direction == Player.UP:
            self._y = self._y - self._scope
        elif direction == Player.DOWN:
            self._y = self._y + self._scope
        elif direction == Player.RIGHT:
            self._x = self._x + self._scope
        elif direction == Player.LEFT:
            self._x = self._x - self._scope

    def get_position(self):
        return (math.ceil(self._x / self._scope), math.ceil(self._y / self._scope))
