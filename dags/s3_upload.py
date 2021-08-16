import  boto3
from boto3 import Session
from auth import ACCESS_KEY,SECRET_KEY

def pushS3():
    ''' pushing data to S3 bucket'''
    session = Session()
    credentials = session.get_credentials()
    client=boto3.client('s3',aws_access_key_id='AKIAVOAQA3636BTME5GY', aws_secret_access_key='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')

    client.create_bucket(Bucket='adam-airflow-test')

    with open("../data/data.csv", "rb") as f:
        client.upload_fileobj(f,'adam-airflow-test',"data.csv")

    print("Upload Completed")

pushS3()
