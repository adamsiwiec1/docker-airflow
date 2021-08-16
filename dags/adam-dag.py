from airflow.models.dag import dag
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from boto3 import Session, client
import auth
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from textwrap import dedent

@dag(start_date=days_ago(2))
def alison_bash_dag():
    t1=BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    This is adams dag documentation
    """
    )

    templated_command = dedent(
        """
    mkdir adamdag
    """
    )

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
    )

    t1 >> [t2, t3]

dag = alison_bash_dag()