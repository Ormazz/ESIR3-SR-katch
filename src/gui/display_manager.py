from gui import updatable
from gui import fireworks

class DisplayManager(updatable.Updatable):
    """
    Manages the display of the game of the user screen. Is mostly responsible of the window

    Members :
        * screen : game display zone
        * updatables : entities that have to be updated every seconds
        * input_box : zone that allows to the user to write the ip he wants to connect to
    """

    _screen = None
    _updatables = []
    _input_box = None

    def __init__(self, screen):
        self._screen = screen

    def add(self, updatable):
        """ Adds an updatable entity"""
        self._updatables.append(updatable)

    def disabled_input_box(self):
        """Removes the input box"""
        self._input_box._display = False

    def launch_fireworks(self):
        """Shows pretty fireworks for the end of the game"""
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 25, 460))
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 100, 460))
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 175, 460))
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 250, 460))
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 325, 460))
        self.add(fireworks.Fireworks(self._screen, "../img/fireworks.png", 400, 460))

    def update(self):
        """Update all the updatable entities"""
        for updatable in self._updatables:
            updatable.update()
