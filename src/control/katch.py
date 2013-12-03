from model import game_state
from model import player
from control import collectable_stack
import pygame

# IMPORTANT : while the players of the game are called "player", the local player is identified as "wizard".
# You should remember this if you don't want any confusion!

class Katch(object):
    """
    Katch main class. This class is the head of the control, making all the decisions.
    The main method, though, is actually in the gui. Indeed, it is this that detects the event, and call the control.
    The gui thus regularly check if values from the control has been "visited" by it, meaning if there is something new it should update.

    Members :
        * instance : static value pointing to the singleton
        * game_state : informations about the state of the game (players, collectables, etc)
        * connection_manager : entity responsible of the communication with other players
        * player_manager : manager of the players on the display
        * display manager : manager of the display
        * collectable_manager : manager of the collectables on the display
        * collectable_stack : manager of the collectables actions
    """

    instance = None
    _game_state = None
    _connection_manager = None
    _player_manager = None
    _display_manager = None
    _collectable_manager = None

    _collectable_stack = None

    def __new__(my_class):
        # Katch is a singleton : if it has already been constructed, we return the one that is running
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
            my_class._game_state = game_state.GameState()
        return my_class.instance

    def init(self, connection_manager, player_manager, display_manager, collectable_manager):
        """
        Starts the game with the given managers. Creates the local player (wizard), and generates a position for the collectables.
        """
        # Set the managers
        self._player_manager = player_manager
        self._connection_manager = connection_manager
        self._display_manager = display_manager
        self._collectable_manager = collectable_manager

        # Initiates the local player
        wizard = player.Player(connection_manager._ip_serv)
        # For now, players are put at the top-left corner at the beginning ; but that might change in a future version
        wizard._x = 0
        wizard._y = 0
        self._game_state.add_player(wizard)

        # Initiates the collectables
        self._collectable_stack = collectable_stack.CollectableStack(self._game_state, connection_manager, collectable_manager, self)
        self._collectable_stack.generate_collectable()

    def add_player(self, ip):
        "Add a new player, the ip is the id"
        new_player = player.Player(ip)

        #Get the position and the score of the player
        inf = self._connection_manager.get_player_information(ip)
        new_player._x = inf[0]
        new_player._y = inf[1]
        new_player.score = inf[2]

        #Add the player in the model
        self._game_state.add_player(new_player)

        #Create the player on the screen
        self._player_manager.create_player(inf[0], inf[1], ip)

        #If the game isn't started (ie: first connection to a player)
        #We create the player character (wizard)
        #And we disable the input box where the ip is writed
        if not self._player_manager.get_started():
            self.activate_player(self._connection_manager.get_ip_serv())
            self._display_manager.disabled_input_box()

            #Create the fez spiders in the model and on the screen
            if not self._collectable_manager.get_started():
                self._collectable_stack.create_collectable(self.get_collectable())
                self._collectable_manager.set_started(True)

    def connection_to_peer(self, ip):
        """Tries to connect to another player, given by its ip."""
        #Gets the spiders of the player and create them (replacing the one we have already created)
        self._collectable_stack.activate_collectable(ip)

        #Connect to a peer
        self._connection_manager.connection_to_peer(ip)

    def activate_player(self, ip):
        "Creates the local player character (wizard) on the screen"
        self._player_manager.activate_player(0, 0, ip)

    def visit_players(self, visit):
        "Tell if The player and score list is visited by the gui."
        self._game_state.set_players_visited(visit)

    def players_has_changed(self):
        "Tell if the player and score list has changed"
        return not self._game_state.get_players_visited()

    def get_players(self):
        "Get the players list"
        return self._game_state._players

    def get_player(self, ip):
        "Get the associated player"
        return self._game_state.get_player(ip)

    def move_player(self, ip, direction):
        "Move a player in a direction"

        #Get the model player
        player = self.get_player(ip)

        #Get the graphical character
        character = self._player_manager.get_player(ip)
        if direction == player.DOWN:
            player.move(player.DOWN)
            character.down()
        if direction == player.UP:
            player.move(player.UP)
            character.up()
        if direction == player.LEFT:
            player.move(player.LEFT)
            character.left()
        if direction == player.RIGHT:
            player.move(player.RIGHT)
            character.right()

    def move_wizard(self, event):
        """Move the local player in a direction"""
        # We only obey of the game has started
        if self._player_manager.get_started() :
            # The wizard can't move if it is at the border of the screen
            if self._player_manager.wizard_can_move(event.key):
                # Retrieve the wizard and its position in the model
                wizard = self.get_player(self._connection_manager.get_ip_serv())
                position = wizard.get_position()
                # Set the wizard's new position acording to the direction he moved
                # (these if else are so ugly… but is it right to comment the code in comments?)
                if event.key == pygame.K_DOWN and position[1] + 1 < game_state.MAP_HEIGTH:
                    # Announces to other players that the wizard has moved
                    self._connection_manager.move_wizard(wizard.DOWN)
                    # Moves the wizard in the model
                    wizard.move(wizard.DOWN)
                    # Move the wizard in the display
                    self._player_manager.wizard.down()
                    # Check if the wizard has obtained a collectable
                    self._collectable_stack.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_UP and position[1] > 0:
                    self._connection_manager.move_wizard(wizard.UP)
                    wizard.move(wizard.UP)
                    self._player_manager.wizard.up()
                    self._collectable_stack.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_LEFT and position[0] > 0:
                    self._connection_manager.move_wizard(wizard.LEFT)
                    wizard.move(wizard.LEFT)
                    self._player_manager.wizard.left()
                    self._collectable_stack.check_wizard_collectable(self._player_manager.wizard)
                if event.key == pygame.K_RIGHT and position[0] + 1 < game_state.MAP_WIDTH:
                    self._connection_manager.move_wizard(wizard.RIGHT)
                    wizard.move(wizard.RIGHT)
                    self._player_manager.wizard.right()
                    self._collectable_stack.check_wizard_collectable(self._player_manager.wizard)

    def remove_collectable(self, ip, x, y):
        """Remove a collectable from the game"""
        self._collectable_stack.remove_collectable(ip, x, y)

    def get_collectable(self):
        """Return the collectables' matrix"""
        return self._game_state.get_matrice()

    def leave(self):
        """Local exit method ; Alert the other players that we are not connected anymore"""
        if self._player_manager.get_started():
            self._connection_manager.leave()

    def remove_player(self,ip):
        """Remove a player that has left the game"""

        # Removing from the model
        self._game_state.remove_player(self._game_state.get_player(ip))
        # Removing from the interface
        self._player_manager.remove_player(ip)

    def finish_game(self):
        """End of the game, when all the collectables has been collected"""
        #Deactive the players on th screen
        self._player_manager.deactivate_player()

        #Launch the fireworks
        self._display_manager.launch_fireworks()
