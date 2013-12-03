import Pyro4
from connection.rmi import network
import connection

def create_server(ip):
    """Instanciates a RMI server"""
    # RMI creation
    network_inst = network.Network()
    print(ip)
    # Server creation
    Pyro4.Daemon.serveSimple(
        {network_inst:connection.URI_CONNECTION},
        host=ip,
        ns=False,
        port=connection.DEFAULT_PORT)
