# Задача 1

HELP = """
Список доступных комманд:  
p - отобразить имя, которому принадлежит номер документа 
s - отобразить номер полки, на котором лежит номер документа
l - отобразить список документов, содержащихся в списке documents
a - добавить новый документ в список documents на определенную полку
d - удалить документ из списка documents и из полки
m - перенести номер документа из одной полки в другую
as - создать новую полку
quit - завершить программу
"""

documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}


def find_people():
	number = input('Ввведите номер документа: \n')
	for document in documents:
		if document.get('number') == number:
			return document.get('name')
	return 'Такого документа нет'


def find_shelf():
	number = input('Ввведите номер документа: \n')
	for key in directories:
		if number in directories.get(key):
			return key
	return 'Такого документа нет'


def find_list():
	for document in documents:
		print(f"{document['type']} {document['number']} {document['name']}")
	return ''


def add_document():
	shelf = input('В какую полку добавить документ? \n')
	if shelf not in directories:
		return 'Такой полки нет'
	doc_number = input("Введите номер документа: \n")
	if doc_number in sum(directories.values(), []):
		return 'Такой документ уже есть'
	doc_type = input("Введите тип документа: \n")
	doc_name = input("Введите имя владельца документа: \n")
	new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
	documents.append(new_doc)
	directories[shelf] += [doc_number]
	return 'Документ добавлен'


def delete_document():
	number = input('Введите номер документа: \n')
	for document in documents:
		if document.get('number') == number:
			documents.remove(document)
	for key, value in directories.items():
		if number in value:
			value.remove(number)
			return 'Документ удалён'
	return 'Такого документа нет'


def transfer_document():
	number_doc = input('Введите номер документа: \n')
	if number_doc in sum(directories.values(), []):
		shelf_transfer = input('Введите нужную полку: \n')
		if shelf_transfer not in directories.keys():
			return 'Такой полки нет'
		for key, value in directories.items():
			if number_doc in value:
				value.remove(number_doc)
				directories[shelf_transfer] += [number_doc]
		return 'Документ перемещен'
	return 'Такого документа нет'


def new_shell():
	new_dict = input('Введите номер новой полки: \n')
	if new_dict in directories.keys():
		return 'Полка уже существует'
	else:
		directories[new_dict] = []
		return 'Полка добавлена'


def help():
	print(HELP)


def main():
	while True:
		print('Доступные команды: p, s, l, a, d, m, as, quit, help')
		command = input('Введите название команды: \n').lower()
		if command == 'p':
			print(find_people())
		elif command == 's':
			print(find_shelf())
		elif command == 'l':
			print(find_list())
		elif command == 'a':
			print(add_document())
		elif command == 'd':
			print(delete_document())
		elif command == 'm':
			print(transfer_document())
		elif command == 'as':
			print(new_shell())
		elif command == 'quit':
			break
		elif command == 'help':
			help()
		else:
			print('Ввели неправильную команду, желаете завершить сеанс? y/n \n')
			answer = input('').lower()
			if answer == 'y':
				print('До свидания!')
				break


if __name__ == "__main__":
	main()
