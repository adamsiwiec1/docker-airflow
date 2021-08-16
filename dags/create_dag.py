import airflow
from airflow import DAG
from airflow.models.dag import dag
from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# with DAG("adam-dag") as dag:
#     op = DummyOperator(task_id="task")
#

@dag(start_date=days_ago(2))
def generate_dag():
    op = DummyOperator(task_id="task")

dag = generate_dag()

