import pygame
from gui import inputbox
from gui import players_layout
from connection import connectionManager

class Game(object):

    _display_input_box = True
    screen = None

    def main(self):
        pygame.init()
        pygame.display.set_caption("Katch")
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1217, 600))
        
        sprites = pygame.sprite.Group()
        self.create_background()
        
        play_layout = players_layout.Players_layout(self.screen)

     #   self.create_input_ip()

        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            play_layout.update()
            sprites.update(dt / 1000.)
            sprites.draw(self.screen)
            pygame.display.flip()

    def create_background(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))
        background = pygame.image.load('../img/background.jpe')
        self.screen.blit(background, (0, 0))


    def create_input_ip(self):
        if self._display_input_box:
            ip = inputbox.ask(self.screen, "IP to connect")
            connectionManager.ConnectionManager().connection_to_peer(ip)
            self._display_input_box = False