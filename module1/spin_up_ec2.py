import re
import boto3
import pprint
import time


def create_ec2_instance(session: boto3.Session):
    """Create an EC2 instance absed on given session

    Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances

    Args:
        session (boto3.Session): Boto3 session

    Returns:
        dict: EC2 create request response
    """
    ec2 = session.client('ec2')
    return ec2.run_instances(
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': 8,
                        'VolumeType': 'gp2'
                    },
                },
            ],
            ImageId='ami-0d5eff06f840b45e9',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'test101'
                        },
                    ]
                },
            ],
        )


def terminate_ec2_instance(session: boto3.Session, instance_ids: list):
    """Ternimate given EC2 instance

    Args:
        session (boto3.Session): Boto3 session object
        instance_id: EC2 instance ids in list format

    Returns:
        dict: EC2 terminate request response
    """
    ec2 = session.client('ec2')
    return ec2.terminate_instances(InstanceIds=instance_ids, DryRun=False)


if __name__ == '__main__':
    # Create a boto3 session
    session = boto3.Session(profile_name='tomo')

    # Create an EC2 instance
    response = create_ec2_instance(session)
    instance_id = response['Instances'][0]['InstanceId']
    print(f'New instance id is {instance_id}')

    print('Sleep for 60 seconds')
    time.sleep(60)

    # Terminate given EC2 instance
    instance_ids = []
    instance_ids.append(instance_id)
    response = terminate_ec2_instance(session, instance_ids)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f'Terminate {instance_ids} successful!')
        pprint.pprint(response['TerminatingInstances'])