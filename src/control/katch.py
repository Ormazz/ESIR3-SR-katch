from model import game_state
from model import player

class Katch:

    instance = None
    _game_state = None
    _connection_Manager = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
            my_class._game_state = game_state.Game_state()
        return my_class.instance

    def add_player(self, ip):
        new_player = player.Player(ip)
        self._game_state.add_player(new_player)

    def connection_to_peer(self, ip):
        self._connection_Manager.connection_to_peer(ip)

    def visit_players(self):
        self._game_state._players_visited = True

    def players_has_changed(self):
        return not self._game_state._players_visited

    def get_players(self):
        return self._game_state._players

    def get_player(self, ip):
        return self._game_state.get_player(ip)