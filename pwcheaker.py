pw = '123456'
i = 3
while True:
	pwenter = input('please enter your password: ')
	if pwenter == pw:
		print('log in success')
		break
	else:
		i = i - 1
		print('wrong password, you have', i,  'attempts')
		if i == 0:
			break
			
			
	

