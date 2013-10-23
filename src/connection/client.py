from connection import connectionManager

def start_game():
    ip_addr = input("IP to connect :")
    connectionManager.ConnectionManager().connection_to_peer(ip_addr)
