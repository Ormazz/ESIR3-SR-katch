def start_game():
	ip_addr = input("IP to connect :")
	ConnectionManager().connection_to_peer(ip_addr)