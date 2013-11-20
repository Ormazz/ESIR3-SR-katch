import connection
from connection import rmi
from control import katch
import Pyro4

class ConnectionManager(object):

    instance = None
    _ip_list = []
    _ip_serv = None

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
        return my_class.instance

    def get_player_position(self, ip):
        network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip + ":" + str(connection.DEFAULT_PORT))
        return network.get_player_position()

    def get_current_position(self):
        position = []
        player = katch.Katch().get_player(self._ip_serv)
        position.append(player._x)
        position.append(player._y)
        return position

    def add_peer(self, ip):
        if ip not in self._ip_list:
            self._ip_list.append(ip)
            katch.Katch().add_player(ip)

    def connection_to_peer(self, ip_addr):
        network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip_addr + ":" + str(connection.DEFAULT_PORT))
        network.add_ip(self._ip_serv)
        ip_list_from_peer = network.get_ip_list()

        self.add_peer(ip_addr)

        for ip in ip_list_from_peer:
            if self._ip_serv != ip:
                if ip not in self._ip_list:
                    self.connection_to_peer(ip)

    def move_wizard(self, direction):
        for ip in self._ip_list:
            network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip + ":" + str(connection.DEFAULT_PORT))
            network.move_player(self._ip_serv, direction)

    def move_player(self, ip, direction):
        katch.Katch().move_player(ip, direction)

    def get_collectables(self, ip):
        network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip + ":" + str(connection.DEFAULT_PORT)) 
        return network.get_collectables()

    def get_wizard_collectables(self):
        print("here")
        return katch.Katch().get_collectable()

    def leave(self):
        """Alert the other players that we are leaving the game"""
        for ip in self._ip_list:
            network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip + ":" + str(connection.DEFAULT_PORT))
            network.remove_player(self._ip_serv)

    def remove_player(self, ip):
        """Receive the exit message from a player. Remove it from the ips list."""
        self._ip_list.remove(ip)
        katch.Katch().remove_player(ip)
