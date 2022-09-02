
from xmlrpc.client import Server, ServerProxy


client = ServerProxy("http://127.0.0.1:40000") # the address of the server

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

total = client.add(num1, num2)

print("The total 1 is:", total)


total = client.multiply(num1, num2)
print("The total 2 is:", total)
