import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_simple_message(to, subject, body):
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": "Yash Trivedi <mailgun@yash>",
            "to": [to],
            "subject": subject,
            "text": body},
        verify = False
        )

def send_user_registration_email(email, username):
    return send_simple_message(
        to=email,
        subject="Successfully signed up",
        body=f"Hi {username}! You have successfully signed up to the Stores REST API."
    )