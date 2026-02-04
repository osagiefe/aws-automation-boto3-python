import boto3
print("Please enter your region")
region=input()

ec2 = boto3.client("ec2", region_name=region)

response = ec2.describe_instances()

for r in response["Reservations"]:
    for i in r["Instances"]:
        name = "NoName"
        if "Tags" in i:
            for tag in i["Tags"]:
                if tag["Key"] == "Name":
                    name = tag["Value"]

        print(
            f"{i['InstanceId']} | {name} | {i['State']['Name']} | {i['Placement']['AvailabilityZone']}"
        )
