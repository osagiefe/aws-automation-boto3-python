#please authnticate yourself in aws already  before running this code using aws cli

#aws configure allowing access_key and secret key with region to be inserted 
#Now confirm  authentication by running 
#aws s3 ls

import boto3
print("please enter your region")
Regions=input()
def cleanup_snapshots(Regions):
    ec2 = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    for region in regions:
        print(f"Cleaning up snapshots in {region}")
        ec2 = boto3.client('ec2')
        response = ec2.describe_snapshots(OwnerIds=['self'])
        snapshots = response['Snapshots']
        while snapshots:
            for snapshot in snapshots:
                print(f"Deleting snapshot {snapshot['SnapshotId']}")
                ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            response = ec2.describe_snapshots(OwnerIds=['self'])
            snapshots = response['Snapshots']
        print(f"Finished cleaning up snapshots in {region}")

if __name__ == '__main__':
    cleanup_snapshots(Regions)

