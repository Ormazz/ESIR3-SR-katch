#!/usr/bin/python3.3

import Pyro4

# Client

hello = Pyro.Proxy("PYRO:example.hello@148.60.14.62:9090")
print(hello.hello())
