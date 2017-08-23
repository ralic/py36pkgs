# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetNetworkConfigurationDnsSettings(Model):
    """Describes a virtual machines scale sets network configuration's DNS
    settings.

    :param dns_servers: List of DNS servers IP addresses
    :type dns_servers: list of str
    """

    _attribute_map = {
        'dns_servers': {'key': 'dnsServers', 'type': '[str]'},
    }

    def __init__(self, dns_servers=None):
        self.dns_servers = dns_servers
