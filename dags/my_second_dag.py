from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain

def print_1():
    print("hello from task 1")
def print_2():
    print("hello from task 2")
def print_3():
    print("hello from task 3")
def print_4():
    print("hello from task 4")
def print_5():
    print("hello from task 5")

default_args = {
    'retries' : 3,
}
with DAG('my_second_dag', start_date=datetime(2024,3,1),
         description="my zrd ever dag man", tags=['practice'],
         schedule='@daily', catchup=False):
    task_1 = PythonOperator(task_id='task_1', python_callable=print_1)
    task_2 = PythonOperator(task_id='task_2', python_callable=print_2, retries=3)
    task_3 = PythonOperator(task_id='task_3', python_callable=print_3, retries=3)
    task_4 = PythonOperator(task_id='task_4', python_callable=print_4, retries=3)
    task_5 = PythonOperator(task_id='task_5', python_callable=print_5, retries=3)

    chain(task_1, [task_2, task_3], [task_4 ,task_5])