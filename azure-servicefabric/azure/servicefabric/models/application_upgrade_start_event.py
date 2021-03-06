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

from .application_event import ApplicationEvent


class ApplicationUpgradeStartEvent(ApplicationEvent):
    """Application Upgrade Start event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param application_id: Required. The identity of the application. This is
     an encoded representation of the application name. This is used in the
     REST APIs to identify the application resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the application name is "fabric:/myapp/app1",
     the application identity would be "myapp\\~app1" in 6.0+ and "myapp/app1"
     in previous versions.
    :type application_id: str
    :param application_type_name: Required. Application type name.
    :type application_type_name: str
    :param current_application_type_version: Required. Current Application
     type version.
    :type current_application_type_version: str
    :param application_type_version: Required. Target Application type
     version.
    :type application_type_version: str
    :param upgrade_type: Required. Type of upgrade.
    :type upgrade_type: str
    :param rolling_upgrade_mode: Required. Mode of upgrade.
    :type rolling_upgrade_mode: str
    :param failure_action: Required. Action if failed.
    :type failure_action: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'application_id': {'required': True},
        'application_type_name': {'required': True},
        'current_application_type_version': {'required': True},
        'application_type_version': {'required': True},
        'upgrade_type': {'required': True},
        'rolling_upgrade_mode': {'required': True},
        'failure_action': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'application_id': {'key': 'ApplicationId', 'type': 'str'},
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'current_application_type_version': {'key': 'CurrentApplicationTypeVersion', 'type': 'str'},
        'application_type_version': {'key': 'ApplicationTypeVersion', 'type': 'str'},
        'upgrade_type': {'key': 'UpgradeType', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'failure_action': {'key': 'FailureAction', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationUpgradeStartEvent, self).__init__(**kwargs)
        self.application_type_name = kwargs.get('application_type_name', None)
        self.current_application_type_version = kwargs.get('current_application_type_version', None)
        self.application_type_version = kwargs.get('application_type_version', None)
        self.upgrade_type = kwargs.get('upgrade_type', None)
        self.rolling_upgrade_mode = kwargs.get('rolling_upgrade_mode', None)
        self.failure_action = kwargs.get('failure_action', None)
        self.kind = 'ApplicationUpgradeStart'
