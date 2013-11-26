from model import game_state
from model import player
import pygame
import math
import random

class Katch(object):

    instance = None
    _game_state = None
    _connection_manager = None
    _player_manager = None
    _display_manager = None
    _collectable_manager = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
            my_class._game_state = game_state.Game_state()
        return my_class.instance

    def init(self, connection_manager, player_manager, display_manager, collectable_manager):
        self._player_manager = player_manager
        self._connection_manager = connection_manager
        self._display_manager = display_manager
        new_player = player.Player(connection_manager._ip_serv)
        new_player._x = 0
        new_player._y = 0
        self._game_state.add_player(new_player)
        self._collectable_manager = collectable_manager

        self.generate_collectable()

    def add_player(self, ip):
        new_player = player.Player(ip)
        inf = self._connection_manager.get_player_information(ip)
        new_player._x = inf[0]
        new_player._y = inf[1]
        new_player.score = inf[2]
        self._game_state.add_player(new_player)
        self._player_manager.create_player(inf[0], inf[1], ip)
        if not self._player_manager._started:
            self.activate_player(self._connection_manager._ip_serv)
            self._display_manager.disabled_input_box()

            if not self._collectable_manager.get_started():
                self.create_collectable(self.get_collectable())
                self._collectable_manager.set_started(True)

    def activate_collectable(self, ip):
        matrice = self._connection_manager.get_collectables(ip)
        self.create_collectable(matrice)
        self._collectable_manager.set_started(True)

    def connection_to_peer(self, ip):
        self.activate_collectable(ip)
        self._connection_manager.connection_to_peer(ip)
    #    self.activate_player(self._connection_manager._ip_serv)

    def activate_player(self, ip):
        self._player_manager.activate_player(0, 0, ip)

    def visit_players(self, visit):
        self._game_state.set_players_visited(visit)

    def players_has_changed(self):
        return not self._game_state._players_visited

    def get_players(self):
        return self._game_state._players

    def get_player(self, ip):
        return self._game_state.get_player(ip)

    def move_player(self, ip, direction):
        player = self.get_player(ip)
        character = self._player_manager.get_player(ip)
        if direction == player._DOWN:
            player.move(player._DOWN)
            character.down()
        if direction == player._UP:
            player.move(player._UP)
            character.up()
        if direction == player._LEFT:
            player.move(player._LEFT)
            character.left()
        if direction == player._RIGHT:
            player.move(player._RIGHT)
            character.right()

    def move_wizard(self, event):
        if self._player_manager._started :
            if self._player_manager.wizard_can_move(event.key):
                player = self.get_player(self._connection_manager._ip_serv)
                position = player.get_position()
                if event.key == pygame.K_DOWN and position[1] + 1 < game_state.MAP_HEIGTH:
                    self._connection_manager.move_wizard(player._DOWN)
                    player.move(player._DOWN)
                    self._player_manager.wizard.down()
                    self.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_UP and position[1] > 0:
                    self._connection_manager.move_wizard(player._UP)
                    player.move(player._UP)
                    self._player_manager.wizard.up()
                    self.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_LEFT and position[0] > 0:
                    self._connection_manager.move_wizard(player._LEFT)
                    player.move(player._LEFT)
                    self._player_manager.wizard.left()
                    self.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_RIGHT and position[0] + 1 < game_state.MAP_WIDTH:
                    self._connection_manager.move_wizard(player._RIGHT)
                    player.move(player._RIGHT)
                    self._player_manager.wizard.right()
                    self.check_wizard_collectable(self._player_manager.wizard)

    def check_wizard_collectable(self, wizard):
        x = math.ceil(wizard._x / 23)
        y = math.ceil(wizard._y / 23)
        if game_state.Game_state().wizard_on_collectable(x, y):
            self._connection_manager.remove_collectable(x, y)
            self.remove_collectable(self._connection_manager._ip_serv, x, y)

            if game_state.Game_state().get_nb_coll() == 0:
                self._connection_manager.wizard_finish_game()
                self.finish_game()

    def remove_collectable(self, ip, x, y):
        game_state.Game_state().incr_score_player(ip)
        self._game_state.set_players_visited(False)
        game_state.Game_state().remove_collectable(x, y)
        self._collectable_manager.remove_collectable(x * 23, y * 23)

    def get_collectable(self):
        return game_state.Game_state().get_matrice()

    def create_collectable(self, matrice):
        game_state.Game_state().set_matrice(matrice)
        for x in range(0, len(matrice)):
            for y in range(0, len(matrice[x])):
                if matrice[x][y]:
                    self._collectable_manager.create_collectable(x*23, y*23)

    def generate_collectable(self):
        gs = game_state.Game_state()
        matrice = gs.get_matrice()
        for i in range(0, 10):
            x = math.ceil(random.random() * 19)
            y = math.ceil(random.random() * 19)

            if matrice[x][y]:
                i = i - 1
            else:
                gs.add_collectable(x,y)

    def leave(self):
        """Local exit method ; Alert the other players that we are not connected anymore"""
        if self._player_manager._started:
            self._connection_manager.leave()

    def remove_player(self,ip):
        """Remove a player that has left the game"""

        # Removing from the model
        self._game_state.remove_player(self._game_state.get_player(ip))
        # Removing from the interface
        self._player_manager.remove_player(ip)

    def finish_game(self):
        self._player_manager.deactivate_player()
        self._display_manager.launch_fireworks()