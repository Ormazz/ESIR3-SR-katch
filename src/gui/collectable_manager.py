from gui import updatable
from gui import gui_control

class Collectable_manager(updatable.Updatable):

	_collectables = []
	_id = 0
	_started = False

	def create_collectable(self, x, y):
		_collectables(collectable.Collectable(self._screen, "../img/spider.png", x, y, id))
		id = id + 1

	def remove_collectable(self, x, y):
		for coll in collectables:
			if coll._x == x and coll._y == y:
				_collectables.remove(coll)
				pass

	def update(self):
		for coll in self._collectables:
			coll.update()

	def get_started(self):
		return self._started

	def set_started(self, started):
		self._started = started