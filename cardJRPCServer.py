#!/usr/bin/python
#_*_encoding:utf-8_*_

#cardServer.py

import pyjsonrpc

def add(a, b):
    """Test function"""
    return a + b

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    # Register public JSON-RPC methods
    methods = {
        "add": add
    }

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = ('', 10400),
    RequestHandlerClass = RequestHandler
)
print "Starting HTTP server ..."
print "URL: http://s2.scs.im:10400"
http_server.serve_forever()
