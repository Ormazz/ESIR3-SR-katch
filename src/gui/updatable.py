from abc import ABCMeta, abstractmethod

class Updatable(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass