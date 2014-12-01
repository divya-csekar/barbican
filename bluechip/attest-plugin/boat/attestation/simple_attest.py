"""
Barbican attestation request plugin Concrete class
#boat/attestation/simple_attest.py
"""
from oslo.config import cfg
import os

from boat.attestation import attest
import six
import urllib2
from xml.dom import minidom
import xml.etree.ElementTree as ET

CONF = cfg.CONF
OAT_URL = "http://ec2-54-186-222-47.us-west-2.compute.amazonaws.com/saml.xml"

class SimpleAttestPlugin(attest.AttestPluginBase):
    """Concrete implementation of the attest plugin."""

    def __init__(self, aik):
        """initializes aik,keyId, bindPubKey"""
        #print "At Simple Attest init\n"        
        self.aik = aik
        self.bindPubKey = None


    def checkAttribute(self):        
        """check valid aik"""
        #print "At SimpleAttest checkAttribute\n"
        #if this check fails, return invalid request response code
        if (self.aik != None):
            return True
        return False


    def attestRequest(self):
        """send attestation request to OAT"""
        #print "At SimpleAttest attestRequest\n"
        #send http request to OAT, 
        #self.bindPubKey = response.header['bindPubKey']
        response = urllib2.urlopen(OAT_URL)
        xml = ET.parse(response)
        root = xml.getroot()

        for child in root:
            if "AttributeStatement" in str(child.tag):
                for step_child in child:
                    if "Bind_PublicKey" in str(step_child.attrib):
                        keyelement = step_child.getchildren()[0]
                        self.bindPubKey = keyelement.text
        return self.bindPubKey
