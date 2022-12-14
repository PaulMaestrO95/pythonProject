# Задача 1

boys = ['Дима', 'Паша', 'Алекс', 'Витя', 'Кирилл', 'Артур', 'Петя', 'Вася']
girls = ['Арина', 'Маша', 'Катя', 'Даша', 'Ира', 'Алена', 'Вера', 'Ксюша']

if len(boys) == len(girls):
	boys.sort()
	girls.sort()
	for boy, girl in zip(boys, girls):
		print(f'{boy} и {girl}')
else:
	print('Кто-то может остаться без пары!')

# Задача 2
print()

cook_book = [
	['салат',
	 [
		 ['картофель', 100, 'гр.'],
		 ['морковь', 50, 'гр.'],
		 ['огурцы', 50, 'гр.'],
		 ['горошек', 30, 'гр.'],
		 ['майонез', 70, 'мл.'],
	 ]
	 ],
	['пицца',
	 [
		 ['сыр', 50, 'гр.'],
		 ['томаты', 50, 'гр.'],
		 ['тесто', 100, 'гр.'],
		 ['бекон', 30, 'гр.'],
		 ['колбаса', 30, 'гр.'],
		 ['грибы', 20, 'гр.'],
	 ],
	 ],
	['фруктовый десерт',
	 [
		 ['хурма', 60, 'гр.'],
		 ['киви', 60, 'гр.'],
		 ['творог', 60, 'гр.'],
		 ['сахар', 10, 'гр.'],
		 ['мед', 50, 'мл.'],
	 ]
	 ]
]

person = int(input('Введите количество гостей: \n'))

for recipe in cook_book:
	for ingredient in recipe[1]:
		print(f"{ingredient[0]}, {ingredient[1] * person}{ingredient[2]}")
