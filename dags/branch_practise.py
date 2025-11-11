from airflow.decorators import dag, task
from datetime import datetime
from random import randint

@dag(
    start_date = datetime(2025,1,1),
    schedule = '@daily',
    catchup= False)
def branch_practise():
    
    @task
    def generate_number():
        a = randint(1,100)
        print(f'The generated random numner is {a}')
        return a
    
    @task
    def even_task():
        print('The generated number is even')
    
    @task
    def odd_task():
        print('the generated number is odd')

    @task.branch
    def vimal_choose_branch(in_value):
        if in_value %2 ==0:
            return "even_task"
        else :
            return "odd_task"
    
    number = generate_number()
    branch_node = vimal_choose_branch(number)
    odd_node = odd_task()
    even_node = even_task()

    branch_node >> [even_node, odd_node]


branch_practise()