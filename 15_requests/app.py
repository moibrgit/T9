import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


import requests


url = "https://imgs.xkcd.com/comics/python.png"


# Download a File
####################


response = requests.get(url) # the file is in a byte mode

if response.ok:
    with open("myimage.png", mode = "wb") as file:
        file.write(response.content)


print("Status Code: ",response.status_code)
print("OK ?: ",response.ok)
print("Header: ",response.headers)

print("Saved Successfully!")