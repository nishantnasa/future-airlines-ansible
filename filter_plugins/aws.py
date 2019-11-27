#!/usr/bin/python

from __future__ import division
from datetime import datetime, timedelta
from operator import itemgetter
from dateutil import parser
import random


def sec_group_helper(list_of_sec_group_rule_dicts):
    """
    a function that takes a list of dicts specifying AWS security group rules and turns it in to one long list that can
    be passed directly to ec2_group module. This means with_tems doesn't have to be used and purge_rules can be true
    ensuring the group can be fully managed by Ansible
    :param list_of_sec_group_rule_dicts: list of dicts - each dict contains the proto to use in the sec group rule along
    with the to port, from port and a list of CIDRs
    :return: a single list of sec group rules compatible with the ec2_group module
    """

    # In the end we want one long list of rules
    rule_list = []
    # Each list contains a dict. The dict represents a common set of rules for example, port 80 for a list of CIDRs
    for sec_group_dict in list_of_sec_group_rule_dicts:
        if 'cidrs' in sec_group_dict:
            for cidr_list in sec_group_dict['cidrs']:
                for cidr in cidr_list:
                    rule_dict = {}
                    rule_dict['proto'] = sec_group_dict['proto']
                    rule_dict['from_port'] = sec_group_dict['from_port']
                    rule_dict['to_port'] = sec_group_dict['to_port']

                    if 'rule_desc' in sec_group_dict:
                        rule_dict['rule_desc'] = sec_group_dict['rule_desc']
                    elif 'rule_desc' in cidr:
                        rule_dict['rule_desc'] = cidr['rule_desc']
                    else:
                        rule_dict['rule_desc'] = ""

                    rule_dict['cidr_ip'] = cidr['cidr_ip'] if 'cidr_ip' in cidr else cidr
                    rule_list.append(rule_dict)

        if 'group_ids' in sec_group_dict:
            for group_id_list in sec_group_dict['group_ids']:
                for group_id in group_id_list:
                    rule_dict = {}
                    rule_dict['proto'] = sec_group_dict['proto']
                    rule_dict['from_port'] = sec_group_dict['from_port']
                    rule_dict['to_port'] = sec_group_dict['to_port']

                    if 'rule_desc' in sec_group_dict:
                        rule_dict['rule_desc'] = sec_group_dict['rule_desc']
                    elif 'rule_desc' in group_id:
                        rule_dict['rule_desc'] = group_id['rule_desc']
                    else:
                        rule_dict['rule_desc'] = ""

                    rule_dict['group_id'] = group_id['group_id'] if 'group_id' in group_id else group_id
                    rule_list.append(rule_dict)

    return rule_list


def ecs_instance_filter(list_of_instances, filter_name, filter_value, filter_operation='equalto', return_percent=100):
    """
    Filter a list of ECS instances based on a filter name and value and also only return a percentage
    of these instances as specified by return_percent

    :param list_of_instances: a list of dicts. Each dict represents an ECS instance
    :param filter_name: the name of the attribute to filter on
    :param filter_value: the value of the attribute to filter on
    :param filter_operation: whether to compare as equal or not
    :param return_percent: the percentage of instances to return
    :return: a list of lists. Each sub-list will be a max of 10 items. The items are ECS instance dicts.
    """

    filtered_list = list()

    for instance in list_of_instances:
        for attribute in instance['attributes']:
            if filter_operation == 'equalto':
                if attribute['name'] == filter_name:
                    if attribute['value'] == filter_value:
                        filtered_list.append(instance)
            elif filter_operation == 'notequalto':
                if attribute['name'] == filter_name:
                    if attribute['value'] != filter_value:
                        filtered_list.append(instance)

    # Shuffle list
    random.shuffle(filtered_list)

    # Calculate how much we should slice the list by based on 'return_percent'
    slice_length = (return_percent / 100) * len(filtered_list)

    # Slice the list so it only contains the return percentage
    sliced_list = filtered_list[0:int(slice_length)]

    # The AWS API only supports changing the status for 10 instances at a time so return a list
    # of lists with each sub-list being no more than 10 items in length
    return [sliced_list[x:x+10] for x in range(0, len(sliced_list), 10)]


class FilterModule(object):

    def filters(self):
        return {
            'sec_group_helper': sec_group_helper,
            'ecs_instance_filter': ecs_instance_filter
        }
