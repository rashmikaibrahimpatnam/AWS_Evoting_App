import boto3
import pdb
from online_election.config import ConfigParse

class SendSMS():
    def access_SNS(self):
        pdb.set_trace()
        keys = ConfigParse().fetch_keys()
        access_key_id = keys['access_key_id']
        secret_access_key = keys['secret_access_key']
        session_token = keys['session_token']
        region_name = keys['region_name']
        session = boto3.session.Session()
        client = session.client(
            service_name='sns',
            region_name=region_name,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token

        )

        # Send your sms message.
        client.publish(
            PhoneNumber="7828820696",
            Message="Hello Rashu"
        )
