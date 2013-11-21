from connection import connectionManager

class Network(object):

    def get_player_position(self):
        return connectionManager.ConnectionManager().get_current_position()

    def get_ip_list(self):
        return connectionManager.ConnectionManager()._ip_list

    def add_ip(self, ip):
        connectionManager.ConnectionManager().add_peer(ip)

    def move_player(self, ip, direction):
        connectionManager.ConnectionManager().move_player(ip, direction)

    def get_collectables(self):
        print(str(connectionManager.ConnectionManager().get_wizard_collectables()))
        return connectionManager.ConnectionManager().get_wizard_collectables()

    def remove_player(self, ip):
    	connectionManager.ConnectionManager().remove_player(ip)

    def remove_collectable(self, x , y):
        connectionManager.ConnectionManager().remove_wizard_collectable(x, y)
