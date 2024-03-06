# test_module.py
from airflow.decorators import dag, task
import pendulum
from my_packages.packages_a.module_a import TestClass
from my_packages.packages_a.subpackage_a.subpackaged_module_a import TestClass1


@dag(schedule = None, start_date = pendulum.datetime(2023, 3, 1), catchup = False)

def test_module():

   @task
   def test_task():
       print(TestClass.my_time())

   @task
   def test_task1():
       print(TestClass1.my_time())

   test_task() >> test_task1()

dag = test_module()