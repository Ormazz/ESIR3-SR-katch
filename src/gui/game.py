import pygame
import inputbox
from connection import connectionManager

class Game(object):

    _display_input_box = True

    def main(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1067, 600))
        background = pygame.image.load('../../img/background.jpe')
        sprites = pygame.sprite.Group()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            sprites.update(dt / 1000.)
            screen.blit(background, (0, 0))
            self.create_input_ip(screen)
            sprites.draw(screen)
            pygame.display.flip()

    def create_input_ip(self, screen):
        if self._display_input_box:
            ip = inputbox.ask(screen, "IP to connect")
            connectionManager.ConnectionManager().connection_to_peer(ip)
            self._display_input_box = False

Game().main()