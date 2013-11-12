from abc import ABCMeta, abstractmethod
from control import katch

class Gui_control(metaclass=ABCMeta):

	_katch = katch.Katch()