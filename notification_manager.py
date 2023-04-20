from twilio.rest import Client
import smtplib

TWILIO_SID = "-"
TWILIO_AUTH_TOKEN = "-"
TWILIO_NUMBER = "-"

MY_NUMBER = "-"

# Email
MY_EMAIL = "-"
MY_PASSWORD = "-"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, text):

        message = self.client.messages.create(body=text, from_=TWILIO_NUMBER, to=MY_NUMBER)
        print(message.status)

    def send_email(self, message, to_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:Cheap Flight Found\n\n{message}".
                                encode("utf-8"))


