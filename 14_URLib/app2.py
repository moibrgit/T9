import urllib.request
import urllib.parse

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)



url = "https://www.google.com/search?q=python"


headers = {}

try:
    headers["User-Agent"] = 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>'

    # Add the headers to the request
    req = urllib.request.Request(url, headers = headers)

    # Send the request to the target website
    response = urllib.request.urlopen(req)

    # Get the response from the website
    response_data = response.read()


    print(response_data)

    with open("result.html", mode = "w", encoding="UTF-8") as file:
        file.write(str(response_data))
except:
    print("Error...")
    
    