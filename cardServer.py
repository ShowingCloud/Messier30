#!/usr/bin/python
#_*_encoding:utf-8_*_

#cardServer.py

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Create server
server = SimpleXMLRPCServer(("", 10400), requestHandler = SimpleXMLRPCRequestHandler)
server.register_introspection_functions()

class MyFuncs:
    def div(self, x, y):
        print '######'
        return x // y

server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()
