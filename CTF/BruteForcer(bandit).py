for i in range(0,10000):
	if len(str(i)) < 4:
		if len(str(i)) == 1:
			i = '000' + str(i)
		if len(str(i)) == 2:
			i = '00' + str(i)
		if len(str(i)) == 3:
			i = '0' + str(i)
	print(i)
	