#!/usr/bin/python3.3

import Pyro4

# Server

class Hello:
    def hello(self):
        return "Hello !"

hello = Hello()
Pyro4.Daemon.serveSimple(
    {hello:"example.hello"},
    host="doudou",
    ns=True)
