import connection
from control import katch
import Pyro4
import threading

class ConnectionManager(object):
    """Manages the communication with other players. Contains the list of other players' ips.
    Send messages to other players, and receive theirs.

    Members :
        * instance : points to the singleton
        * ip_list : list of known ips
        * ip_serv : local ip (as seen by other players)
    """

    instance = None
    _ip_list = []
    _ip_serv = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
        return my_class.instance

    def get_ip_serv(self):
        return self._ip_serv

    def get_player_information(self, ip):
        """Obtain position and score of the player given by its ip."""
        # We ask the player's RMI the informations we neeed
        network = self.get_network(ip)
        return network.get_player_information()

    def get_current_information(self):
        """Returns position and score of the local player"""
        inf = []    # This will be the buffer returned
        player = katch.Katch().get_player(self._ip_serv)
        inf.append(player._x)
        inf.append(player._y)
        inf.append(player.score)
        return inf

    def add_peer(self, ip):
        """Add a new ip in the list of known ip. Does not add it if it is already in it."""
        if ip not in self._ip_list:
            self._ip_list.append(ip)
            # We have to add a new player
            katch.Katch().add_player(ip)

    def connection_to_peer(self, ip_addr):
        """Connection to an existing network by an ip. This will allow us to connect with every other players.
        Notice that this is a recursive method. It calls every players until we know them all."""
        # Getting the other player's RMI
        network = self.get_network(ip_addr)
        # We give our own ip to that player, so that he knows us
        network.add_ip(self._ip_serv)

        # We then acquire the player's ip list
        ip_list_from_peer = network.get_ip_list()

        # Before continuing, we add its ip in our list
        self.add_peer(ip_addr)
        # Browsing the ip known by the other player
        for ip in ip_list_from_peer:
            if self._ip_serv != ip:
                if ip not in self._ip_list:
                    # If it is a totally new ip, we repeat the process with that player
                    self.connection_to_peer(ip)


    def move_wizard(self, direction):
        """Inquires other player to move our wizard in the given direction."""
        for ip in self._ip_list:
            # For all players, we get their RMI, and move the player that have our ip
            network = self.get_network(ip)
            network.move_player(self._ip_serv, direction)
        network = self.get_network(self._ip_serv)
        network.move_player(self._ip_serv, direction)

    def move_player(self, ip, direction):
        """Moves the player given by its ip in the given direction"""
        cont = katch.Katch()
        with cont.condition:
            cont.players_direction[ip] = direction
            cont.orders_nb.value = cont.orders_nb.value + 1
            if cont.orders_nb.value == len(self._ip_list) + 1:
                cont.condition.notify()

    def get_collectables(self, ip):
        """Obtains the collectables' matrix from a player"""
        network = self.get_network(ip)
        return network.get_collectables()

    def get_wizard_collectables(self):
        """Return the local collectables' matrix"""
        return katch.Katch().get_collectable()

    def leave(self):
        """Alerts the other players that we are leaving the game"""
        for ip in self._ip_list:
            network = self.get_network(ip)
            network.remove_player(self._ip_serv)

    def remove_player(self, ip):
        """Receives the exit message from a player. Removes it from the ips list."""
        self._ip_list.remove(ip)
        katch.Katch().remove_player(ip)

    def get_network(self, ip):
        return Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip)

    def player_ack(self, ip):
        katch.Katch().player_ack[ip] = True

    def wizard_ack(self,):
        for ip in self._ip_list:
            network = self.get_network(ip)
            network.player_ack(self._ip_serv)
