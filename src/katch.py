import threading
import time
from connection import server, client

t = threading.Thread(target=server.create_server)
t.start()

time.sleep(2)
client.start_game()
