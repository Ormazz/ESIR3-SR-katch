from abc import ABCMeta, abstractmethod
from control import katch

class GuiControl(metaclass=ABCMeta):

	_katch = katch.Katch()