"""
TCP: Transmission Control Protocol
- Langsamer als UDP
- zuverlässig
- USE Cases: Chat, Email, FTP, Datenaustausch, etc.
"""

import socket 

print("Server Side TCP (Listner, Receiver)")
print("~" * 50)

# socket.AF_INET : IPV4
# socket.SOCK_STREAM : TCP 



# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "" # receive from all
port = 20000

s.bind((ip,port))

# Listen to the port
s.listen()

try:
   # Accept the connection from the client
   comm, addresse = s.accept() 
   
   while True:
       data = comm.recv(1024) # Data Buffer Size 
       
       if not data:
           comm.close()
           break 
       
       print(f"{data.decode()}")
       
       response_text = input("Answer: ")
       comm.send(response_text.encode())


except:
    print("Something wrong happend!") 

finally:
    s.close()