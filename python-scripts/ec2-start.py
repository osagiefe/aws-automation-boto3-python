import boto3

print("Please enter your region")
region=input()

ec2 = boto3.client("ec2", region_name=region)

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

# Start instances if any are found
if ids:
    ec2.start_instances(InstanceIds=ids)
    print("Started instances:", ids)
else:
    print("No instances found with tag Env=dev")