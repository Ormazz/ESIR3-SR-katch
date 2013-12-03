from connection import connectionManager

# Client console to starts the game without GUI
# Is not used anymore

def start_game():
    ip_addr = input("IP to connect :")
    connectionManager.ConnectionManager().connection_to_peer(ip_addr)
