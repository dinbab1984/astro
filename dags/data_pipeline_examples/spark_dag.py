from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG('spark_dag', start_date=datetime(2024,3,3), description="spark submit dag",
         schedule='@daily', tags=['spark'], catchup=False):
     ingestion = SparkSubmitOperator(
          task_id='ingestion'
          , application ='pyspark/ingestion.py' 
          , conn_id= 'spark_local'
          , verbose=False)

     ingestion