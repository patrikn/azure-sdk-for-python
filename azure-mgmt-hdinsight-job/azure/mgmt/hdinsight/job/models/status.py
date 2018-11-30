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


class Status(Model):
    """Gets or sets the object containing the job status information.

    :param cleanup_progress: The progress made on the cleanup.
    :type cleanup_progress: float
    :param failure_info: The information about any failures that have
     occurred.
    :type failure_info: str
    :param finish_time: The time at which the job completed. It is an integer
     in milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00.
    :type finish_time: long
    :param history_file: The history file of the job.
    :type history_file: str
    :param job_ac_ls: The ACLs of the job.
    :type job_ac_ls: object
    :param job_complete: Whether or not the job has completed.
    :type job_complete: bool
    :param job_file: The job configuration file.
    :type job_file: str
    :param job_id: The full ID of the job.
    :type job_id: str
    :param job_id1: The ID of the job.
    :type job_id1: ~azure.mgmt.hdinsight.job.models.JobID
    :param job_name: The user-specified job name.
    :type job_name: str
    :param job_priority: The priority of the job.
    :type job_priority: str
    :param map_progress: The progress made on the maps.
    :type map_progress: float
    :param needed_mem: The amount of memory needed for the job.
    :type needed_mem: long
    :param num_reserved_slots: The number of slots reserved.
    :type num_reserved_slots: int
    :param num_used_slots: The number of slots used for the job.
    :type num_used_slots: int
    :param priority: The priority of the job.
    :type priority: str
    :param queue: The job queue name.
    :type queue: str
    :param reduce_progress: The progress made on the reduces.
    :type reduce_progress: float
    :param reserved_mem: The amount of memory reserved for the job.
    :type reserved_mem: long
    :param retired: Whether or not the job has been retired.
    :type retired: bool
    :param run_state: The current state of the job.
    :type run_state: int
    :param scheduling_info: The information about the scheduling of the job.
    :type scheduling_info: str
    :param setup_progress: The progress made on the setup.
    :type setup_progress: float
    :param start_time: The time at which the job started. It is an integer in
     milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00.
    :type start_time: long
    :param state: The state of the job.
    :type state: str
    :param tracking_url: The link to the web-ui for details of the job.
    :type tracking_url: str
    :param uber: Whether job running in uber mode.
    :type uber: bool
    :param used_mem: The amount of memory used by the job.
    :type used_mem: long
    :param username: The userid of the person who submitted the job.
    :type username: str
    """

    _attribute_map = {
        'cleanup_progress': {'key': 'cleanupProgress', 'type': 'float'},
        'failure_info': {'key': 'failureInfo', 'type': 'str'},
        'finish_time': {'key': 'finishTime', 'type': 'long'},
        'history_file': {'key': 'historyFile', 'type': 'str'},
        'job_ac_ls': {'key': 'jobACLs', 'type': 'object'},
        'job_complete': {'key': 'jobComplete', 'type': 'bool'},
        'job_file': {'key': 'jobFile', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'job_id1': {'key': 'jobID', 'type': 'JobID'},
        'job_name': {'key': 'jobName', 'type': 'str'},
        'job_priority': {'key': 'jobPriority', 'type': 'str'},
        'map_progress': {'key': 'mapProgress', 'type': 'float'},
        'needed_mem': {'key': 'neededMem', 'type': 'long'},
        'num_reserved_slots': {'key': 'numReservedSlots', 'type': 'int'},
        'num_used_slots': {'key': 'numUsedSlots', 'type': 'int'},
        'priority': {'key': 'priority', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'reduce_progress': {'key': 'reduceProgress', 'type': 'float'},
        'reserved_mem': {'key': 'reservedMem', 'type': 'long'},
        'retired': {'key': 'retired', 'type': 'bool'},
        'run_state': {'key': 'runState', 'type': 'int'},
        'scheduling_info': {'key': 'schedulingInfo', 'type': 'str'},
        'setup_progress': {'key': 'setupProgress', 'type': 'float'},
        'start_time': {'key': 'startTime', 'type': 'long'},
        'state': {'key': 'state', 'type': 'str'},
        'tracking_url': {'key': 'trackingUrl', 'type': 'str'},
        'uber': {'key': 'uber', 'type': 'bool'},
        'used_mem': {'key': 'usedMem', 'type': 'long'},
        'username': {'key': 'username', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)
        self.cleanup_progress = kwargs.get('cleanup_progress', None)
        self.failure_info = kwargs.get('failure_info', None)
        self.finish_time = kwargs.get('finish_time', None)
        self.history_file = kwargs.get('history_file', None)
        self.job_ac_ls = kwargs.get('job_ac_ls', None)
        self.job_complete = kwargs.get('job_complete', None)
        self.job_file = kwargs.get('job_file', None)
        self.job_id = kwargs.get('job_id', None)
        self.job_id1 = kwargs.get('job_id1', None)
        self.job_name = kwargs.get('job_name', None)
        self.job_priority = kwargs.get('job_priority', None)
        self.map_progress = kwargs.get('map_progress', None)
        self.needed_mem = kwargs.get('needed_mem', None)
        self.num_reserved_slots = kwargs.get('num_reserved_slots', None)
        self.num_used_slots = kwargs.get('num_used_slots', None)
        self.priority = kwargs.get('priority', None)
        self.queue = kwargs.get('queue', None)
        self.reduce_progress = kwargs.get('reduce_progress', None)
        self.reserved_mem = kwargs.get('reserved_mem', None)
        self.retired = kwargs.get('retired', None)
        self.run_state = kwargs.get('run_state', None)
        self.scheduling_info = kwargs.get('scheduling_info', None)
        self.setup_progress = kwargs.get('setup_progress', None)
        self.start_time = kwargs.get('start_time', None)
        self.state = kwargs.get('state', None)
        self.tracking_url = kwargs.get('tracking_url', None)
        self.uber = kwargs.get('uber', None)
        self.used_mem = kwargs.get('used_mem', None)
        self.username = kwargs.get('username', None)
