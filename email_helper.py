import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def send_email(name, email, phone, product, message):
    try:
        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL")

        msg = MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = receiver
        msg["Subject"] = f"PurePower Inquiry from {name}"

        body = f"""
New inquiry from PurePower website!

Name: {name}
Email: {email}
Phone: {phone}
Interested In: {product}

Message:
{message}
        """

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, receiver, msg.as_string())
        server.quit()

        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False