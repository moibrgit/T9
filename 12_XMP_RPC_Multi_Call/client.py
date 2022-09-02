
import xmlrpc.client 

server = xmlrpc.client.ServerProxy("http://127.0.0.1:41000") # the address of the server

# Create a multi call requester
multicall = xmlrpc.client.MultiCall(server)



# Assign the requester the functions and the arguments
multicall.add(6, 4)
multicall.multiply(10, 5)

# Send the request as a Bundle and get results
results = multicall() # the results is an Iterator

# convert the iterator to a tuple
results = tuple(results)


# Print the results 
print(results)

print(f"Add: {results[0]} - Multiply: {results[1]}")
