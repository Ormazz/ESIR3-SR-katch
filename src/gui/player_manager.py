import pygame
from gui import character
from gui import updatable
from gui import gui_control

class PlayerManager(updatable.Updatable, gui_control.GuiControl):
    """Manages the player on the game display. Players are represented as magicians.
    The local player is white like the moon, whereas the other players are red like fire.

    Members :
        * wizard : the local player
        * started : the player are not displayed until this value is on True
        * players : list of other players
        * screen : game display
    """

    wizard = None
    started = False
    _players = []
    _screen = None

    def __init__(self, screen):
        self._screen = screen

    def event(self, event):
        """Reacts to a given event"""
        # As you can see, there not many event the game possibly can react
        self._katch.move_wizard(event)

    def update(self):
        """Updates the players in the game"""
        if self.started:
            # First the local player
            self.wizard.update()
            # Then the others
            for player in self._players:
                player.update()

    def deactivate_player(self):
        """At the end of the game, removes the players from the display"""
        self.started = False    # It's that simple ; the gui will do the rest

    def activate_player(self, x, y, ip):
        """Insert the local player in the display"""
        self.wizard = character.Character(self._screen, "../img/wizard.png", x, y, ip)
        self.wizard.set_position(x, y)
        self.started = True

    def create_player(self, x, y, ip):
        """Create a new player"""
        self._players.append(character.Character(self._screen, "../img/player.png", x, y, ip))

    def wizard_can_move(self, direction):
        """Tells if the local player collides with another player if he goes in that direction. If this is the case, he won't move."""
        # Read the current position
        old_x = self.wizard._x
        old_y = self.wizard._y
        # Move the wizard, just to try
        self.wizard_position(direction)

        result = True
        # Now, where are the other players ?
        for p in self._players:
            if p._x == self.wizard._x and p._y == self.wizard._y:
                # One seems to be at the same spot than us! This is wrong.
                result = False
                break

        # The wizard go back to its old position ; nothing happened (yet)
        self.wizard.set_position(old_x, old_y)
        return result

    def wizard_position(self, direction):
        """Moves the wizard one case in the given direction"""
        if direction == pygame.K_UP:
            self.wizard.set_position(self.wizard._x, self.wizard._y - self.wizard._scope)
        elif direction == pygame.K_DOWN:
            self.wizard.set_position(self.wizard._x, self.wizard._y + self.wizard._scope)
        elif direction == pygame.K_LEFT:
            self.wizard.set_position(self.wizard._x - self.wizard._scope, self.wizard._y)
        elif direction == pygame.K_RIGHT:
            self.wizard.set_position(self.wizard._x + self.wizard._scope, self.wizard._y)

    def get_player(self, ip):
        """Returns a player, identified by its ip"""
        for p in self._players:
            if p._ip == ip:
                return p

    def remove_player(self, ip):
        """Remove a player from the GUI"""
        player = self.get_player(ip)
        self._players.remove(player)

    def get_started(self):
        return self.started

