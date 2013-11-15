import pygame
from gui import character
from gui import updatable
from gui import gui_control

class Player_manager(updatable.Updatable, gui_control.Gui_control):

    _wizard = None
    _started = False
    _players = []
    _screen = None

    def __init__(self, screen):
        self._screen = screen

    def event(self, event):
        if self._started:
            if event.key == pygame.K_DOWN:
                self._wizard.down()
            if event.key == pygame.K_UP:
                self._wizard.up()
            if event.key == pygame.K_LEFT:
                self._wizardleft()
            if event.key == pygame.K_RIGHT:
                self._wizard.right()

    def update(self):
        if self._started:
            self._wizard.update()

        for player in self._players:
            player.update()

    def activate_player(self, x, y):
        self._wizard = character.Character(self._screen, "../img/wizard.png", x, y)
        self._wizard.set_position(x, y)
        self._started = True

    def create_player(self, x, y):
        self._players.append(character.Character(self._screen, "../img/player.png", x, y))