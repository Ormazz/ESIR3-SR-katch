import threading
import time
from control import katch
from connection import server,client,connectionManager
import urllib.request

ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode()

connectionManager.ConnectionManager()._ip_serv = ip
katch.Katch(connectionManager.ConnectionManager())

t = threading.Thread(target=server.create_server, args=(ip,))
t.start()

time.sleep(2)
client.start_game()
