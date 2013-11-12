import pygame
from gui import character
from gui import updatable

class Player_manager(updatable.Updatable):

    _wizard = None
    _started = False
    _players = []

    def __init__(self, screen):
        self._wizard = character.Character(screen, "../img/wizard.png", 0, 0)

    def event(self, event):
        if self._started:
            if event.key == pygame.K_DOWN:
                self._wizard.down()
            if event.key == pygame.K_UP:
                self._wizard.up()
            if event.key == pygame.K_LEFT:
                self._wizard.left()
            if event.key == pygame.K_RIGHT:
                self._wizard.right()

    def update(self):
        if self._started:
            self._wizard.update()

    def activate_player(self, x, y):
        self._wizard.set_position(x, y)
        self._started = True