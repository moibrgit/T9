""" 
IMAP4: Internet Message Access Protocol Version4

- Server Oriented Storage
- Folder Structure (Mailboxes, Inbox, Outbox, etc.)
- Multi Device (PC, Mobile, Table, etc.)
"""


import os 
from pathlib import Path
os.chdir(Path(__file__).parent)

import imaplib 
import json


with open("./cred.json", mode = "r", encoding="UTF-8") as file:
    content  = file.read() 
    
jsondict = json.loads(content)   


email_username = jsondict["username"]
email_password = jsondict["password"]



SERVER = "outlook.office365.com"
PORT = 993

# Create an IMAP Connection
im = imaplib.IMAP4_SSL(SERVER, port = PORT)

# Login
im.login(email_username, email_password)


for mb in im.list()[1]:
    name = mb.split(b'"."')[-1]
    print(f"- {name.decode()}")
    
    
# Ask the user which Mailbox
user_mb = input("Which MailBox ? ")

im.select(user_mb)

# Read the E-Mails in the choosed Mailbox
status, data = im.search(None, "ALL")

print("Status:", status)
print("Data:", data)

for mailnr in data[0].split():
    typ, data = im.fetch(mailnr, "(RFC822)")
    print(f"{data[0][1].decode()} \n+++++++++\n")


im.close()
