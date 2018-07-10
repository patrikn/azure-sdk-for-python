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


class AnalysisEventMetadata(Model):
    """Metadata about an Analysis Event.

    :param delay: The analysis delay.
    :type delay: timedelta
    :param duration: The duration of analysis.
    :type duration: timedelta
    """

    _attribute_map = {
        'delay': {'key': 'Delay', 'type': 'duration'},
        'duration': {'key': 'Duration', 'type': 'duration'},
    }

    def __init__(self, *, delay=None, duration=None, **kwargs) -> None:
        super(AnalysisEventMetadata, self).__init__(**kwargs)
        self.delay = delay
        self.duration = duration