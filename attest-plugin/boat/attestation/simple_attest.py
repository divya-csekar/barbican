"""
Barbican attestation request plugin Concrete class
#boat/attestation/simple_attest.py
"""
from oslo.config import cfg
import os

from boat.attestation import attest
import six

CONF = cfg.CONF
'''
simple_attest_plugin_group = cfg.OptGroup(name='simple_attest_plugin',
                                          title="Simple Attest Plugin Options")
simple_attest_plugin_opts = [
    cfg.StrOpt('aik',
               default=b'this is a dummy aik, do not use for production!')
]
CONF.register_group(simple_attest_plugin_group)
CONF.register_opts(simple_attest_plugin_opts, group=simple_attest_plugin_group)
'''

class SimpleAttestPlugin(attest.AttestPluginBase):
    """Concrete implementation of the attest plugin."""

    def __init__(self, aik=None, keyId=None):
        """initializes aik,keyId, bindPubKey"""
        print "At Simple Attest init\n"        
        self.aik = aik
        self.keyId = keyId
        self.bindPubKey = None


    def checkAttribute(self):        
        """check valid aik, keyId"""
        print "At SimpleAttest checkAttribute\n"
        #if this check fails, return invalid request response code
        if ((self.aik != None) and (self.keyId != None)):
            return True
        return False


    def attestRequest(self):
        """send attestation request to OAT"""
        print "At SimpleAttest attestRequest\n"
        #send http request to OAT, 
        #self.bindPubKey = response.header['bindPubKey']
        return self.bindPubKey
