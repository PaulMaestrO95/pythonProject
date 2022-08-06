# Задание 1

geo_logs = [
	{'visit1': ['Москва', 'Россия']},
	{'visit2': ['Дели', 'Индия']},
	{'visit3': ['Владимир', 'Россия']},
	{'visit4': ['Лиссабон', 'Португалия']},
	{'visit5': ['Париж', 'Франция']},
	{'visit6': ['Лиссабон', 'Португалия']},
	{'visit7': ['Тула', 'Россия']},
	{'visit8': ['Тула', 'Россия']},
	{'visit9': ['Курск', 'Россия']},
	{'visit10': ['Архангельск', 'Россия']}
]

new_geo_logs = []

for visits in geo_logs:
	for visit, country in visits.items():
		if 'Россия' in country:
			new_geo_logs.append(visits)

print(new_geo_logs)

# Задание 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_id = []
newlist = []

for user, id in ids.items():
	id = set(id)
	unique_id.append(id)

for i in unique_id:
	for j in i:
		newlist.append(j)

newlist = set(newlist)
newlist = list(newlist)
print(newlist)

# Задание 3

queries = [
	'смотреть сериалы онлайн',
	'новости спорта',
	'афиша кино',
	'курс доллара',
	'сериалы этим летом',
	'курс по питону',
	'сериалы про спорт',
	'погода',
	'игра престолов',
	'афиша кино',
	'курс по питону',
	'',
	'курс по питону',
	'курс по питону',
	'qwertyuiop asdfghjkl zxcvbnm test',
	''
]

numbers = {}

for requests in queries:
	words = requests.split()
	if len(words) in numbers.keys():
		numbers[len(words)] += 1
	else:
		numbers.update({len(words): 1})

for key, value in numbers.items():
	percent = round((value / len(queries)) * 100, 2)
	print(f'Поисковых запросов из {key}: {percent}% (запросов - {value})')

# Задание 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98, }

x = []
for v in stats.values():
	x.append(v)
y = (max(x))

new_dict = {}
for k, v in stats.items():
	new_dict[v] = k

print(f'{new_dict[y]}')

