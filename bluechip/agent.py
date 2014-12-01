#!/usr/bin/python

import urllib2
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import httplib

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def __init__(self, key, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert)

key_retrieval_request = urllib2.Request(sys.argv[1], headers={"Accept" : "application/octet-stream", "X-Project-Id" : "12345", "aik" : "12345"})
#encrypted_aes_key = urllib2.urlopen(key_retrieval_request).read()
opener = urllib2.build_opener(HTTPSClientAuthHandler('/home/dc/certs/client.key','/home/dc/certs/client.crt'))
encrypted_aes_key = opener.open(key_retrieval_request).read()
private_key_filepath = sys.argv[2]
private_key_file = open(private_key_filepath, "r").read()
private_key = RSA.importKey(private_key_file)
padded_private_key = PKCS1_OAEP.new(private_key)
aes_key = padded_private_key.decrypt(encrypted_aes_key)
aes_key = aes_key.replace('\n','')
print aes_key

