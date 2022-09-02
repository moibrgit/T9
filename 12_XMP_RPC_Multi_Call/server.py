"""
RPC: Remote Procedure Call
"""

from xmlrpc.server import SimpleXMLRPCServer as Server 

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y 


# Create a server with a tuple of IP and Port
srv = Server(   ("127.0.0.1", 41000) )

# Allow MultiCall
srv.register_multicall_functions()

# Register the functiosn to the server
srv.register_function(add, "add")
srv.register_function(multiply, "multiply")

# Start the server 
print("Starting the server.....")
srv.serve_forever()