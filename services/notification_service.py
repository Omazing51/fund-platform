import boto3
from core.config import settings

class NotificationService:
    def __init__(self):
        self.ses_client = boto3.client(
            "ses",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.region_name
        )
        self.email_source = settings.email_source  

    def send_email(self, to_email, subject, body):
        return self.ses_client.send_email(
            Source=self.email_source, 
            Destination={
                "ToAddresses": [to_email]
            },
            Message={
                "Subject": {"Data": subject},
                "Body": {
                    "Text": {"Data": body}
                }
            }
        )
