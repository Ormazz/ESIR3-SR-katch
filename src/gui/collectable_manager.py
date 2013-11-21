from gui import updatable
from gui import gui_control
from gui import collectable

class Collectable_manager(updatable.Updatable):

	_collectables = []
	_id = 0
	_started = False
	_screen = None

	def __init__(self, screen):
		self._screen = screen

	def create_collectable(self, x, y):
		self._collectables.append(collectable.Collectable(self._screen, "../img/spider.png", x, y, id))
		self._id = self._id + 1

	def remove_collectable(self, x, y):
		for coll in self._collectables:
			if coll._x == x and coll._y == y:
				self._collectables.remove(coll)
				break

	def update(self):
		for coll in self._collectables:
			coll.update()

	def get_started(self):
		return self._started

	def set_started(self, started):
		self._started = started