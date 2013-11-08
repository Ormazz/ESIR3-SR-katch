import Pyro4
from connection.rmi import network
import connection

def create_server(ip):
	"""Instanciates a RMI server"""
	network_inst = network.Network()
	print(ip)
	d = Pyro4.Daemon(port=9999, nathost=ip, natport=5555)
	uri = d.register(network_inst, connection.URI_CONNECTION)
	print(uri)
	

# NOTE : As you can see, the public IP address is calculated from an externate website
# However, as you can guess, this is NOT optimal at all
# Thus, this solution should be improved in the near future
# By asking to the other ip, maybe ?
