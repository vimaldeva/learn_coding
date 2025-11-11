from airflow import DAG
from airflow.decorators import dag
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

# with DAG('learn_schedule', start_date = datetime(2025,11,1), 
#          schedule_interval = '@daily',
#          catup = False,

#          ) as dag:
    
@dag(start_date = datetime(2025,11,1), 
         schedule_interval = '@daily',
         catchup = False)
def empty_dag():
    ta = EmptyOperator(task_id = 'ta')

empty_dag()
