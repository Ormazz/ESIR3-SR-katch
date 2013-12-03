from gui import updatable
from gui import collectable

class CollectableManager(updatable.Updatable):
	"""
	Contains the collectables on the game display. Collectables are represented by dancing spiders with a neat fez.

	Members :
		* collectables : list of the remaining collectables
		* id : id for the next collectable
		* started : indicates if the collectable should be displayed or not
		* screen : game display
	"""

	_collectables = []
	_id = 0
	_started = False
	_screen = None

	def __init__(self, screen):
		self._screen = screen

	def create_collectable(self, x, y):
		"""Put a new collectable in the list, with x and y as position"""
		self._collectables.append(collectable.Collectable(self._screen, "../img/spider.png", x, y, id))
		self._id = self._id + 1

	def remove_collectable(self, x, y):
		"""Remove the collectable identified by its position"""
		for coll in self._collectables:
			if coll._x == x and coll._y == y:
				self._collectables.remove(coll)
				break

	def update(self):
		"""Update the collectables' picture."""
		for coll in self._collectables:
			coll.update()

	def get_started(self):
		return self._started

	def set_started(self, started):
		self._started = started