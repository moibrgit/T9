import urllib.request
import urllib.parse

x = urllib.request.urlopen("https://google.com")
print(x.read())
