#!/usr/bin/env python
import json
import boto3

def get_ec2_by_tag(tag_key, tag_value):
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_instances(
        Filters=[
            { 'Name': 'instance-state-name', 'Values': ['running'] },
            { 'Name': f'tag:{tag_key}', 'Values': [tag_value] }
        ]
    )

    instances = []
    reservations = response['Reservations']
    for reservation in reservations:
        instances.extend(reservation['Instances'])

    return instances


def get_public_ip_by_role(role: str) -> str:
    return get_ec2_by_tag("Role", role)[0]['PublicIpAddress']

def get_private_ip_by_role(role: str) -> str:
    return get_ec2_by_tag("Role", role)[0]['PrivateIpAddress']


def main():

    redis_primary_public_ip = get_public_ip_by_role('redis_primary')
    redis_secondary_public_ip = get_public_ip_by_role('redis_secondary')

    inventory = {
        "_meta": {
            "hostvars": {
                redis_primary_public_ip: {
                    'ansible_user': 'ec2-user',
                    'ansible_ssh_private_key_file': './cks.pem', 
                    'ansible_ssh_common_args': '-o StrictHostKeyChecking=no',
                    'redis_primary_private_ip': get_private_ip_by_role('redis_primary')
                },
                redis_secondary_public_ip: {
                    'ansible_user': 'ec2-user',
                    'ansible_ssh_private_key_file': './cks.pem', 
                    'ansible_ssh_common_args': '-o StrictHostKeyChecking=no',
                }
            },
        },

        'redis_primary': {
            'hosts': [redis_primary_public_ip]
        },
        'redis_secondary': {
            'hosts': [redis_secondary_public_ip]
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    main()