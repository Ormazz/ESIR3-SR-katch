import pygame
from connection import connectionManager

class Players_layout:

    screen = None

    def __init__(self, screen):
        self.screen = screen
        self.draw("Players", 16, 1113, 10)


    def draw(self, text, size, x, y):
        font = pygame.font.SysFont("Arial", size)
        label = font.render(text, 1, (0, 0, 0))
        self.screen.blit(label, (x, y))

    def update(self):

        print(connectionManager.ConnectionManager()._has_new_ip)
        if connectionManager.ConnectionManager()._has_new_ip is True:
            ip_list = connectionManager.ConnectionManager()._ip_list
            y = 40
            for ip in ip_list:
                self.draw(ip, 14, 1100, y)
                y += 10
            connectionManager.ConnectionManager()._has_new_ip = False