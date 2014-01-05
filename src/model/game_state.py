from multiprocessing import Manager

# number of cases in the map (width and heigth)
MAP_WIDTH = 20
MAP_HEIGTH = 20

class GameState(object):
    """Gathers all the information about the state of the game.

    Members :
        * players_visited : indicates if changes has happened to the player that the GUI hasn't visited yet
        * players : list of players
        * manager : ensures that some value are shared between the two threadss
        * matrix : positions of the collectables on the map
        * nb_coll : number of collectables remaining
    """
    _players = []
    # _collectables = []

    _manager = Manager()
    _matrix = _manager.list([[False for i in range(MAP_WIDTH)] for j in range(MAP_HEIGTH)])
    _nb_coll = _manager.Value('i', 10)

    def _edit_matrix_value(self,x,y,value):
        """Set one point of the matric to True or False"""
        # We have to separe the line to synchronize the matrix between the two threads
        x_line = self._matrix[x]
        x_line[y] = value
        self._matrix[x] = x_line
        # This can seem odd, but it is how work shared matrix

    def set_players_visited(self, visited):
        self._players_visited = visited

    def add_player(self, player):
        """Adds a new player to the list"""
        self._players.append(player)

    def remove_player(self, player):
        """Removes a player from the list"""
        self._players.remove(player)

    def incr_score_player(self, ip):
        """Increments one player's score by one. The player is identified by its ip."""
        player = self.get_player(ip)
        player.score = player.score + 1

    def add_collectable(self, x, y):
        """Add a collectable to the collectables' matrix.
        If there is already a collectable, returns False. Else, returns True."""
        if self._matrix[x][y]:
            return False
        else:
            self._edit_matrix_value(x,y,True)
            return True

    def remove_collectable(self, x, y):
        """Removes a collectable from the collectables' matrix"""
        self._nb_coll.value = self._nb_coll.value - 1
        self._edit_matrix_value(x,y,False)

    def wizard_on_collectable(self, x, y):
        """Returns True if there is a collectable on the given position"""
        return self._matrix[x][y]

    def set_matrix(self, matrix):
        """Copies a matrix values into the local one"""
        # We do this operation line by line
        for x in range(len(self._matrix)):
            self._matrix[x] = matrix[x]
        # It is important to count the number of collectable remaining in the new matrix
        self.calculate_coll()

    def calculate_coll(self):
        """Counts the number of collectables in the matrix, and set the corresponding number"""
        # We just browse the matrix, and each time we encounter True, we increments the value
        nb = 0
        for x in range(0, len(self._matrix)):
            for y in range(0, len(self._matrix[0])):
                if self._matrix[x][y]:
                    nb = nb + 1

        self._nb_coll.value = nb

    def get_matrix(self):
        return list(self._matrix)

    def get_player(self, ip):
        pl = [p for p in self._players if p._ip == ip]
        return pl[0]

    def pretty_print_matrix(self):
        """For test purposes : will print a simplified version of the matrix (only the forst lines that contains a collectable)"""
        finish = False
        for x in range(0, len(self._matrix)):
            for y in range(0, len(self._matrix[0])):
                if self._matrix[x][y]:
                    finish = True
                    pass

            if finish:
                pass

    def get_nb_coll(self):
        return self._nb_coll.value
