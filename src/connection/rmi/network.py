import Pyro4
from connection import connectionManager

class Network(object):

	def get_ip_list(self, ip):
		return connectionManager.ConnectionManager()._ip_list