import random
import string
print('|{:^50}|'.format('Welcome to password picker'))
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
    passlen = int(input('How many characters you want in your password ? (8-16) '))
    if passlen < 8:
        print('Pls enter a digit more than 8 or equal to ')
    else:
        pass
passlen = int(passlen)
while len(password) <= passlen:
	password += str(random.sample(s, passlen))
pwd = ''.join(password)
print('\n \n \n your password is : \n ', pwd)
print(*eval(pwd),sep="")