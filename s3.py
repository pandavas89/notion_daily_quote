import io
import os
import boto3
from openpyxl import load_workbook

# AWS S3 객체
class S3():
    # 환경 변수로부터 값을 받아오기
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    
    def read_quote(self, bucket: str, file_name: str) -> tuple:
        response = self.s3_client.get_object(Bucket=bucket, Key=file_name)
        status = response.get('ResponseMetadata', {}).get('HTTPStatusCode')
    
        if status == 200:
            target = load_workbook(io.BytesIO(response['Body'].read()))
            return True, target
        return False, [[]]