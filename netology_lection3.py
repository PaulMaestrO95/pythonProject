# Задача 1

boys = ['Дима', 'Паша', 'Алекс', 'Витя', 'Кирилл', 'Артур', 'Петя', 'Вася']
girls = ['Арина', 'Маша', 'Катя', 'Даша', 'Ира', 'Алена', 'Вера', 'Ксюша']

boys.sort()
girls.sort()

if len(boys) == len(girls):
	for boy, girl in zip(boys, girls):
		print(f'{boy} и {girl}')
else:
	print('Кто-то может остаться без пары!')


