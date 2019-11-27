#!/usr/bin/python


def to_json_list_string(yaml_list):
    """
    We use yaml to define lists, for example, CIDR ranges. These lists are then used in json documents. Often the
    document needs a nice quoted json list. There is no straight forward way to do this in Ansible so we created
    this ansible filter.

    :yaml_list: list of items - each item in the list should be a string
    :return: a JSON compatible string - each item is doubled quoted and comma seperated
    """

    # In the end we want one long list of rules
    yaml_list_quoted = []

    for item in yaml_list:
        yaml_list_quoted.append("\"" + item + "\"")

    return ", ".join(yaml_list_quoted)


class FilterModule(object):

    def filters(self):
        return {
            'to_json_list_string': to_json_list_string
        }
