import pygame
from gui import inputBox
from gui import players_layout
from gui import display_manager
from gui import player_manager
from gui import collectable
from gui import collectable_manager

class Game(object):
    _screen = None
    _background = None
    _display_manager = None
    _player_manager = None
    _collectable_manager = None

    def __init__(self):
        self._display_manager = display_manager.DisplayManager()

        pygame.init()
        pygame.display.set_caption("Katch")
        self._screen = pygame.display.set_mode((1217, 600))

        self._player_manager = player_manager.Player_manager(self._screen)
        self._display_manager.add(self._player_manager)

        self._collectable_manager = collectable_manager.Collectable_manager()
        self._display_manager.add(self._collectable_manager)

    def main(self):
        sprites = pygame.sprite.Group()
        self.create_background()

        self._display_manager.add(players_layout.Players_layout(self._screen))

        input_box = inputBox.InputBox(self._screen, "IP to connect")
        self._display_manager._input_box = input_box
        self._display_manager.add(input_box)

        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    self._player_manager.event(event)
                    input_box.event(event)


            self.update_background()
            self._display_manager.update()
            sprites.update(dt / 1000.)
            sprites.draw(self._screen)
            pygame.display.flip()
        pygame.quit()

    def get_player_manager(self):
        return self._player_manager

    def get_display_manager(self):
        return self._display_manager

    def get_collectable_manager(self):
        return self._collectable_manager

    def create_background(self):
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self.update_background()

    def update_background(self):
        self._background.fill((255, 255, 255))
        self._screen.blit(self._background, (0, 0))
        self._background = pygame.image.load('../img/background.jpe')
        self._screen.blit(self._background, (0, 0))
