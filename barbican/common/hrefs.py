#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from barbican.common import utils


def convert_secret_to_href(secret_id):
    """Convert the secret IDs to a HATEOS-style href."""
    if secret_id:
        resource = 'secrets/' + secret_id
    else:
        resource = 'secrets/????'
    return utils.hostname_for_refs(resource=resource)


def convert_order_to_href(order_id):
    """Convert the order IDs to a HATEOS-style href."""
    if order_id:
        resource = 'orders/' + order_id
    else:
        resource = 'orders/????'
    return utils.hostname_for_refs(resource=resource)


def convert_container_to_href(container_id):
    """Convert the container IDs to a HATEOS-style href."""
    if container_id:
        resource = 'containers/' + container_id
    else:
        resource = 'containers/????'
    return utils.hostname_for_refs(resource=resource)


def convert_transport_key_to_href(transport_key_id):
    """Convert the transport key IDs to a HATEOS-style href."""
    if transport_key_id:
        resource = 'transport_keys/' + transport_key_id
    else:
        resource = 'transport_keys/????'
    return utils.hostname_for_refs(resource=resource)


# TODO(hgedikli) handle list of fields in here
def convert_to_hrefs(fields):
    """Convert id's within a fields dict to HATEOS-style hrefs."""
    if 'secret_id' in fields:
        fields['secret_ref'] = convert_secret_to_href(fields['secret_id'])
        del fields['secret_id']

    if 'order_id' in fields:
        fields['order_ref'] = convert_order_to_href(fields['order_id'])
        del fields['order_id']

    if 'container_id' in fields:
        fields['container_ref'] = convert_container_to_href(
            fields['container_id'])
        del fields['container_id']

    if 'transport_key_id' in fields:
        fields['transport_key_ref'] = convert_transport_key_to_href(
            fields['transport_key_id'])
        del fields['transport_key_id']

    return fields


def convert_list_to_href(resources_name, offset, limit):
    """Supports pretty output of paged-list hrefs.

    Convert the offset/limit info to a HATEOS-style href
    suitable for use in a list navigation paging interface.
    """
    resource = '{0}?limit={1}&offset={2}'.format(resources_name, limit,
                                                 offset)
    return utils.hostname_for_refs(resource=resource)


def previous_href(resources_name, offset, limit):
    """Supports pretty output of previous-page hrefs.

    Create a HATEOS-style 'previous' href suitable for use in a list
    navigation paging interface, assuming the provided values are the
    currently viewed page.
    """
    offset = max(0, offset - limit)
    return convert_list_to_href(resources_name, offset, limit)


def next_href(resources_name, offset, limit):
    """Supports pretty output of next-page hrefs.

    Create a HATEOS-style 'next' href suitable for use in a list
    navigation paging interface, assuming the provided values are the
    currently viewed page.
    """
    offset = offset + limit
    return convert_list_to_href(resources_name, offset, limit)


def add_nav_hrefs(resources_name, offset, limit,
                  total_elements, data):
    """Adds next and/or previous hrefs to paged list responses.

    :param resources_name: Name of api resource
    :param offset: Element number (ie. index) where current page starts
    :param limit: Max amount of elements listed on current page
    :param num_elements: Total number of elements
    :returns: augmented dictionary with next and/or previous hrefs
    """
    if offset > 0:
        data.update({'previous': previous_href(resources_name,
                                               offset,
                                               limit)})
    if total_elements > (offset + limit):
        data.update({'next': next_href(resources_name,
                                       offset,
                                       limit)})
    return data
