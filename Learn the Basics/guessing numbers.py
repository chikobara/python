import math
import random

def guess(x):
	randomnum = random.randint(1, x)
	tryings = 0
	guesses = 0
	while guesses != randomnum:
		try:
			guesses = int(input(f'guess a number between 1 and {x} : '))
		except:
			print('pls type a number')
		if guesses > randomnum:
			print('your guess is too high')
			tryings += 1
		elif guesses < randomnum:
			print('your guess is too low')
			tryings += 1
	tryings += 1
	print(f'Yeah! you did it in {tryings} times. ')

try:
	x = int(input('type a number higher than 1 : '))
except:
	print('pls type a number')

guess(x)