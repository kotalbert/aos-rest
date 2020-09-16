"""Aws utilities for project resource management"""
import logging
from typing import List

import boto3
from mypy_boto3_s3.service_resource import Bucket, S3ServiceResource, BucketObjectsCollection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aws")


# indicate aws profile for this session

def get_s3_client() -> S3ServiceResource:
    """Create s3 resource with aos-app session credentials.
    Credentials should be downloaded from IAM console and configured
    in .aws/credentials file.
    """
    aos_session = boto3.session.Session(profile_name='aos-app')

    resource = aos_session.resource('s3')
    logger.info("{0} created.".format(str(resource)))
    return resource


def get_s3_bucket_resource(bucket_name: str) -> Bucket:
    """Create bucket resource, using client with `aos-app` session."""
    s3 = get_s3_client()
    bucket = s3.Bucket(bucket_name)
    logger.info("{0} created.".format(str(bucket)))
    return bucket


def get_bucket_object_keys(bucket: Bucket) -> List[str]:
    """Get list of objects keys in the bucket"""
    all_objects: BucketObjectsCollection = bucket.objects.all()
    return [obj.key for obj in all_objects]


def put_to_bucket(bucket: Bucket, filename: str, filename_part_to_include: int = 1) -> bool:
    """
    Put file to bucket

    :param bucket:  bucket resource
    :param filename: filename to be put to s3
    :param filename_part_to_include: optional, how many filename parts to include
    in object key in the bucket. defaults to 1, which means that only the file will
    be object key.
    :return: true if upload successfull
    """
    key = create_object_key(filename, filename_part_to_include)
    try:
        bucket.upload_file(filename, key)
        return True
    except Exception as e:
        logger.error(f"Error putting {filename} to {str(bucket)}.")
        return False


def create_object_key(filename, filename_part_to_include):
    """
    Create object key based on filename and how many parts of filename to include.
    :param filename:
    :param filename_part_to_include:
    :return:
    """
    elements = filename.split('/')[-filename_part_to_include:]
    join = '/'.join(elements)
    return join


# todo: download feature for individual files
# todo: download feature for files matching pattern.

if __name__ == '__main__':
    bucket = get_s3_bucket_resource('aos-app-develop')
    assert put_to_bucket(bucket, '../resources/test_file.txt')
    assert put_to_bucket(bucket, '../resources/dir1/test_file_in_dir.txt', 2)
    print(get_bucket_object_keys(bucket))
