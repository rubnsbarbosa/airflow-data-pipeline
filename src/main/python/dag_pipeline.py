import os
import sys

from airflow.decorators import dag, task
from airflow.exceptions import AirflowException
from airflow.operators.empty import EmptyOperator

sys.path.insert(1, os.path.dirname(__file__))

from utils.config_utils import DAGArgs
from utils.aws_utils import extract_data_from_s3


@dag(dag_id=DAGArgs.NAME, schedule="@daily", catchup=False, default_args=DAGArgs.DEFAULT)
def data_pipeline_dag():
    init = EmptyOperator(task_id="init")

    @task
    def run_data_pipeline():
        try:
            data = extract_data_from_s3()

        except Exception as e:
            raise AirflowException(f"Airflow raised the exception: {e}")

    done = EmptyOperator(task_id="done")

    (init >> run_data_pipeline() >> done)


data_pipeline_dag()
