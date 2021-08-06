pw = '123456'
i = 3
while i > 0:
	pwenter = input('please enter your password: ')
	if pwenter == pw:
		print('log in success')
		break
	else:
		i = i - 1
		if i > 0:
			print('wrong password, you still have', i,  'attempts')
		else:
			print('too many attempts, bye bye')
			break

			
			
	

