# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from gui import updatable
from connection import connectionManager

class InputBox(updatable.Updatable):

    _current_string = []
    _question = []
    _display = True

    def __init__(self, screen, question):
        self.screen = screen
        self._question = question

    def get_key(self, event):
        if event.type == KEYDOWN:
            if pygame.key.get_mods() and KMOD_SHIFT:
                return self.get_laptop_key(event.key)
            return event.key

    def event(self, event):
        if self._display:
            inkey = self.get_key(event)
            if event.key == pygame.K_RETURN:
                self._display = False
                connectionManager.ConnectionManager().connection_to_peer("".join(self._current_string))
            elif inkey == K_BACKSPACE:
                self._current_string = self._current_string[0:-1]
            elif inkey == K_MINUS:
                self._current_string.append("_")
            elif inkey <= 127:
                self._current_string.append(chr(inkey))
            self.display_box(self.screen, self._question + ": " + "".join(self._current_string))

    def update(self):
        if self._display:
            self.display_box(self.screen, self._question + ": " + "".join(self._current_string))

    def get_laptop_key(self, key):
        if key == 38:
            return 49
        elif key == 233:
            return 50
        elif key == 34:
            return 51
        elif key == 39:
            return 52
        elif key == 40:
            return 53
        elif key == 45:
            return 54
        elif key == 232:
            return 55
        elif key == 95:
            return 56
        elif key == 231:
            return 57
        elif key == 224:
            return 48
        elif key == 59:
            return 46
        return key

    def display_box(self, screen, message):
        "Print a message in a box in the middle of the screen"
        fontobject = pygame.font.Font(None,18)
        pygame.draw.rect(screen, (0,0,0),
                         ((screen.get_width() / 2) - 100,
                          (screen.get_height() / 2) - 10,
                          200,20), 0)
        pygame.draw.rect(screen, (255,255,255),
                         ((screen.get_width() / 2) - 102,
                          (screen.get_height() / 2) - 12,
                          204,24), 1)
        if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (255,255,255)),
                      ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
