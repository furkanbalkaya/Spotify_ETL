from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import sys

sys.path.insert(0, "~/<C:/Users/furka/OneDrive/Desktop/Repositories/Spotify_ETL/dag/spotify_etl.py>")

from spotify_etl import run_spotify_etl



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='spotify_etl',
    schedule_interval=timedelta(days=1),
    catchup=False
)

def just_a_function():
    print("I'm going to show you something :)")

run_etl = PythonOperator(
    task_id='spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl