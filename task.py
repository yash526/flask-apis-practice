import os
import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": "Yash Trivedi <mailgun@yash>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html },
        verify = False
        )

def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        #Code from action.html here
        render_template("email/action.html", username=username),
        )