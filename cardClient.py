#!/usr/bin/python
#_*_encoding:utf-8_*_

#cardClient.py

import xmlrpclib

print '123'
s = xmlrpclib.ServerProxy('http://s2.scs.im:10400')
print 'sdsfdfds'
print s.div(5,2)  # Returns 5//2 = 2

# Print list of available methods
print s.system.listMethods()
