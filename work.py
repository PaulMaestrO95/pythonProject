import random

while True:
	a = int(input('1 число \n'))
	b = int(input('2 число \n'))
	print('случайное число ' + str(random.randint(a, b)))
