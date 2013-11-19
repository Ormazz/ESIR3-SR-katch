class Game_state:

	_players_visited = True
	_players = []
	_collectables = []

	_matrice = [ [False for i in range(0, 20)] for j in range(0, 20)]

	def set_players_visited(self, visited):
		self._players_visited = visited

	def add_player(self, player):
		self._players.append(player)
		self._players_visited = False

	def remove_player(self, player):
		self._players.remove(player)
		self._players_visited = False

	def add_collectable(self, x, y):
		if self._matrice[x][y]:
			return False
		else:
			self._matrice[x][y] = True
			return True

	def remove_collectable(self, x, y):
		self._matrice[x][y] = False

	def wizard_on_collectable(self, x, y):
		return self._matrice[x][y]

	def set_matrice(self, matrice):
		self._matrice = matrice

	def get_matrice(self):
		return self._matrice

	def get_player(self, ip):
		pl = [p for p in self._players if p._ip == ip]
		return pl[0]
