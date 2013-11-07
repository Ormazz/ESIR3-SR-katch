from gui import updatable

class DisplayManager(updatable.Updatable):

	_updatables = []

	def add(self, updatable):
		self._updatables.append(updatable)

	def update(self):
		for updatable in self._updatables:
			updatable.update()


