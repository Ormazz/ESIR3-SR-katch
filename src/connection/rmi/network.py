from connection import connectionManager

class Network(object):

    def get_ip_list(self):
        return connectionManager.ConnectionManager()._ip_list

    def add_ip(self, ip):
        if ip not in connectionManager.ConnectionManager()._ip_list:
            connectionManager.ConnectionManager()._ip_list.append(ip)