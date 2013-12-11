import threading
from gui import game
from control import katch
from connection import server,connectionManager
import urllib.request
import sys
import socket

# Launch of the game

# Retrieving the local ip from the outside
# Getting the port
if len(sys.argv) < 2:
	print("Please give the port you wish to use for the server!")
else:
	port = sys.argv[1]
	try:
		# By default, we try to use a local network
		ip = socket.gethostbyname(socket.getfqdn()) + ":" + str(port)
	except:
		# if this doesn't work, we get the connection through the internet
		ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode() + ":" + str(port)

	# Initializing the game and its component
	connectionManager.ConnectionManager()._ip_serv = ip
	myGame = game.Game()
	katch.Katch().init(connectionManager.ConnectionManager(), myGame.get_player_manager(), myGame.get_display_manager(), myGame.get_collectable_manager())

	# Launching the server in another thread
	t = threading.Thread(target=server.create_server, args=(ip,))
	t.start()

	# Launching the game
	myGame.main()

	# When the game has stopped, we have to send a message to other players
	katch.Katch().leave()

	# Shutting down the server
	t._stop()
