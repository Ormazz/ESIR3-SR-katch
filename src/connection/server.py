import Pyro4
from connection.rmi import network
import connection
import urllib.request

def create_server():
	"""Instanciates a RMI server"""
	network_inst = network.Network()
	ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode()
	Pyro4.Daemon.serveSimple(
	    {network_inst:connection.URI_CONNECTION},
	    host= ip,
	    ns=False,
	    port=connection.DEFAULT_PORT)

# NOTE : As you can see, the public IP address is calculated from an externate website
# However, as you can guess, this is NOT optimal at all
# Thus, this solution should be improved in the near future
# By asking to the other ip, maybe ?
