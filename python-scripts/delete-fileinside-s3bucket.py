import boto3
client=boto3.client("s3")
s3=boto3.resource("s3")
#Bucket='examplebucket-2234u4433-ayenco',

bucketname=input("enter bucket name to delete")
def delete_s3(bucketname):
    
    fileupload=s3.Bucket(bucketname).upload_file('command.md')
    s3.Object(bucketname,'command.md').delete()
    try:
         print(f"S3 bucket '{bucketname}' file successfully deleted")
         return  True
    except Exception as e:
        
        print(f"An error occurred while deleting the bucket")
        return None
delete_s3(bucketname)
