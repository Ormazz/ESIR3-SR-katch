from connection import connectionManager

class Network(object):

    def get_player_position(self):
        return connectionManager.ConnectionManager().get_current_position()

    def get_ip_list(self):
        return connectionManager.ConnectionManager()._ip_list

    def add_ip(self, ip):
        connectionManager.ConnectionManager().add_peer(ip)

    def move_player(self, ip, direction):
        print("CALL")
        connectionManager.ConnectionManager.move_player(ip, direction)
