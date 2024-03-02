from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


def read_file():
    lambda: print(open('/tmp/dummy', 'rb').read())

with DAG('check_dag',start_date=datetime(2024,3,2), description='check dag - python and bash operator',
    schedule=timedelta(days=1), tags=['exercise'], catchup=False):
    create_file = BashOperator(task_id='create_file', bash_command='echo "Hi there!" >/tmp/dummy')
    check_file = BashOperator(task_id='check_file', bash_command='test -f /tmp/dummy')
    read_file = PythonOperator(task_id='read_file', python_callable=read_file)
    
    create_file >> check_file >> read_file

