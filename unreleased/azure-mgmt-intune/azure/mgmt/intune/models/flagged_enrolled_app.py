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


class FlaggedEnrolledApp(Resource):
    """Flagged Enrolled App for the given tenant.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource Tags
    :type tags: dict
    :param location: Resource Location
    :type location: str
    :ivar device_type:
    :vartype device_type: str
    :ivar friendly_name:
    :vartype friendly_name: str
    :ivar last_modified_time:
    :vartype last_modified_time: str
    :ivar platform:
    :vartype platform: str
    :param errors:
    :type errors: list of :class:`FlaggedEnrolledAppError
     <azure.mgmt.intune.models.FlaggedEnrolledAppError>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'device_type': {'readonly': True},
        'friendly_name': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'platform': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'device_type': {'key': 'properties.deviceType', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'str'},
        'platform': {'key': 'properties.platform', 'type': 'str'},
        'errors': {'key': 'properties.errors', 'type': '[FlaggedEnrolledAppError]'},
    }

    def __init__(self, tags=None, location=None, errors=None):
        super(FlaggedEnrolledApp, self).__init__(tags=tags, location=location)
        self.device_type = None
        self.friendly_name = None
        self.last_modified_time = None
        self.platform = None
        self.errors = errors