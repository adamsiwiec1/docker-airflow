from airflow.models.dag import dag
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from boto3 import Session, client
import auth


@dag(start_date=days_ago(1))
def upload_to_s3():
    ''' pushing data to S3 bucket'''

    c = client('s3',aws_access_key_id=auth.ACCESS_KEY, aws_secret_access_key=auth.SECRET_KEY)

    c.create_bucket(Bucket='adam-airflow-test')

    with open("/data/data.csv", "rb") as f:
        c.upload_fileobj(f,'adam-airflow-test',"data.csv")

    print("Upload Completed")


dag = upload_to_s3()