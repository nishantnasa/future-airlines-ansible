# Role Name

This role is used to deploy ansible in AWS using a min 1 max 1 ASG

This role has an extra task set:

 - set_dns

You can use this by adding the parameter `create_or_destroy=set_dns` to your
ansible-playbook command.  It queries for all instances with Type:ansible and then
picks the newest instance and sets ansible.future-airlines.net to that private IP
address.

You can use it after deploying a new ansible ASG and confirmed everything is working
as expected.

## Requirements

None

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## License

Commercial

## Author Information

Rob White (rob.white@future-airlines.com)
