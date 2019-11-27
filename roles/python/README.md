# python

Role to install python version.  Defaults to python3 which is not installed by default in Amazon Linux 1/2.

Also installs the pip package manager.

We do not set python3 as the default here because python2 is required by important packages on AL 1/2 such as yum and grub. To use it you should
specify `python3` from the command line and `pip3` for pip package management.

## Requirements

Tested against Amazon Linux

## Role Variables

python_version - the version to install

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: python, python_version: 36 }

## License

Commercial

## Author Information

Rob White (rob.white@future-airlines.com)
