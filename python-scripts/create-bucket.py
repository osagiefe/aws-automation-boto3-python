import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name: str, region: str):
    s3 = boto3.client("s3", region_name=region)

    try:
        if region == "us-east-1":
            # us-east-1 must NOT include LocationConstraint
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )

        print(f"S3 bucket '{bucket_name}' created successfully in {region}")
        return True

    except ClientError as e:
        print("Failed to create bucket.")
        print(e.response.get("Error", {}))
        return False

bucket_name = input("Enter bucket name: ").strip()
region = input("Enter your region (e.g., us-east-1): ").strip()

create_s3_bucket(bucket_name, region)
