""" 
POP3: Post Office Protocol Version 3

- Client oriented storage
- No Folders
- No Multi-Device

"""

import os 
from pathlib import Path
os.chdir(Path(__file__).parent)

import poplib
import json 


with open("./cred.json", mode = "r", encoding="UTF-8") as file:
    content  = file.read() 
    
jsondict = json.loads(content)   


email_username = jsondict["username"]
email_password = jsondict["password"]



SERVER = "outlook.office365.com"
PORT = 995


pop = poplib.POP3_SSL(SERVER, port = PORT)

# Login
pop.user(email_username)
pop.pass_(email_password)


# Get Information about inbox
print(pop.stat())


# Loop Over the Mail

for i in range(1, pop.stat()[0] + 1):
    print(pop.retr(i)) # Tuple(answer , line , length)
    
    print("+" * 30 )
    
    for line in pop.retr(i)[1]:
        print(line)
        
    print("#" * 70 )
    
    
pop.quit()