import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

def send_email(name, email, phone, product, message):
    try:
        receiver = os.getenv("RECEIVER_EMAIL")

        if not receiver:
            print("Missing RECEIVER_EMAIL in environment variables")
            return False

        body = f"""
        <h2>New Inquiry from PurePower Website</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Interested In:</strong> {product}</p>
        <p><strong>Message:</strong></p>
        <p>{message}</p>
        """

        params = {
            "from": "PurePower <onboarding@resend.dev>",
            "to": [receiver],
            "subject": f"PurePower Inquiry from {name}",
            "html": body,
        }

        resend.Emails.send(params)
        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False