import boto3
from botocore.exceptions import ClientError
import os
import json
from sentry_sdk import capture_exception

from .constants import AWS_REGION
from .constants import AWS_SECRET_ACCESS_KEY
from .constants import AWS_ACCESS_KEY_ID
from .constants import AWS_TOPIC_SNS


class Notify:

    @staticmethod
    def sns(kwargs: dict):
        """
        send a notification via sns
        """
        topicArn = AWS_TOPIC_SNS
        snsClient = boto3.client(
            'sns',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )

        try:

            snsClient.publish(
                TargetArn=topicArn,
                Message=json.dumps(kwargs),
                Subject="Change Products",
            )

            return
        except Exception as e:
            capture_exception(e)

    @staticmethod
    def email(kwargs, email_admin: str):
        """."""

        SENDER = os.environ.get('EMAIL_NOTIFY_CHANGES', 'test@test.com')
        RECIPIENT = email_admin

        CONFIGURATION_SET = "ConfigSet"

        AWS_REGION = AWS_REGION

        SUBJECT = "Update Products"

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = kwargs

        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>Changes Update Product</h1>
        <p>
        </p>
        </body>
        </html>
                    """

        CHARSET = "UTF-8"
        client = boto3.client('ses', region_name=AWS_REGION)

        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                ConfigurationSetName=CONFIGURATION_SET,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
