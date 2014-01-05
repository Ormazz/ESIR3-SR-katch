import pygame
from gui import inputBox
from gui import players_layout
from gui import display_manager
from gui import player_manager
from gui import collectable_manager

class Game(object):
    """GUI main class. Allows to launch the game once it is initialized.

    Members :
        * screen : game display
        * background : background's picture
        * display_manager : manager of the game zone
        * player_anager : manager of the characters
        * collectable_manager : manager of the collectable items
    """
    _screen = None
    _background = None
    _display_manager = None
    _player_manager = None
    _collectable_manager = None

    def __init__(self):
        # Launches pygame windows
        pygame.init()
        pygame.display.set_caption("Katch")
        self._screen = pygame.display.set_mode((680, 460))

        #Creates player layout
        play_layout = players_layout.PlayersLayout(self._screen)

        # Creates the managers
        self._display_manager = display_manager.DisplayManager(self._screen)
        self._player_manager = player_manager.PlayerManager(self._screen, play_layout)
        self._display_manager.add(self._player_manager)
        self._collectable_manager = collectable_manager.CollectableManager(self._screen)

        # Adds the player layout to the display
        self._display_manager.add(play_layout)

        # The display manager must be connected to the collectable manager
        self._display_manager.add(self._collectable_manager)

    def main(self):
        """
            Game's main method. First, display the connect box.
            Then, it enters a loop where it regularly checks the control if some new data have to be visited. If so, it updates the display.
            Also detects events and alert the control.
            The game closes when the player closes the windows.
        """
        # Displays the background
        sprites = pygame.sprite.Group()
        self.create_background()

        # Print the IP box ; The user has to enter an ip to connect, or wait for another player to connect, before starting playing
        input_box = inputBox.InputBox(self._screen, "IP to connect")
        self._display_manager._input_box = input_box
        self._display_manager.add(input_box)

        # Starts the sweet music, so the spiders can dance
        sound = pygame.mixer.Sound("../music/katch.ogg")
        sound.play(-1)

        # Entering the loop
        clock = pygame.time.Clock()
        running = True
        while running:
            # Every 10 ms
            dt = clock.tick(10)
            # Checks for events (mostly user input)
            for event in pygame.event.get():
                # The game quits when the user close the window
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # … Or when he presses escape
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # Eitherway, it calls the player manager to react
                    self._player_manager.event(event)
                    # The input box as well
                    input_box.event(event)

            # Now, let's update everything!
            self.update_background()
            self._display_manager.update()
            sprites.update(dt / 1000.)
            sprites.draw(self._screen)
            pygame.display.flip()

        # Out of the loop, we close the game
        pygame.quit()

    def get_player_manager(self):
        return self._player_manager

    def get_display_manager(self):
        return self._display_manager

    def get_collectable_manager(self):
        return self._collectable_manager

    def create_background(self):
        """Set the backroung image : a peaceful field with flowers, rocks, and pixels"""
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self.update_background()

    def update_background(self):
        """Update the background image"""
        self._background.fill((255, 255, 255))
        self._screen.blit(self._background, (0, 0))
        self._background = pygame.image.load('../img/background.png')
        self._screen.blit(self._background, (0, 0))
