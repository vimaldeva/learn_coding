from airflow.decorators import dag, task
import datetime as dt

@dag(
    start_date=dt.datetime(2025, 1, 1),
    schedule_interval='@daily',
    description='printing time',
    catchup=False
)
def current_time_dag():
    @task
    def print_time_task():
        now = dt.datetime.now()
        print(f'The current date is {now.date()}')
        print(f'The current timestamp is {now}')
    print_time_task()

current_time_dag()