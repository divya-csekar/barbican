"""
Barbican attestation request plugin Manager class for stevedore
#boat/attestation/attest_manager.py
"""

from oslo.config import cfg
from stevedore import named

CONF = cfg.CONF


class _AttestManager(named.NamedExtensionManager):
    def __init__(self, conf=CONF, invoke_on_load=True,
                 invoke_args=(), invoke_kwargs={}):
        """initializes attester plugin"""
        print "At Attest Base abstract attestRequest\n"
        super(_AttestManager, self).__init__(
            'boat.attestation.plugin',
            'simple_attest',
            invoke_on_load=invoke_on_load,
            invoke_args=invoke_args,
            invoke_kwds=invoke_kwargs
        )

PLUGIN_MANAGER = _AttestManager()

"""
            conf.attestation.namespace,
            conf.attestation.enabled_attestation_plugins,
            invoke_on_load=invoke_on_load,
            invoke_args=invoke_args,
            invoke_kwds=invoke_kwargs
        )

PLUGIN_MANAGER = _AttestManager()
"""