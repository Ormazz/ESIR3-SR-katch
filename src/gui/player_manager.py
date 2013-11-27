import pygame
from gui import character
from gui import updatable
from gui import gui_control

class PlayerManager(updatable.Updatable, gui_control.GuiControl):

    wizard = None
    started = False
    _players = []
    _screen = None

    def __init__(self, screen):
        self._screen = screen

    def event(self, event):
        self._katch.move_wizard(event)

    def update(self):
        if self.started:
            self.wizard.update()
            for player in self._players:
                player.update()

    def deactivate_player(self):
        self.started = False

    def activate_player(self, x, y, ip):
        self.wizard = character.Character(self._screen, "../img/wizard.png", x, y, ip)
        self.wizard.set_position(x, y)
        self.started = True

    def create_player(self, x, y, ip):
        self._players.append(character.Character(self._screen, "../img/player.png", x, y, ip))

    def wizard_can_move(self, direction):
        old_x = self.wizard._x
        old_y = self.wizard._y
        self.wizard_position(direction)

        result = True
        for p in self._players:
            if p._x == self.wizard._x and p._y == self.wizard._y:
                result = False
                break
        self.wizard.set_position(old_x, old_y)
        return result

    def wizard_position(self, direction):
        if direction == pygame.K_UP:
            self.wizard.set_position(self.wizard._x, self.wizard._y - self.wizard._scope)
        elif direction == pygame.K_DOWN:
            self.wizard.set_position(self.wizard._x, self.wizard._y + self.wizard._scope)
        elif direction == pygame.K_LEFT:
            self.wizard.set_position(self.wizard._x - self.wizard._scope, self.wizard._y)
        elif direction == pygame.K_RIGHT:
            self.wizard.set_position(self.wizard._x + self.wizard._scope, self.wizard._y)

    def get_player(self, ip):
        for p in self._players:
            if p._ip == ip:
                return p

    def remove_player(self, ip):
        """Remove a player from the GUI"""
        player = self.get_player(ip)
        self._players.remove(player)

    def get_started(self):
        return self.started

