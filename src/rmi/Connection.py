import Pyro4

class Connection:

	def get_ip_list(self, ip):
		return ConnectionManager()._ip_list