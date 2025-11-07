from airflow.decorators import dag, task
from datetime import datetime
from random import randint

@dag(
    start_date = datetime(2025,1,1),
    schedule = '@daily',
    catchup = False,
    tags = ['learning']
)

def even_or_odd():

    @task
    def generate_random():
        print('Generating a random number ')
        a = randint(1,100)
        return a
    
    @task
    def identify_even(value):
        print('Identifying if the number is even or odd')
        if  value % 2 ==0 :
            print('The random value is even')
        else :
            print('The random value is odd')
    
    identify_even(generate_random())

even_or_odd()


