import smtplib
import json
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template


class EMailClient:
    def __init__(self,provider=None) -> None:
        if provider == "hotmail":
            self.smtp_server = "smtp-mail.outlook.com"
            self.smtp_port = 587
        elif provider == "gmail":
            self.smtp_server = "smtp.gmail.com"
            self.smtp_port = 587
        elif provider == "webde":
            self.smtp_server = "smtp.web.de"
            self.smtp_port = 587
        elif provider is None:
            self.smtp_server = config.smtp_server
            self.smtp_port = config.smtp_port
    
    def send_mail(self,receiver, subject, message):
            
        # E-Mail Container Instnace
        message = MIMEMultipart()

        # E-Mail Meta Data
        message["from"] = config.email_username
        message["to"] = receiver
        message["subject"] = subject

        

        # Body
        message.attach(MIMEText(message))

        try:
            with smtplib.SMTP(host = self.smtp_server, port = self.smtp_port) as smtp:
                smtp.ehlo() # start the connect
                smtp.starttls()  # start the encryption
                smtp.login(config.email_username, config.email_password)
                smtp.send_message(message)
                
                print("Sent Successfully..!")


        except Exception as ex:
            print("Something went wrong", ex)

    def send_mail_with_attachments(self):
        pass
    
    




if __name__ == "__main__":
    email_client = EMailClient()
    #email_client.send_mail()