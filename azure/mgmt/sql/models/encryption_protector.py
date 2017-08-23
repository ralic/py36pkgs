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

from .proxy_resource import ProxyResource


class EncryptionProtector(ProxyResource):
    """The server encryption protector.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param kind: Kind of encryption protector. This is metadata used for the
     Azure portal experience. Possible values include: '', 'azurekeyvault',
     'servicemanaged'
    :type kind: str or :class:`enum <azure.mgmt.sql.models.enum>`
    :ivar location: Resource location.
    :vartype location: str
    :ivar subregion: Subregion of the encryption protector.
    :vartype subregion: str
    :param server_key_name: The name of the server key.
    :type server_key_name: str
    :param server_key_type: The encryption protector type like
     'ServiceManaged', 'AzureKeyVault'. Possible values include:
     'ServiceManaged', 'AzureKeyVault'
    :type server_key_type: str or :class:`ServerKeyType
     <azure.mgmt.sql.models.ServerKeyType>`
    :ivar uri: The URI of the server key.
    :vartype uri: str
    :ivar thumbprint: Thumbprint of the server key.
    :vartype thumbprint: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'subregion': {'readonly': True},
        'uri': {'readonly': True},
        'thumbprint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'subregion': {'key': 'properties.subregion', 'type': 'str'},
        'server_key_name': {'key': 'properties.serverKeyName', 'type': 'str'},
        'server_key_type': {'key': 'properties.serverKeyType', 'type': 'str'},
        'uri': {'key': 'properties.uri', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
    }

    def __init__(self, kind=None, server_key_name=None, server_key_type=None):
        super(EncryptionProtector, self).__init__()
        self.kind = kind
        self.location = None
        self.subregion = None
        self.server_key_name = server_key_name
        self.server_key_type = server_key_type
        self.uri = None
        self.thumbprint = None
