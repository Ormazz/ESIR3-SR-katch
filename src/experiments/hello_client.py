#!/usr/bin/python3.3

import Pyro4

# Client

hello = Pyro4.Proxy("PYRO:example.hello@37.187.0.92:9090")
print(hello.hello())
