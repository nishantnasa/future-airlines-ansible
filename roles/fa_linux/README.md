# fa_linux

This role is purely a metadata role to ease including "standard" roles.

For example, many roles like fa_jenkins and fa_ecs_host share the same 'must have' roles such as fa_common_linux, datadog etc.

Rather than modifying both of these roles when we add a new 'must have' role we just add it as a dependency in this role and then fa_jenkins etc just
have to require this fa_linux role.

## Requirements

N/A

## Role Variables

N/A

## Dependencies

All roles that are regarded as 'must have' should be a dependency of this role.

Currently that is:

- fa_common_linux
- fa_datadog
- python - should be installed first to upgrade OS to python3

## License

Commercial

## Author Information

Rob White (rob.white@future-airlines.com)
