from airflow.decorators import task, dag
from datetime import datetime

@dag(
    start_date = datetime(2025,1,1),
    schedule = '@daily',
    catchup = False,
    tags = ['learning']
)

def taskflow():

    @task
    def task_a():
        print('Tast A')
        return 43
    
    @task
    def task_b(value):
        print("Task B")
        print(value)

    task_b(task_a())

taskflow()