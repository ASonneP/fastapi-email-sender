from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("APP_PASSWORD")

def get_email_config():
    return ConnectionConfig(
        MAIL_USERNAME=SMTP_USER,
        MAIL_FROM=SMTP_USER,
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
        MAIL_PASSWORD=SMTP_PASSWORD
    )

class EmailSchema(BaseModel):
    receiver_email: str
    subject: str
    body: str

async def send_mail(email: EmailSchema):
    conf = get_email_config()
    fm = FastMail(conf)
    message = MessageSchema(
        subject=email.subject,
        recipients=[email.receiver_email],
        body=email.body,
        subtype="html"
    )
    await fm.send_message(message)

@app.post("/send-email/")
async def send_email(background_tasks: BackgroundTasks, email: EmailSchema):
    background_tasks.add_task(send_mail, email)
    return {"message": "Email has been sent!"}


