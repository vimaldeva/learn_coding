from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.bash import BashOperator


@dag(
    start_date = datetime(2025,1,1),
    schedule = '@daily',
    catchup = False)
def bash_dag():

    BashOperator(
        task_id="bash_task",
        bash_command='pwd',
    )
    
bash_dag()
