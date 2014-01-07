from connection import connectionManager

class Network(object):
    """Game RMI used to allows other players to see local data and to send events"""

    def get_player_information(self):
        """Returns player position and score"""
        return connectionManager.ConnectionManager().get_current_information()

    def get_ip_list(self):
        """Return the list of players known by the local application"""
        return connectionManager.ConnectionManager()._ip_list

    def add_ip(self, ip):
        """Add a new player to the game"""
        connectionManager.ConnectionManager().add_peer(ip)

    def move_player(self, ip, direction):
        """Moves a player (identified by its ip) one case in the given direction"""
        connectionManager.ConnectionManager().move_player(ip, direction)

    def get_collectables(self):
        """Returns the collectables' matrix"""
        return connectionManager.ConnectionManager().get_wizard_collectables()

    def remove_player(self, ip):
        """Remove a player from the local list"""
        connectionManager.ConnectionManager().remove_player(ip)
