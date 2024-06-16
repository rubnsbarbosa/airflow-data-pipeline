#!/bin/bash
bucket_name="your-bucket-name"

echo "making bucket..."
aws s3 mb s3://$bucket_name

echo "copying iris dataset to bucket s3"
aws s3 cp file.csv s3://$bucket_name/

echo "listing buckets..."
aws s3 ls
