

import socket 

print("Client Side UDP (Sender)")
print("~" * 50)

# socket.AF_INET : IPV4
# socket.SOCK_DGRAM : UDP 



# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "localhost" # IP of the server Localhost IP 127.0.0.1
port = 12000

# Create the message
message = input("Enter your message: ")

# Send the message
s.sendto(message.encode(), (ip,port))

# Close the socket
s.close()