
import socket 

print("Clide Side TCP (Sender)")
print("~" * 50)

# socket.AF_INET : IPV4
# socket.SOCK_STREAM : TCP 



# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "localhost" # receive from all
port = 20000

# 1. Connect with server
s.connect((ip, port))


try:
    
    while True:
        message = input("Enter your message: ")
        
        s.send(message.encode())
        
        # Wait for an answer from the server
        answer = s.recv(1024)
        
        print(f"{answer.decode()}")


except:
    print("Something wrong happend!") 

finally:
    s.close()