from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2024,3,1),
    description='sensors second day',
    tags=['sensors'],
    catchup=False
)
def sensors_second_dag():

    @task
    def runme():
        print("Hi from runme")
    
    runme()

sensors_second_dag()