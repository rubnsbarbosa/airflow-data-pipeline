import os
import sys
import boto3
import logging
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
from io import StringIO

from config_utils import Config

sys.path.insert(1, os.path.dirname(__file__))

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


def extract_data_from_s3():
    config = Config()
    s3 = boto3.client("s3",
                      endpoint_url=config.localstack_endpoint,
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key
                      )

    logger.info("list objects in the s3 bucket")
    response = s3.list_objects_v2(Bucket=config.s3_bucket_name)
    logger.debug(response)

    resp_s3_object = s3.get_object(Bucket=config.s3_bucket_name, Key=config.s3_file_key)
    csv_content = resp_s3_object["Body"].read().decode("utf-8")
    logger.debug(f"csv content:  {csv_content}")

    return csv_content


def load_data_into_redshift(csv_content):
    config = Config()
    logger.info(f"load the .csv content into a pandas dataframe")
    df = pd.read_csv(StringIO(csv_content), header=None)

    engine = create_engine(
        f'postgresql://{config.redshift_username}:{config.redshift_password}@'
        f'{config.redshift_hostname}:{config.redshift_port}/{config.redshift_database}')

    conn = engine.connect()

    df.to_sql(conn.redshift_table, engine, index=False, if_exists="replace")

    conn.close()
