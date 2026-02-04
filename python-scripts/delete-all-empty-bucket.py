#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError


def bucket_region(s3_global, bucket_name: str) -> str:
    resp = s3_global.get_bucket_location(Bucket=bucket_name)
    loc = resp.get("LocationConstraint")
    if loc in (None, ""):
        return "us-east-1"
    if loc == "EU":
        return "eu-west-1"
    return loc


def is_bucket_empty(s3_regional, bucket_name: str) -> bool:
    # Check current objects
    obj = s3_regional.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
    if obj.get("KeyCount", 0) > 0:
        return False

    # Check versioned objects
    ver = s3_regional.get_bucket_versioning(Bucket=bucket_name)
    status = ver.get("Status")

    if status in ("Enabled", "Suspended"):
        vers = s3_regional.list_object_versions(Bucket=bucket_name, MaxKeys=1)
        if vers.get("Versions") or vers.get("DeleteMarkers"):
            return False

    return True


def delete_empty_buckets():
    s3_global = boto3.client("s3")

    buckets = s3_global.list_buckets().get("Buckets", [])
    if not buckets:
        print("No buckets found.")
        return

    deleted = 0
    skipped = 0

    for b in buckets:
        name = b["Name"]

        try:
            region = bucket_region(s3_global, name)
            s3_regional = boto3.client("s3", region_name=region)

            if not is_bucket_empty(s3_regional, name):
                skipped += 1
                continue

            s3_regional.delete_bucket(Bucket=name)
            deleted += 1
            print(f"Deleted empty bucket: {name} ({region})")

        except ClientError as e:
            code = e.response.get("Error", {}).get("Code", "Unknown")
            msg = e.response.get("Error", {}).get("Message", str(e))
            print(f"SKIP {name}: {code} - {msg}")
            skipped += 1

    print(f"\nDone. Deleted: {deleted}. Skipped: {skipped}")


if __name__ == "__main__":
    delete_empty_buckets()
