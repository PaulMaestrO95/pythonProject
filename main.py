interest_rate = 7
region = ['дальний восток', 'сибирь', 'урал', 'поволжье', 'центральная россия', 'юг россии']

def child():
    global interest_rate
    try:
        children = int(input('Сколько у вас детей? \n'))
        if children > 3:
            interest_rate -= 1
    except:
        print('Введите число!')
        children = int(input('Сколько у вас детей? \n'))
        if children > 3:
            interest_rate -= 1

def data():
    global interest_rate
    salary = input('Получаете ли Вы зарплату на карту нашего банка? да/нет \n').lower()
    if salary == 'да':
        interest_rate -= 0.5
    elif salary == 'нет':
        interest_rate == interest_rate
    else:
        print('Пожалуйста, ответьте да или нет')
        salary = input('Получаете ли Вы зарплату на карту нашего банка? да/нет \n').lower()
        if salary == 'да':
            interest_rate -= 0.5

    insurance = input('Будете подключать страховую программу? да/нет \n').lower()
    if insurance == 'да':
        interest_rate -= 1.5
    elif insurance == 'нет':
        interest_rate == interest_rate
    else:
        print('Пожалуйста, ответьте да или нет')
        insurance = input('Будете подключать страховую программу? да/нет \n').lower()
        if insurance == 'да':
            interest_rate -= 1.5

def client_regions():
    while True:
        client_region = input('Из какого Вы региона? \n').lower()
        if client_region in region and client_region == region[0]:
            interest_rate = 2
            print(f"Процентная ставка составит {str(interest_rate)}%. До свидания!")
            exit()
        elif client_region not in region:
            print('Недоступный регион!')
            print('Доступные регионы: ' + str(region))
            continue
        break

if __name__=="__main__":
    client_regions()
    child()
    data()
    print(f"Процентная ставка составит {str(float(interest_rate))}%. До свидания!")