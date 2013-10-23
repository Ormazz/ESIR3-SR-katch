import threading
from connection import server, client

t = threading.Thread(target=server.create_server)
print("start")
t.start()
print("after")
client.start_game()
