import threading
import time
from gui import game
from control import katch
from connection import server,client,connectionManager
import urllib.request

ip = "192.168.0.22"

connectionManager.ConnectionManager()._ip_serv = ip
myGame = game.Game()
katch.Katch().init(connectionManager.ConnectionManager(), myGame.get_player_manager(), myGame.get_display_manager())

t = threading.Thread(target=server.create_server, args=(ip,))
t.start()
#time.sleep(2)
myGame.main()
