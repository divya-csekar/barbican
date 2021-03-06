# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo.config import cfg
from stevedore import named

from barbican.common import utils
from barbican.plugin.crypto import crypto
from barbican.plugin.interface import secret_store

CONF = cfg.CONF


class _CryptoPluginManager(named.NamedExtensionManager):
    def __init__(self, conf=CONF, invoke_on_load=True,
                 invoke_args=(), invoke_kwargs={}):
        """Crypto Plugin Manager

        Each time this class is initialized it will load a new instance
        of each enabled crypto plugin. This is undesirable, so rather than
        initializing a new instance of this class use the PLUGIN_MANAGER
        at the module level.
        """
        super(_CryptoPluginManager, self).__init__(
            conf.crypto.namespace,
            conf.crypto.enabled_crypto_plugins,
            invoke_on_load=invoke_on_load,
            invoke_args=invoke_args,
            invoke_kwds=invoke_kwargs
        )

    def get_plugin_store_generate(self, type_needed, algorithm=None,
                                  bit_length=None, mode=None):
        """Gets a secret store or generate plugin that supports provided type.

        :param type_needed: PluginSupportTypes that contains details on the
        type of plugin required
        :returns: CryptoPluginBase plugin implementation
        """

        if len(self.extensions) < 1:
            raise crypto.CryptoPluginNotFound()

        for ext in self.extensions:
            if ext.obj.supports(type_needed, algorithm, bit_length, mode):
                plugin = ext.obj
                break
        else:
            raise secret_store.SecretStorePluginNotFound()

        return plugin

    def get_plugin_retrieve(self, plugin_name_for_store):
        """Gets a secret retrieve plugin that supports the provided type.

        :param type_needed: PluginSupportTypes that contains details on the
        type of plugin required
        :returns: CryptoPluginBase plugin implementation
        """

        if len(self.extensions) < 1:
            raise crypto.CryptoPluginNotFound()

        for ext in self.extensions:
            decrypting_plugin = ext.obj
            plugin_name = utils.generate_fullname_for(decrypting_plugin)
            if plugin_name == plugin_name_for_store:
                break
        else:
            raise secret_store.SecretStorePluginNotFound()

        return decrypting_plugin


PLUGIN_MANAGER = _CryptoPluginManager()
