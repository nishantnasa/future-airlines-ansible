# fa_infra_aws_ecs_cluster

Used to create AWS ECS cluster infrastructure. This includes an ASG for the ECS hosts and the ECS cluster itself.

## Requirements

You need to define a default AMI ID to use. This should be an AMI that has the ECS agent installed. Usually this AMI will of
been built with the fa_ecs_host role.

## Role Variables

create_or_destroy - whether to create or destroy the infrastructure
ami_id - AMI to use in ASG
type - added as a tag to the infrastructure to identify its type
instance_type - ec2 instance size
asg_min_size - asg minimum size
asg_max_size - asg maximum size
asg_desired_size - asg desired size (the ASG will initialise with this many instances)
allow_against_prod - allow this role to be run against the prod environment
cluster_id - the ECS cluster ID
remove_cluster - whether to remove the ECS cluster when destroying all infrastructure. Otherwise, just the ASG is removed.

## Dependencies

None

## Example Playbook

You need to define the variable `deploy_in_subnet` (either pub for public, pro for protected or pri for private) and also
the variable `channel` as it is used to construct the cluster name.

The example below will create a new ASG and ECS cluster.

```yaml
- hosts: local
  roles:
     - { role: fa_infra_aws_ecs_cluster, deploy_in_subnet=pro channel=lsl }
```

This role also contains a special `drain.yml` playbook. This playbook is used to set the status of existing ECS instances to 'DRAINING'.
This DRAINING status will stop new tasks being placed on the instance and move existing instances off.  This is required so that we can
then cleanly terminate the old ASG.

```yaml
- hosts: local
  roles:
     - { role: fa_infra_aws_ecs_cluster, deploy_in_subnet=pro channel=lsl create_or_destroy=drain }
```

An example call:
```bash
ansible-playbook -i inventories/aws deploy_role_local.yml -e "hosts=aws-account-qldev role_to_deplochay=fa_infra_aws_ecs_cluster use_sts=true env=dev channel=agw"
```

## License

Commercial

## Author Information

Rob White (rob.white@qantasloyalty.com)
