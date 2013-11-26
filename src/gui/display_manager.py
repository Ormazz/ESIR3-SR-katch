from gui import updatable
from gui import fireworks

class DisplayManager(updatable.Updatable):

	_screen = None
	_updatables = []
	_input_box = None

	def __init__(self, screen):
		self._screen = screen

	def add(self, updatable):
		self._updatables.append(updatable)

	def disabled_input_box(self):
		self._input_box._display = False

	def launch_fireworks(self):
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 25, 460))
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 100, 460))
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 175, 460))
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 250, 460))
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 325, 460))
		self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 400, 460))

	def update(self):
		for updatable in self._updatables:
			updatable.update()