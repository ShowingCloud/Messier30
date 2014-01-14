#!/usr/bin/python
#_*_encoding:utf-8_*_

#cardClient.py


import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://s2.scs.im:10400"
)
print http_client.call("add", 1, 2)
# Result: 3

# It is also possible to use the *method* name as *attribute* name.
print http_client.add(1, 2)
# Result: 3
