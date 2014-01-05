from test import classes
from connection import server, connectionManager
import unittest
import threading
import socket
import urllib.request

ip = None
port = 9090
try:
	# By default, we try to use a local network
	ip = socket.gethostbyname(socket.getfqdn()) + ":" + str(port)
except:
	# if this doesn't work, we get the connection through the internet
	ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode() + ":" + str(port)


class TestKatch(unittest.TestCase):

	_katch = None
	_threads = list()

	def create_player(self, p_ip):
		katch = classes.KatchTest()
		classes.ConnectionManagerMock().set_ip_serv(p_ip)
		katch.init(
			classes.ConnectionManagerMock(), \
			classes.PlayerManagerTest(None),
			classes.DisplayManagerMock(),
			classes.CollectableManagerMock())

	def setUp(self):

		self._katch = classes.KatchTest()
		classes.ConnectionManagerMock().set_ip_serv(ip)
		self._katch.init(
			classes.ConnectionManagerMock(), \
			classes.PlayerManagerTest(None),
			classes.DisplayManagerMock(),
			classes.CollectableManagerMock())

	def tearDown(self):
		self._katch.leave()


	def test_init(self):
		self.assertIsNotNone(self._katch)

		player = self._katch.get_player(ip)
		self.assertEqual(0, player.get_position()[0])
		self.assertEqual(0, player.get_position()[1])
		self.assertEqual(0, player.score)

		game_state = self._katch.get_game_state()
		game_state.calculate_coll()
		self.assertEqual(1, game_state.get_nb_coll())
		self.assertEqual(True, game_state.get_matrix()[1][1])
	
	def test_add_player(self):
		ip2 = ip.split(":")[0] + ":9091"
		t_player2 = threading.Thread(target=self.create_player, args=(ip2,))
		t_serv2 = threading.Thread(target=server.create_server, args=(ip2,))
		self._threads.append(t_serv2);
		self._threads.append(t_player2);
		t_serv2.start()
		t_player2.start()

		self._katch.connection_to_peer(ip2)
		self.assertIn(ip2,[p._ip for p in self._katch.get_players()])
		self.assertNotNone(self._katch.get_player(ip2))

		player = self._katch.get_player(ip2)
		self.assertEqual(0, player.get_position()[0])
		self.assertEqual(0, player.get_position[1])
		self.assertEqual(0, player._score)

		players_list = self._katch.get_players()
		self.assertEqual(2, len(players_list))

		for t in self._threads:
			t._stop()

	def test_move_player(self):
		pass


if __name__ == '__main__':
	t = threading.Thread(target=server.create_server, args=(ip,))
	t.start()
	unittest.main()
	t._stop()
