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

    started = False
    _players = []
    _wizard_ip = None
    _screen = None
    _players_layout = None

    def __init__(self, screen, _players_layout):
        self._screen = screen
        self._players_layout = _players_layout

    def event(self, event):
        """Reacts to a given event"""
        # As you can see, there not many event the game possibly can react
        self._katch.move_wizard(event)

    def update(self):
        """Updates the players in the game"""
        if self.started:
            # Then the others
            for player in self._players:
                player.update()

    def deactivate_player(self):
        """At the end of the game, removes the players from the display"""
        self.started = False    # It's that simple ; the gui will do the rest

    def activate_player(self, x, y, ip):
        """Insert the local player in the display"""
        self._players.append(character.Character(self._screen, "../img/wizard.png", x, y, ip))
        self._wizard_ip = ip
        self._players[len(self._players) - 1].set_position(x, y)
        self.started = True
        self.set_score_player(ip, 0)

    def create_player(self, x, y, ip, score):
        """Create a new player"""

        self._players.append(character.Character(self._screen, "../img/player.png", x, y, ip))
        self.set_score_player(ip, score)

    def set_score_player(self, ip, score):
        self._players_layout.set_score_player(ip, score)

    def incr_score_player(self, ip):
        self._players_layout.incr_score_player(ip)

    def wizard_can_move(self, direction):
        """Tells if the local player collides with another player if he goes in that direction. If this is the case, he won't move."""
        wizard = self.get_player(self._wizard_ip)
        # Read the current position
        old_x = wizard._x
        old_y = wizard._y
        # Move the wizard, just to try
        self.wizard_position(wizard, direction)

        result = True
        # Now, where are the other players ?
        for p in self._players:
            if p._ip != self._wizard_ip:
                if p._x == wizard._x and p._y == wizard._y:
                    # One seems to be at the same spot than us! This is wrong.
                    result = False
                    break

        # The wizard go back to its old position ; nothing happened (yet)
        wizard.set_position(old_x, old_y)
        return result

    def wizard_position(self, wizard, direction):
        """Moves the wizard one case in the given direction"""
        if direction == pygame.K_UP:
            wizard.set_position(wizard._x, wizard._y - wizard._scope)
        elif direction == pygame.K_DOWN:
            wizard.set_position(wizard._x, wizard._y + wizard._scope)
        elif direction == pygame.K_LEFT:
            wizard.set_position(wizard._x - wizard._scope, wizard._y)
        elif direction == pygame.K_RIGHT:
            wizard.set_position(wizard._x + wizard._scope, wizard._y)

    def get_player(self, ip):
        """Returns a player, identified by its ip"""
        for p in self._players:
            if p._ip == ip:
                return p

    def remove_player(self, ip):
        """Remove a player from the GUI"""
        player = self.get_player(ip)
        self._players.remove(player)
        self._players_layout.remove_player(ip)

    def get_started(self):
        return self.started

