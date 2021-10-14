import random
import math

print('|{:^50}|'.format('Rolling dice'))
rd = 'y'
while rd == 'y':
	print('Rolling dice.....')
	dice1 = random.randint(1,6)
	print('dice1 is : ', dice1)
	dice2 = random.randint(1,6)
	print('dice2 is : ', dice2)
	rd = input('|{:^50}|'.format('Want to roll the dice again (y / n) : '))
	rd = rd.lower()