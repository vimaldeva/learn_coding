from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date = datetime(2025,1,1),
    schedule = '@daily',
    catchup = False)
def parameter_dag():

    @task
    def greet_task(in_val):
        print(f'How are you {in_val} !!!')
    
    a = greet_task("pandhi")

parameter_dag()

