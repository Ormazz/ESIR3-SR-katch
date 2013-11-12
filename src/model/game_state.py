class Game_state:

	_players_visited = True
	_players = []
	_collectables = []

	def add_player(self, player):
		self._players.append(player)
		self._players_visited = False

	def remove_player(self, player):
		self._players.remove(player)
		self._players_visited = False

	def add_collectable(self, collectable):
		self._collectables.append(collectable)

	def remove_collectable(self, collectable):
		self._collectables.remove(collectable)

	def get_player(self, ip):
		ip = [p for p in self._players if p._ip == ip]
		return ip[0]