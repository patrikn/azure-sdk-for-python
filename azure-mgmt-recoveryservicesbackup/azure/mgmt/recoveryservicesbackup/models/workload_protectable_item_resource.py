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

from .resource import Resource


class WorkloadProtectableItemResource(Resource):
    """Base class for backup item. Workload-specific backup items are derived from
    this class.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id represents the complete path to the resource.
    :vartype id: str
    :ivar name: Resource name associated with the resource.
    :vartype name: str
    :ivar type: Resource type represents the complete path of the form
     Namespace/ResourceType/ResourceType/...
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :param e_tag: Optional ETag.
    :type e_tag: str
    :param properties: WorkloadProtectableItemResource properties
    :type properties: :class:`WorkloadProtectableItem
     <azure.mgmt.recoveryservicesbackup.models.WorkloadProtectableItem>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'WorkloadProtectableItem'},
    }

    def __init__(self, location=None, tags=None, e_tag=None, properties=None):
        super(WorkloadProtectableItemResource, self).__init__(location=location, tags=tags, e_tag=e_tag)
        self.properties = properties
