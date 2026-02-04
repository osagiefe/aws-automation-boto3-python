import boto3
client=boto3.client("s3")
s3=boto3.resource("s3")
print("enter bucet name")
bucket_name=input()
print("enter your region")
region=input()
def create_s3_bucket(bucket_name,region):
    
    response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint':region,
    },
    )

    #print(response)
    # Specify the bucket name you wish to create
    try:
         print(f"S3 bucket with bucket name '{response}' created successfully")
         return True
    except Exception as e:
        
        print(f"An error occurred while creating the S3 bucket:")
        return None
    

create_s3_bucket(bucket_name,region)
oaq-nciw-cnp