from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = "gauravkr648@gmail.com",
    MAIL_PASSWORD = "upsp asre wbrc sxlv",
    MAIL_FROM = "gauravkr648@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Gaurav Kumar",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_email(emails: List[str]):
    html = """<p>Hi, thanks for registration. Our team will connect with you soon.</p> """

    message = MessageSchema(
        subject="Registration Successful",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    print({"message": "email has been sent"})