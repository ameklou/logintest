from sendsms.backends.base import BaseSmsBackend
from twilio.rest import Client

account_sid = 'ACb85dd575fa2b4b0f0bd3d9626e4da14e'
api_key = 'SK89dcfa490e6ae1a54e0bf5edb0314ae2'
api_secret = 'rCAl1vQjBUQrNPgR98opabPJ6DArx85J'
client = Client(api_key, api_secret, account_sid)


class AwesomeSmsBackend(BaseSmsBackend):
    def send_messages(self, message):
        #print(message[0].to)
        messag = client.messages.create(
                                       body=message[0].body,
                                       from_='+12526801215',
                                       to=message[0].to
                                   )

        print(messag.sid)
