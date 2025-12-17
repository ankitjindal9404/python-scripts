#checking website and automatically getting mail status
import requests
import smtplib #for connecting to server and sending email
from email.message import EmailMessage #for email message
from dotenv import load_dotenv
import os


def email_sender(body):
    sender_email = "sendermail@gmail.com"
    sender_password = "google app password"
    receiver_email = "reciveremail@gmail.com"
    subject = "Website Status Update: Python Scripting Practice"

    msg = EmailMessage()

    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    smtp_server = "smtp.gmail.com"
    port = 587 # For STARTTLS

    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent sucessfully")
    except Exception as e:
        print(f"Error: {e}")

def website_checker(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        email_sender("EROR: Not able to fetch data from website.")
        return
    if 500 <= response.status_code < 600:
        print("ERROR: website is down becuase of server issue")
        email_sender("ERROR: website is down becuase of server issue")
    elif 400 <= response.status_code < 500:
        print("ERROR: website has issue from client side")
        email_sender("ERROR: website has issue from client side")
    else:
        print(response)
        print("website is up")
        email_sender("website is up")

website_checker("https://www.google.org/")
