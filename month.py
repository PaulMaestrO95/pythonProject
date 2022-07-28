m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
day_month = range(1, 32)

month = input('Введите месяц \n')
month1 = month.lower()

if month1 not in m:
  print('Неверное название месяца. Повторите ввод')
  print(f"{m}")
  month = input('Введите месяц \n')
  month1 = month.lower()

day = int(input('Введите число \n'))

if day not in day_month:
  print('Неправильно ввели число. В месяце не более 31 дня.')
  day = int(input('Введите число \n'))

if month1 == ('январь'):
  if day <= 20:
    print('Козерог')
  else:
    print('Водолей')
if month1 == ('февраль'):
  if day <= 18:
    print('Водолей')
  else:
    print('Рыбы')
if month1 == ('март'):
  if day <= 20:
    print('Рыбы')
  else:
    print('Овен')
if month1 == ('апрель'):
  if day <= 20:
    print('Овен')
  else:
    print('Телец')
if month1 == ('май'):
  if day <= 21:
    print('Телец')
  else:
    print('Близнецы')
if month1 == ('июнь'):
  if day <= 21:
    print('Близнецы')
  else:
    print('Рак')
if month1 == ('июль'):
  if day <= 22:
    print('Рак')
  else:
    print('Лев')
if month1 == ('август'):
  if day <= 23:
    print('Лев')
  else:
    print('Дева')
if month1 == ('сентябрь'):
  if day <= 22:
    print('Дева')
  else:
    print('Весы')
if month1 == ('октябрь'):
  if day <= 23:
    print('Весы')
  else:
    print('Скорпион')
if month1 == ('ноябрь'):
  if day <= 22:
    print('Скорпион')
  else:
    print('Стрелец')
if month1 == ('декабрь'):
  if day <= 21:
    print('Стрелец')
  else:
    print('Козерог')



