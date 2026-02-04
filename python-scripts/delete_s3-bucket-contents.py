import boto3

client = boto3.client('s3', Region='eu-west-2')
response = client.list_buckets()
print(response)
for bucket in response['Buckets']:
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(bucket['Name'])
    bucket_versioning = s3.BucketVersioning(bucket['Name'])
    if bucket_versioning.status == 'Enabled':
        s3_bucket.object_versions.delete()
    else:
        s3_bucket.objects.all().delete()
    response = client.delete_bucket(Bucket=bucket['Name'])