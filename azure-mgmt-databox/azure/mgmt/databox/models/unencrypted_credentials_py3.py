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


class UnencryptedCredentials(Model):
    """Unencrypted credentials for accessing device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar job_name: Name of the job.
    :vartype job_name: str
    :ivar job_secrets: Secrets related to this job.
    :vartype job_secrets: ~azure.mgmt.databox.models.JobSecrets
    """

    _validation = {
        'job_name': {'readonly': True},
        'job_secrets': {'readonly': True},
    }

    _attribute_map = {
        'job_name': {'key': 'jobName', 'type': 'str'},
        'job_secrets': {'key': 'jobSecrets', 'type': 'JobSecrets'},
    }

    def __init__(self, **kwargs) -> None:
        super(UnencryptedCredentials, self).__init__(**kwargs)
        self.job_name = None
        self.job_secrets = None