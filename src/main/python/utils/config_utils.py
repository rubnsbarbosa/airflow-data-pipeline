import os
import sys
from airflow.utils import dates

sys.path.insert(1, os.path.dirname(__file__))


class DAGArgs:
    """
    A class that contains the arguments for an Airflow DAG
    """
    NAME = "el-pipeline-aws"
    DEFAULT = {"start_date": dates.days_ago(1), "retries": 0}


class Config:
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    s3_bucket_name = os.getenv("S3_BUCKET_NAME")
    s3_file_key = os.getenv("S3_FILE_KEY")
    localstack_endpoint = os.getenv("LOCALSTACK_ENDPOINT")
    # redshift
    redshift_username = os.getenv("REDSHIFT_USERNAME")
    redshift_password = os.getenv("REDSHIFT_PASSWORD")
    redshift_hostname = os.getenv("REDSHIFT_HOSTNAME")
    redshift_port = os.getenv("REDSHIFT_PORT")
    redshift_database = os.getenv("REDSHIFT_DATABASE")
    redshift_table = os.getenv("REDSHIFT_TABLE")
