from model import game_state
from model import player

class Katch:

    instance = None
    _game_state = None
    _connection_manager = None
    _player_manager = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
            my_class._game_state = game_state.Game_state()
        return my_class.instance

    def init(self, connection_manager, player_manager):
        self._player_manager = player_manager
        self._connection_manager = connection_manager
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
        self._player_manager.create_player(position[0], position[1])

    def connection_to_peer(self, ip):
        self._connection_manager.connection_to_peer(ip)

    def visit_players(self):
        self._game_state._players_visited = True

    def players_has_changed(self):
        return not self._game_state._players_visited

    def get_players(self):
        return self._game_state._players

    def get_player(self, ip):
        return self._game_state.get_player(ip)