import boto3

client = boto3.client('s3')
response = client.list_buckets(
    MaxBuckets=123,
    ContinuationToken='',
    Prefix='',
    BucketRegion='us-east-1'
)
buckets = response["Buckets"]
for buckt in buckets:
    bucket_name = buckt["Name"]
    print(bucket_name)
    #print(response)