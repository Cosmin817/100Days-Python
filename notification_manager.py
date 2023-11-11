from twilio.rest import Client


class NotificationManager(Client):
    def __init__(self):
        self.account_sid = 'ACb3ecdfb36ca582b3888fb1a11c62af5f'
        self.auth_token = '6274fd2ca9387f41703d443bfa41d6f0'
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_='+15673722701',
            body=message_body,
            to='+40749153818'
        )
        print(message.sid)