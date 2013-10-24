import threading
import time
from gui import client
from connection import server,connectionManager
import urllib.request

ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode()

t = threading.Thread(target=server.create_server, args=(ip,))
t.start()

connectionManager.ConnectionManager()._ip_serv = ip
time.sleep(2)
client.launch()
#client.start_game()
