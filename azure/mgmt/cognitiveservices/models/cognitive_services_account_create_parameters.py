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


class CognitiveServicesAccountCreateParameters(Model):
    """The parameters to provide for the account.

    :param sku: Required. Gets or sets the SKU of the resource.
    :type sku: :class:`Sku <azure.mgmt.cognitiveservices.models.Sku>`
    :param kind: Required. Gets or sets the Kind of the resource. Possible
     values include: 'Academic', 'Bing.Autosuggest', 'Bing.Search',
     'Bing.Speech', 'Bing.SpellCheck', 'ComputerVision', 'ContentModerator',
     'CustomSpeech', 'Emotion', 'Face', 'LUIS', 'Recommendations',
     'SpeakerRecognition', 'Speech', 'SpeechTranslation', 'TextAnalytics',
     'TextTranslation', 'WebLM'
    :type kind: str or :class:`Kind
     <azure.mgmt.cognitiveservices.models.Kind>`
    :param location: Required. Gets or sets the location of the resource. This
     will be one of the supported and registered Azure Geo Regions (e.g. West
     US, East US, Southeast Asia, etc.). The geo region of a resource cannot be
     changed once it is created, but if an identical geo region is specified on
     update the request will succeed.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict
    :param properties: Must exist in the request. Must be an empty object.
     Must not be null.
    :type properties: object
    """

    _validation = {
        'sku': {'required': True},
        'kind': {'required': True},
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, sku, kind, location, properties, tags=None):
        self.sku = sku
        self.kind = kind
        self.location = location
        self.tags = tags
        self.properties = properties