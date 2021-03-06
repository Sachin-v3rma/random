#!/bin/python
import requests

username = input('Username :')
pwd = input('Password :')
url = f"http://{username}.natas.labs.overthewire.org"
#headers={'referer':'http://natas5.natas.labs.overthewire.org/'}
response = requests.get(url,auth=(username,pwd))
print(response.text)