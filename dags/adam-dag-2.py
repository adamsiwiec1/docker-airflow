from airflow.models.dag import dag
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago, datetime
from boto3 import Session, client
import auth
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from textwrap import dedent
import smtplib
from email.message import EmailMessage
import auth


def send_email():
    my_email='adam2.siwiec@gmail.com'

    to='adam2.siwiec@gmail.com'

    smtp_server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(my_email, auth.PASS)
    smtp_server.sendmail(my_email, to, 'hi')
    smtp_server.close()
    print("Email sent successfully!")


def print_hi():
    print('hi')

@dag(start_date=datetime.now())
def adam_email_dag_3():
    t1= PythonOperator (
        task_id='send_first_email',
        python_callable=send_email
    )

    t2 = PythonOperator(
        task_id='send_email',
        python_callable=send_email
    )

    t1 >> t2

dag = adam_email_dag_3()