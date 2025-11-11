from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date = datetime(2025,1,1),
     schedule = '@daily',
     catchup= False)
def three_taask():
    @task
    def task_a():
        print('You are in Task A now')

    @task
    def task_b():
        print('You are in task B now')
    
    @task
    def task_c():
        print('You are in task C now')
    
    a_task= task_a()
    b_task = task_b()
    c_task = task_c()

    a_task >> c_task >> b_task

three_taask()