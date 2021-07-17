import os
from twilio.rest import Client
from dotenv import load_dotenv
import sys


def send_sms(message):
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    if "-t" in opts:
        load_dotenv()
        sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth = os.environ.get('TWILIO_AUTH_TOKEN')
        phone = os.environ.get('PHONE')
        from_phone = os.environ.get('TWILIO_FROM_PHONE')

        if (not sid):
            print('No SID. Cannot text')
            return

        client = Client(sid, auth)

        message = client.messages.create(
            to=phone,
            from_=from_phone,
            body=message)
        print('SMS sent to {}'.format(phone))

    else:
        print('Do not send sms. No -t flag')
        return
