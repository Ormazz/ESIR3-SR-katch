import pygame
from connection import connectionManager
from gui import updatable
from gui import gui_control

class Players_layout(updatable.Updatable,gui_control.Gui_control, object):

    screen = None

    def __init__(self, screen):
        self.screen = screen
        self.draw("Players", 16, screen.get_width() - 114, 10)


    def draw(self, text, size, x, y):
        font = pygame.font.SysFont("Arial", size)
        label = font.render(text, 1, (0, 0, 0))
        self.screen.blit(label, (x, y))

    def clean_list(self):
        pygame.draw.rect(self.screen, pygame.Color("white"), pygame.Rect(self.screen.get_width() - 135, 0, 320, 460))

    def update(self):
        if self._katch.players_has_changed() is True:
            self.clean_list()
            self.draw("Players", 16, self.screen.get_width() - 114, 10)
            y = 40
            for p in self._katch.get_players():
                self.draw(p._ip + "   " + str(p.score), 14, self.screen.get_width() - 150, y)
                y += 20
            self._katch.visit_players(True)