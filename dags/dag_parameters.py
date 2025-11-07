from airflow import DAG
from datetime  import datetime, timedelta

with DAG('dag_parameters', 
         start_date = datetime(2025,1,1),
         schedule= '@daily',
         catchup  = False,
         description = "This DAG defines the different parametrs used in the DAG",
         tags = ["dag basics"],
         default_args = {"retries": 1},
         dagrun_timeout = timedelta(minutes=20) 
         ) as dag:
    pass

