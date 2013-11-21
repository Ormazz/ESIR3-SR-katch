class Player:

    _x = 0
    _y = 0
    score = 0
    _ip = None

    _scope = 23

    _UP = 0
    _DOWN = 1
    _LEFT = 2
    _RIGHT = 3

    def __init__(self, ip):
        self._ip = ip

    def move(self, direction):
        if direction == Player._UP:
            self._y = self._y - self._scope
        elif direction == Player._DOWN:
            self._y = self._y + self._scope
        elif direction == Player._RIGHT:
            self._x = self._x + self._scope
        elif direction == Player._LEFT:
            self._x = self._x - self._scope