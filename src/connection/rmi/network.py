from connection import connectionManager

class Network(object):

	def get_ip_list(self):
		return connectionManager.ConnectionManager()._ip_list