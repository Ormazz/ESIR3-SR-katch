import Pyro4
from connection import connectionManager

class Network:

	def get_ip_list(self, ip):
		return connectionManager.ConnectionManager()._ip_list