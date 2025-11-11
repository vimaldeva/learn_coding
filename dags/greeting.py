from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator



@dag(
    start_date = datetime(2025,1,1),
    schedule= '@daily',
    catchup = False,
    description = 'Printing hello world')
def gretting():

    @task
    def greet_task():
        print('Hello World 2')
    greet_task()
gretting()

