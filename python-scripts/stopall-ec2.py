import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

# Get all running instances
response = ec2.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)

instance_ids = [
    i["InstanceId"]
    for r in response["Reservations"]
    for i in r["Instances"]
]

# Be careful this stops all running instances

if instance_ids:
    print("Stopping:", instance_ids)
    ec2.stop_instances(InstanceIds=instance_ids)
    print("All running instances are stopping...")
else:
    print("No running instances found.")
