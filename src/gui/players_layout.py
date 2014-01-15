import pygame
from gui import updatable
import threading

class PlayersLayout(updatable.Updatable, object):
    """Layout were players are displayed"""

    screen = None
    _players_score = {}

    _condition = threading.Condition()

    def __init__(self, screen):
        self.screen = screen

    def draw(self, text, size, x, y):
        font = pygame.font.SysFont("Arial", size)
        label = font.render(text, 1, (0, 0, 0))
        self.screen.blit(label, (x, y))

    def clean_list(self):
        pygame.draw.rect(self.screen, pygame.Color("white"), pygame.Rect(self.screen.get_width() - 200, 0, 420, 460))

    def remove_player(self, ip):
        with self._condition:
            del self._players_score[ip]

    def set_score_player(self, ip, score):
        with self._condition:
            self._players_score[ip] = score

    def incr_score_player(self, ip):
        with self._condition:
            if ip in self._players_score:
                self._players_score[ip] = self._players_score[ip] + 1
            else:
                self._players_score[ip] = 0

    def update(self):
        with self._condition:
            self.clean_list()
            self.draw("Players", 16, self.screen.get_width() - 185, 10)
            y = 40
            for p in self._players_score:
                self.draw(p + "   " + str(self._players_score[p]), 14, self.screen.get_width() - 190, y)
                y += 20


    # def update(self):
    #     if self._katch.players_has_changed() is True:
    #         self.clean_list()
    #         self.draw("Players", 16, self.screen.get_width() - 185, 10)
    #         y = 40
    #         for p in self._katch.get_players():
    #             self.draw(p._ip + "   " + str(p.score), 14, self.screen.get_width() - 190, y)
    #             y += 20
    #         self._katch.visit_players(True)
