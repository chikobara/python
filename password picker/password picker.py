import random
import string
print('|{:^50}|'.format('Welcome to password picker'))
b = 0
while b == 0:
	password = []
	s = []
	asciiu = string.ascii_uppercase
	asciil = string.ascii_lowercase
	asciid = string.digits
	asciip = '!#$%&'
	for i in asciid:
		s.append(i)
	for i in asciip:
		s.append(i)
	for i in asciiu:
		s.append(i)
	for i in asciil:
		s.append(i)
	try:
		passlen = int(input('How many characters you want in your password ? (8-16 / or more) '))
		if passlen < 8:
			print('Pls enter a digit more than 8 or equal to ')
		else:
			while len(password) <= passlen:
				password += str(random.sample(s, passlen))
			pwd = ''.join(password)
			print(' \n your password is : \n ')
			print(*eval(pwd),sep="")

			onemore = input(' Do you want another password ? (y)/(n) ')
			if onemore == 'y':
				continue
			else:
				b += 1
				break
	except:
		continue