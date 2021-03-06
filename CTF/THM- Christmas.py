import requests

data={'email':'Sting@sting.com','password':'Sting'}

s=requests.Session()
#r = s.post('http://10.10.144.68:3000/login',data=data)
#print(r.text)
print(s.cookies)

cook={'authid':'bWNpbnZlbnRvcnl2NGVyOWxsMSFzcw%3D%3D'}
r2=s.post('http://10.10.144.68:3000/home',cookies=cook)
print(s.cookies['authid'])
print(r2.text)
#U3Rpbmd2NGVyOWxsMSFzcw%3D%3D
#bWNpbnZlbnRvcnl2NGVyOWxsMSFzcw%3D%3D