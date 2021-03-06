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


class DiagnosticSettingsResourceCollection(Model):
    """Represents a collection of alert rule resources.

    :param value: The collection of diagnostic settings resources;.
    :type value: list[~azure.mgmt.monitor.models.DiagnosticSettingsResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DiagnosticSettingsResource]'},
    }

    def __init__(self, **kwargs):
        super(DiagnosticSettingsResourceCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
