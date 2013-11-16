from model import game_state
from model import player
import pygame

class Katch:

    instance = None
    _game_state = None
    _connection_manager = None
    _player_manager = None
    _display_manager = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
            my_class._game_state = game_state.Game_state()
        return my_class.instance

    def init(self, connection_manager, player_manager, display_manager):
        self._player_manager = player_manager
        self._connection_manager = connection_manager
        self._display_manager = display_manager
        new_player = player.Player(connection_manager._ip_serv)
        new_player._x = 0
        new_player._y = 0
        self._game_state.add_player(new_player)

    def add_player(self, ip):
        new_player = player.Player(ip)
        position = self._connection_manager.get_player_position(ip)
        new_player._x = position[0]
        new_player._y = position[1]
        self._game_state.add_player(new_player)
        self._player_manager.create_player(position[0], position[1], ip)
        if not self._player_manager._started:
            self.activate_player(self._connection_manager._ip_serv)
            self._display_manager.disabled_input_box()

    def connection_to_peer(self, ip):
        self._connection_manager.connection_to_peer(ip)
        self.activate_player(self._connection_manager._ip_serv)

    def activate_player(self, ip):
        self._player_manager.activate_player(0, 0, ip)

    def visit_players(self):
        self._game_state._players_visited = True

    def players_has_changed(self):
        return not self._game_state._players_visited

    def get_players(self):
        return self._game_state._players

    def get_player(self, ip):
        return self._game_state.get_player(ip)

    def move_player(self, ip, direction):
        player = self.get_player(ip)
        character = self._player_manager.get_player(îp)
        if direction == player.Player._DOWN:
            player.move(player.Player._DOWN)
            character.down()
        if direction == player.Player._UP:
            player.move(player.Player._UP)
            character.up()
        if direction == player.Player._LEFT:
            player.move(player.Player._LEFt)
            self._player_manager.wizard.left()
            character.left()
        if direction == player.Player._RIGHT:
            player.move(player.Player._RIGHT)
            self._player_manager.wizard.right()
            character.right()


    def move_wizard(self, event):
        if self._player_manager._started :
            player = self.get_player(self._connection_manager._ip_serv)
            if event.key == pygame.K_DOWN:
                self._connection_manager.move_wizard(player.Player._DOWN)
                player.move(player.Player._DOWN)
                self._player_manager.wizard.down()
            if event.key == pygame.K_UP:
                self._connection_manager.move_wizard(player.Player._UP)
                player.move(player.Player._UP)
                self._player_manager.wizard.up()
            if event.key == pygame.K_LEFT:
                self._connection_manager.move_wizard(player.Player._LEFT)
                player.move(player.Player._LEFT)
                self._player_manager.wizard.left()
            if event.key == pygame.K_RIGHT:
                self._connection_manager.move_wizard(player.Player._RIGHT)
                player.move(player.Player._RIGHT)
                self._player_manager.wizard.right()
