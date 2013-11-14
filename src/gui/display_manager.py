from gui import updatable

class DisplayManager(updatable.Updatable):

	_updatables = []
	_input_box = None

	def add(self, updatable):
		self._updatables.append(updatable)

	def disabled_input_box(self):
		self._input_box._display = False

	def update(self):
		for updatable in self._updatables:
			updatable.update()


