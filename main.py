interest_rate = 7
region = ['дальний восток', 'сибирь', 'урал', 'поволжье', 'центральная россия', 'юг россии']
client_region = input('Из какого Вы региона? \n')
client_region1 = client_region.lower()

if client_region1 in region and client_region1 == region[0]:
    interest_rate = 2
    print('Процентная ставка составит ' + str(interest_rate) + '%')
    exit()
elif client_region1 not in region:
    print('Недоступный регион!')
    print('Доступные регионы: ' + str(region))
    exit()

children = int(input('Сколько у вас детей? \n'))
if children > 3:
    interest_rate -= 1

salary = input('Получаете ли Вы зарплату на карту нашего банка? да/нет \n')
salary1 = salary.lower()
if salary1 == 'да':
    interest_rate -= 0.5

insurance = input('Будете подключать страховую программу? да/нет \n')
insurance1 = insurance.lower()
if insurance1 == 'да':
    interest_rate -= 1.5

print('Процентная ставка составит {0}%'.format(str(interest_rate)))

