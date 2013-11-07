import pygame
from gui import inputBox
from gui import players_layout
from gui import display_manager

class Game(object):

    _display_input_box = False
    _screen = None
    _background = None
    _display_manager = None

    def main(self):
        self._display_manager = display_manager.DisplayManager()

        pygame.init()
        pygame.display.set_caption("Katch")
        clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((1217, 600))
        
        sprites = pygame.sprite.Group()
        self.create_background()
        
        self._display_manager.add(players_layout.Players_layout(self._screen))
        input_box = inputBox.InputBox(self._screen, "IP to connect")
        self._display_manager.add(input_box)

        self.create_input_ip()

        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    input_box.event(event)

            self.update_background()
            self._display_manager.update()

            sprites.update(dt / 1000.)
            sprites.draw(self._screen)
            pygame.display.flip()

    def create_background(self):
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self.update_background()

    def update_background(self):
        self._background.fill((255, 255, 255))
        self._screen.blit(self._background, (0, 0))
        self._background = pygame.image.load('../img/background.jpe')
        self._screen.blit(self._background, (0, 0))


    def create_input_ip(self):
        self._input_box = inputBox.InputBox(self._screen, "IP to connect")