import connection
from connection import rmi
import Pyro4

class ConnectionManager:

    instance = None
    _ip_list = []

    def __new__(my_class):
        if my_class.instance is None:
            my_class.instance = object.__new__(my_class)
        return my_class.instance

    def connection_to_peer(self, ip_addr):
        ##TODO RECUP LIST PYRO
        print("Connection to " + str(ip_addr))
        network = Pyro4.Proxy("PYRO:" + connection.URI_CONNECTION + "@" + ip_addr + ":" + str(connection.DEFAULT_PORT))
        print("Get connection")
        ip_list_from_peer = network.get_ip_list()
        print("List from peer " + ip_list_from_peer)

        for ip in ip_list_from_peer:
            if ip not in self._ip_list:
                self._ip_list.append(ip)
                self.connection_to_peer(ip)