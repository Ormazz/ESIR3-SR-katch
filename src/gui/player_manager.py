import pygame
from gui import character
from gui import updatable
from gui import gui_control

class Player_manager(updatable.Updatable, gui_control.Gui_control):

    wizard = None
    _started = False
    _players = []
    _screen = None

    def __init__(self, screen):
        self._screen = screen

    def event(self, event):
        _katch.move_wizard(event)

    def update(self):
        if self._started:
            self.wizard.update()

        for player in self._players:
            player.update()

    def activate_player(self, x, y, ip):
        self.wizard = character.Character(self._screen, "../img/wizard.png", x, y, ip)
        self.wizard.set_position(x, y)
        self._started = True

    def create_player(self, x, y, ip):
        self._players.append(character.Character(self._screen, "../img/player.png", x, y, ip))

    def get_player(self, ip):
        pl = [p for p in self._players if p._ip == ip]
        return pl[0]

