"""
UDP: User Datagram Protocol
- Schneller als TCP
- Nicht zuverlässig
- USE Cases: Streams (Audio, Video) , VOIP (Voice over IP)
"""

import socket 

print("Server Side UDP (Listner, Receiver)")
print("~" * 50)

# socket.AF_INET : IPV4
# socket.SOCK_DGRAM : UDP 



# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "" # receive from all
port = 12000


try:
    s.bind((ip,port))  # tuple of (ip, port)

    while True:
        data, add = s.recvfrom(1024) # waits for any messages
        print("Data:", data)
        print("Address:", add)

        print(f"{data.decode()}")

except:
    print("Something wrong happend!") 

finally:
    s.close()