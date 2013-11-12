import threading
import time
from gui import game
from control import katch
from connection import server,client,connectionManager
import urllib.request

ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode()

connectionManager.ConnectionManager()._ip_serv = ip
katch.Katch()._connection_manager = connectionManager.ConnectionManager()

t = threading.Thread(target=server.create_server, args=(ip,))
t.start()
#time.sleep(2)
game.Game().main()
#client.start_game()
