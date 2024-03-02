from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain


@dag(start_date=datetime(2024,3,1),
     description="my first ever dag man", tags=['practice'],
     schedule='@daily', catchup=False)
def my_first_dag():
     @task
     def task_1():
          print("hello from dag1 --> task 1")
     @task
     def task_2():
          print("hello from task 2")
     @task
     def task_3():
          print("hello from task 3")
     @task
     def task_4():
          print("hello from task 4")
     @task
     def task_5():
          print("hello from task 5")
     
     chain(task_1() , [task_2() , task_3() ], [task_4() , task_5()])

my_first_dag()