import sys
import subprocess

pwd = 0
while pwd < 10000:
	pin=str(pwd).zfill(4)
	s=subprocess.run('~/leviathan6 pin', shell=True)
	print(s)
	if 'Wrong' in s:
		print('Wrong pin : ',pwd)
	else:
		print(s)
		break
	pwd +=1
sys.exit()