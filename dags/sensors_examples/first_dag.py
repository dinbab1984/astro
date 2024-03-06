from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2024,3,1),
    description="sensors dag 1",
    tags=['sensors'],
    catchup=False
)
def sensors_first_dag():
    wait_for_files = FileSensor.partial(
        task_id='wait_for_files',
        fs_conn_id='fs_default',
        mode='reschedule'
    ).expand(
        filepath=['data_1.csv','data_2.csv','data_3.csv']
    )

    @task
    def process_file():
        print('processed te file!')
    
    wait_for_files >> process_file()

sensors_first_dag()