from connection import connectionManager

class Network(object):

    def get_player_information(self):
        return connectionManager.ConnectionManager().get_current_information()

    def get_ip_list(self):
        return connectionManager.ConnectionManager()._ip_list

    def add_ip(self, ip):
        connectionManager.ConnectionManager().add_peer(ip)

    def move_player(self, ip, direction):
        connectionManager.ConnectionManager().move_player(ip, direction)

    def get_collectables(self):
        return connectionManager.ConnectionManager().get_wizard_collectables()

    def remove_player(self, ip):
    	connectionManager.ConnectionManager().remove_player(ip)

    def remove_collectable(self, ip, x , y):
        connectionManager.ConnectionManager().remove_wizard_collectable(ip, x, y)

    def finish_game():
        return connectionManager.ConnectionManager().finish_game()
