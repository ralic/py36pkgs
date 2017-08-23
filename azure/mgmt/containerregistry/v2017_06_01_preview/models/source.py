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


class Source(Model):
    """The registry node that generated the event. Put differently, while the
    actor initiates the event, the source generates it.

    :param addr: The IP or hostname and the port of the registry node that
     generated the event. Generally, this will be resolved by os.Hostname()
     along with the running port.
    :type addr: str
    :param instance_id: The running instance of an application. Changes after
     each restart.
    :type instance_id: str
    """

    _attribute_map = {
        'addr': {'key': 'addr', 'type': 'str'},
        'instance_id': {'key': 'instanceID', 'type': 'str'},
    }

    def __init__(self, addr=None, instance_id=None):
        self.addr = addr
        self.instance_id = instance_id
