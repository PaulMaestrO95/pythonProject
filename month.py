m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
day_month = range(1, 32)

month = input('Введите месяц \n').lower()

if month not in m:
  print('Неверное название месяца. Повторите ввод')
  print(f"{m}")
  month = input('Введите месяц \n').lower()

try:
  day = int(input('Введите число \n'))
  if day not in day_month:
    print('Неправильно ввели число. В месяце не более 31 дня.')
    day = int(input('Введите число \n'))
except ValueError:
  print('Введите число!')
  day = int(input('Введите число \n'))

if month == ('январь'):
  if day <= 20:
    print('Козерог')
  else:
    print('Водолей')
if month == ('февраль'):
  if day <= 18:
    print('Водолей')
  else:
    print('Рыбы')
if month == ('март'):
  if day <= 20:
    print('Рыбы')
  else:
    print('Овен')
if month == ('апрель'):
  if day <= 20:
    print('Овен')
  else:
    print('Телец')
if month == ('май'):
  if day <= 21:
    print('Телец')
  else:
    print('Близнецы')
if month == ('июнь'):
  if day <= 21:
    print('Близнецы')
  else:
    print('Рак')
if month == ('июль'):
  if day <= 22:
    print('Рак')
  else:
    print('Лев')
if month == ('август'):
  if day <= 23:
    print('Лев')
  else:
    print('Дева')
if month == ('сентябрь'):
  if day <= 22:
    print('Дева')
  else:
    print('Весы')
if month == ('октябрь'):
  if day <= 23:
    print('Весы')
  else:
    print('Скорпион')
if month == ('ноябрь'):
  if day <= 22:
    print('Скорпион')
  else:
    print('Стрелец')
if month == ('декабрь'):
  if day <= 21:
    print('Стрелец')
  else:
    print('Козерог')



