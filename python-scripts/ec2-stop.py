import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# Get instances with tag Env=dev
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Env',
            'Values': ['dev']
        }
    ]
)

# Extract instance IDs
ids = [
    instance['InstanceId']
    for reservation in response['Reservations']
    for instance in reservation['Instances']
]

# Stop instances if any are found
if ids:
    ec2.stop_instances(InstanceIds=ids)
    print("Stopped instances:", ids)
else:
    print("No instances found with tag Env=dev")
