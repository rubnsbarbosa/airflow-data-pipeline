## Airflow Data Pipeline: S3 to Redshift

This project demonstrates an end-to-end data pipeline using Apache Airflow, where data is 
extracted from an S3 bucket, processed with Pandas, and then loaded into Amazon Redshift.

### Introduction

This repository provides an example of a data pipeline that:
1. Extracts a CSV file from an S3 bucket.
2. Loads the CSV content into a Pandas DataFrame.
3. Inserts the data into a table in Amazon Redshift.

### Prerequisites

- Python 3.8+
- Apache Airflow 2.0+
- LocalStack (for local development)

#### Virtual Environment

It's recommended to use a virtual environment for dependency management.

```bash
python3 -m venv .venv
.venv/bin/activate
```

### Airflow DAG

The Airflow DAG is responsible for orchestrating the data pipeline. Here’s a simplified example:

```python
@task
def run_data_pipeline():
    try:
        data = extract_data_from_s3()
        load_data_into_redshift(data)

    except Exception as e:
        raise AirflowException(f"Airflow raised the exception: {e}")


(init >> run_data_pipeline() >> done)
```

### Usage

1. Activate the Virtual Environment.
2. Set Environment Variables.
3. Run Airflow (Start Airflow webserver).
4. Trigger the DAG on the Airflow UI.

### License

This project is licensed under the MIT License.
