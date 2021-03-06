import requests

s=requests.Session()
r = s.post('http://10.10.188.201/#/search?q=a')
print(r.url)
print(r.headers)
print(r.cookies)
