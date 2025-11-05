from airflow import DAG
from datetime import datetime
with DAG('sample_dag',start_date= datetime(2024,1,1), 
         schedule_interval = '@daily', catchup= False) as dag :
    None