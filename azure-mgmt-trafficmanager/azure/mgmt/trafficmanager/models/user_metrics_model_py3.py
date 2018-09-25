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

from .proxy_resource_py3 import ProxyResource


class UserMetricsModel(ProxyResource):
    """Class representing Traffic Manager User Metrics.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
    :type id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Network/trafficmanagerProfiles.
    :vartype type: str
    :param key: The key returned by the User Metrics operation.
    :type key: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'key': {'key': 'properties.key', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, key: str=None, **kwargs) -> None:
        super(UserMetricsModel, self).__init__(id=id, **kwargs)
        self.key = key
