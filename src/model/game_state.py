from multiprocessing import Manager

MAP_WIDTH = 20
MAP_HEIGTH = 20

class GameState(object):

	_players_visited = True
	_players = []
	_collectables = []

	_manager = Manager()
	_matrice = _manager.list([[False for i in range(MAP_WIDTH)] for j in range(MAP_HEIGTH)])
	_nb_coll = _manager.Value('i', 10)

	def _edit_matrice_value(self,x,y,value):
		# We have to separe the line to synchronize the matrice
		x_line = self._matrice[x]
		x_line[y] = value
		self._matrice[x] = x_line

	def set_players_visited(self, visited):
		self._players_visited = visited

	def add_player(self, player):
		self._players.append(player)
		self._players_visited = False

	def remove_player(self, player):
		self._players.remove(player)
		self._players_visited = False

	def incr_score_player(self, ip):
		player = self.get_player(ip)
		player.score = player.score + 1

	def add_collectable(self, x, y):
		if self._matrice[x][y]:
			return False
		else:
			self._edit_matrice_value(x,y,True)
			return True

	def remove_collectable(self, x, y):
		self._nb_coll.value = self._nb_coll.value - 1
		self._edit_matrice_value(x,y,False)

	def wizard_on_collectable(self, x, y):
		return self._matrice[x][y]

	def set_matrice(self, matrice):
		for x in range(len(self._matrice)):
			self._matrice[x] = matrice[x]
		self.calculate_coll()

	def calculate_coll(self):
		nb = 0
		for x in range(0, len(self._matrice)):
			for y in range(0, len(self._matrice[0])):
				if self._matrice[x][y]:
					nb = nb + 1

		self._nb_coll.value = nb

	def get_matrice(self):
		return list(self._matrice)

	def get_player(self, ip):
		pl = [p for p in self._players if p._ip == ip]
		return pl[0]

	def pretty_print_matrice(self):
		finish = False
		for x in range(0, len(self._matrice)):
			for y in range(0, len(self._matrice[0])):
				if self._matrice[x][y]:
					finish = True
					pass

			if finish:
				pass

	def get_nb_coll(self):
		return self._nb_coll.value