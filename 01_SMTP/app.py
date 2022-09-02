""" 
SMTP: Simple Mail Transfer Protocol
Only ASCII Encoding
"""

"""
MiMe Encoding: provides:

1. Special Charachter
2. Attachments
3. HTML Template

"""


import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os 
from pathlib import Path
os.chdir(Path(__file__).parent)

# Read Credential File

with open("./email.json", mode ="r", encoding="UTF-8") as file:
    content = file.read()

email_cred = json.loads(content)

# Define Credentials
hotmail_user = email_cred.get("username")
hotmail_pass = email_cred.get("password")


# E-Mail Container Instnace
message = MIMEMultipart()

# E-Mail Meta Data
message["from"] = hotmail_user
message["to"] = hotmail_user
message["subject"] = "MiMe WBS Test 100"

# Body
message.attach(MIMEText("This is a test email 100"))



try:
    with smtplib.SMTP(host = "smtp-mail.outlook.com", port = 587) as smtp:
        smtp.ehlo() # start the connect
        smtp.starttls()  # start the encryption
        smtp.login(hotmail_user, hotmail_pass)
        smtp.send_message(message)
        
        print("Sent Successfully..!")


except Exception as ex:
    print("Something went wrong", ex)


