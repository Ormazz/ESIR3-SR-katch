import math
import random

class CollectableStack(object):

    _game_state = None
    _connection_manager = None
    _collectable_manager = None

    def __init__(self, game_state, connection_manager, collectable_manager):
        self._game_state = game_state
        self._connection_manager = connection_manager
        self._collectable_manager = collectable_manager

    def activate_collectable(self, ip):
        #Get the spiders of the other player
        #Set the matrice and create the spiders on the players screen
        matrice = self._connection_manager.get_collectables(ip)
        self.create_collectable(matrice)
        self._collectable_manager.set_started(True)

    def check_wizard_collectable(self, wizard):
        x = math.ceil(wizard._x / 23)
        y = math.ceil(wizard._y / 23)
        if self._game_state.wizard_on_collectable(x, y):
            self._connection_manager.remove_collectable(x, y)
            self.remove_collectable(self._connection_manager.get_ip_serv(), x, y)

            if self._game_state.get_nb_coll() == 0:
                self._connection_manager.wizard_finish_game()
                self.finish_game()

    def remove_collectable(self, ip, x, y):
        self._game_state.incr_score_player(ip)
        self._game_state.set_players_visited(False)
        self._game_state.remove_collectable(x, y)
        self._collectable_manager.remove_collectable(x * 23, y * 23)

    def generate_collectable(self):
        matrice = self._game_state.get_matrice()
        for i in range(0, 10):
            x = math.ceil(random.random() * 19)
            y = math.ceil(random.random() * 19)

            if matrice[x][y]:
                i = i - 1
            else:
                self._game_state.add_collectable(x,y)

    def create_collectable(self, matrice):
        #Set the new matrice
        self._game_state.set_matrice(matrice)

        #Taught on the matrice and create collectable
        for x in range(0, len(matrice)):
            for y in range(0, len(matrice[x])):
                if matrice[x][y]:
                    self._collectable_manager.create_collectable(x*23, y*23)
