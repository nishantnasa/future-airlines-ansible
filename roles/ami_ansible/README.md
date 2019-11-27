# ami_ansible

Used to install and configure Ansible.

## Requirements

Extends the 'ansible' role to provide QL specific function

## Role Variables

None

## Dependencies

* python
* common_linux
* ansible

## Example Playbook

Just apply the role, no vars required:

    - hosts: servers
      roles:
        - { role: ami_ansible }

## License

Open Source

## Author Information

Nishant Nasa (nishant.nasa@gmail.com)
