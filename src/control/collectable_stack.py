import math
import random

class CollectableStack(object):
    """Control of the collectables. Count them, decides if one is taken, and keep scores.

    Members :
        * game_state : information about the status of the game_state
        * connection_manager : manages the communication with other players
        * collectable_manager : responsible of the collectables in the GUI
        * katch : main control
    """

    _game_state = None
    _connection_manager = None
    _collectable_manager = None
    _katch = None

    def __init__(self, game_state, connection_manager, collectable_manager, katch):
        self._game_state = game_state
        self._connection_manager = connection_manager
        self._collectable_manager = collectable_manager
        self._katch = katch

    def activate_collectable(self, ip):
        """Get the spiders from another other players.
        Sets the matrix and creates the spiders on the players screen."""
        matrix = self._connection_manager.get_collectables(ip)
        self.create_collectable(matrix)
        self._collectable_manager.set_started(True)

    def check_wizard_collectable(self, wizard):
        """Checks if the wizard is on a collectable, and thus has the right to take it."""
        # Translation of the wizard's position into matrix coordinates
        x = math.ceil(wizard._x / 23)
        y = math.ceil(wizard._y / 23)

        # If the wizard is on a collecable
        if self._game_state.wizard_on_collectable(x, y):
            # We remove the collectable both from our session and other player's one
            self._connection_manager.remove_collectable(x, y)
            self.remove_collectable(self._connection_manager.get_ip_serv(), x, y)

            # If there are no collectable remaining
            if self._game_state.get_nb_coll() == 0:
                # We indicates to other players that the game is finished
                self._connection_manager.wizard_finish_game()
                # And we go to the end
                self._katch.finish_game()

    def remove_collectable(self, ip, x, y):
        """Register a collectable taken by a player (identified by its ip), on a given position"""
        # The player obtain one point
        self._game_state.incr_score_player(ip)
        # The gui has to update scores
        self._game_state.set_players_visited(False)
        # Removing the collectable from the model and the gui
        self._game_state.remove_collectable(x, y)
        self._collectable_manager.remove_collectable(x * 23, y * 23)

    def generate_collectable(self):
        """Randomly places 10 collectables in the matrix."""
        matrix = self._game_state.get_matrix()
        for i in range(0, 10):
            x = math.ceil(random.random() * 19)
            y = math.ceil(random.random() * 19)

            if matrix[x][y]:
                # If there is already a collectable here, we have to place the current one elsewhere
                i = i - 1
            else:
                self._game_state.add_collectable(x,y)

    def create_collectable(self, matrix):
        """Put collectables in the game from another matrix"""
        #Set the new matrix
        self._game_state.set_matrix(matrix)

        #Taught on the matrix and create collectable in the gui
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                if matrix[x][y]:
                    self._collectable_manager.create_collectable(x*23, y*23)