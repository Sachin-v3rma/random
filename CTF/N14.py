#!/bin/python
import requests

username = "natas14"
pwd = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
url = f"http://{username}.natas.labs.overthewire.org/"
session = requests.Session()
response = session.get(url,auth=(username,pwd))
#response = session.post(url,data={},auth=(username,pwd))
content=response.text
print(content)