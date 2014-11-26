"""
Barbican attestation request plugin Base class
#boat/attestation/attest.py
"""
import abc
import six
from oslo.config import cfg
from requests import exceptions as request_exceptions

CONF = cfg.CONF
DEFAULT_PLUGIN_NAMESPACE = 'boat.attestation.plugin'
DEFAULT_PLUGINS = ['simple_attest']
OAT_IP=""
OAT_PORT=""
'''
attestation_opt_group = cfg.OptGroup(name='attestation',
                                title='Attestation Plugin Options')
attestation_opts = [
    cfg.StrOpt('namespace',
               default=DEFAULT_PLUGIN_NAMESPACE
               ),
    cfg.MultiStrOpt('enabled_attestation_plugins',
                    default=DEFAULT_PLUGINS
                    )
]
CONF.register_group(attestation_opt_group)
CONF.register_opts(attestation_opts, group=attestation_opt_group)
'''

class AttestPluginBase(object):
    """Implementation of the attestation plugin base"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def checkAttribute(self):        
        """check valid aik, keyId"""
        print "At Attest Base abstract checkAttribute\n"
        #if this check fails, return invalid request response code
        return False


    @abc.abstractmethod
    def attestRequest(self):
        """send attestation request to OAT"""
        print "At Attest Base abstract attestRequest\n"
        #send http request to OAT, 
        #self.bindPubKey = response.header['bindPubKey']
        return None

