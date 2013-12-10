import Pyro4
from connection.rmi import network
import connection

def create_server(ip):
    """Instanciates a RMI server"""
    # RMI creation
    network_inst = network.Network()
    print(ip)
    tab = str.split(ip, ":")
    # Server creation
    Pyro4.Daemon.serveSimple(
        {network_inst:connection.URI_CONNECTION},
        host=tab[0],
        ns=False,
        port=int(tab[1])
        )
