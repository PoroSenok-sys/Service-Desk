"""Вспомогательная функция для отправки писем по почте"""
import smtplib
from email.mime.text import MIMEText

from src.config import settings


async def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.SERVICE_EMAIL
    msg["To"] = to_email
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("user@example.com", "password")
            server.send_message(msg)
    except Exception as e:
        return {
            "message": f"Error sending email: {e}"
        }
