from multiprocessing import Manager

class Game_state:

	_players_visited = True
	_players = []
	_collectables = []

	_manager = Manager()
	_matrice = _manager.list([[False for i in range(20)] for j in range(20)])

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

	def add_collectable(self, x, y):
		if self._matrice[x][y]:
			return False
		else:
			self._edit_matrice_value(x,y,True)
			return True

	def remove_collectable(self, x, y):
		self._edit_matrice_value(x,y,False)

	def wizard_on_collectable(self, x, y):
		return self._matrice[x][y]

	def set_matrice(self, matrice):
		self._matrice = self._manager.list(matrice)
		print("Set matrice")
		self.pretty_print_matrice()

	def get_matrice(self):
		print("Get matrice")
		self.pretty_print_matrice()
		return list(self._matrice)

	def get_player(self, ip):
		pl = [p for p in self._players if p._ip == ip]
		return pl[0]

	def pretty_print_matrice(self):
		finish = False
		for x in range(0, len(self._matrice)):
			for y in range(0, len(self._matrice[0])):
				if self._matrice[x][y]:
					print("Molololololololo " + str(x) + " " + str(y))
					finish = True
					pass

			if finish:
				pass