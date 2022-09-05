# создать новый модуль victory.py.
# Написать или улучшить программу Викторина из предыдущего дз
# (Для тренировки - не пользоваться никакими библиотеками кроме random)
# Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') -
# для тренировки пока использовать строку
# Программа выбирает из этих 10-и 5 случайных людей,
# это можно реализовать с помощью модуля random и функции sample

# Пример использования sample:
#import random
#numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
#result = random.sample(numbers, 2)
#print(result) # [5, 1]

#После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
#пользователь вводит дату в формате 'dd.mm.yyyy'

#Например 03.01.2009, если пользователь ответил неверно,
# то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

#В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

# Викторина "Годы рождения знаменитых рок-гитаристов" (данные получены их Википедии)
# звезды, дни рождения

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

days = {
    '01': 'первого',
    '02': 'второго',
    '03': 'третьего',
    '04': 'четвертого',
    '05': 'пятого',
    '06': 'шестого',
    '07': 'седьмого',
    '08': 'восьмого',
    '09': 'девятого',
    '10': 'десятого',
    '11': 'одиннадцатого',
    '12': 'двенадцатого',
    '13': 'тринадцатого',
    '14': 'четырнадцатого',
    '15': 'пятнадцатого',
    '16': 'шестнадцатого',
    '17': 'семнадцатое',
    '18': 'восемнадцатого',
    '19': 'девятнадцатого',
    '20': 'двадцатого',
    '21': 'двадцать первого',
    '22': 'двадцать второго',
    '23': 'двадцать третьего',
    '24': 'двадцать четвертого',
    '25': 'двадцать пятого',
    '26': 'двадцать шестого',
    '27': 'двадцать седьмого',
    '28': 'двадцать восьмого',
    '29': 'двадцать девятого',
    '30': 'тридцатого',
    '31': 'тридцать первого'
}

star_1 = 'Карлос Сантана'
data_1 = '20.07.1947'

star_2 = 'Джимми Хендрикс'
data_2 = '27.11.1942'

star_3 = 'Риччи Блэкмор'
data_3 = '14.04.1945'

star_4 = 'Эрик Клэптон'
data_4 = '30.03.1945'

star_5 = 'Марк Нопфлер'
data_5 = '12.08.1949'

star_6 = 'Рэнди Роадс'
data_6 = '06.12.1956'

star_7 = 'Брайан Мэй'
data_7 = '19.07.1947'

star_8 = 'Пол Кук'
data_8 = '20.07.1956'

star_9 = 'Ринго Старр'
data_9 = '07.07.1940'

star_10 = 'Джо Сатриани'
data_10 = '15.07.1956'

stars = [star_1, star_2,star_3,star_4,star_5,star_6,star_7,star_8,star_9,star_10 ]

user_y = 0
user_n = 0

import random

result= random.sample (stars,5)
print(result) # [5.1]

if star_1 in result:
    answere_1 = str (input('День рождения Карлоса Сантаны в формате dd.mm.yyyy ? :'))
    if answere_1 == data_1:
        print ('Верно')
        user_y += 1
    else:
        print('Неверно !')
        day, month, year = data_1.split('.')
        print (days[day], months [month], year,'года')
        user_n += 1

if star_2 in result:
    answere_2 = str (input('День рождения Джимми Хендрикса в формате dd.mm.yyyy ? :'))
    if answere_2 == data_2:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_2.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_3 in result:
    answere_3 = str (input('День рождения Риччи Блэкмора в формате dd.mm.yyyy ? :'))
    if answere_3 == data_3:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_3.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_4 in result:
    answere_4 = str (input('День рождения Эрика Клэптона в формате dd.mm.yyyy ? :'))
    if answere_4 == data_4:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_4.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_5 in result:
    answere_5 = str (input('День рождения Марка Нопфлера в формате dd.mm.yyyy ? :'))
    if answere_5 == data_5:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_5.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_6 in result:
    answere_6 = str (input('День рождения Рэнди Роадса в формате dd.mm.yyyy ? :'))
    if answere_6 == data_6:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_6.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_7 in result:
    answere_7 = str (input('День рождения Брайана Мэя в формате dd.mm.yyyy ? :'))
    if answere_7 == data_7:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_7.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_8 in result:
    answere_8 = str (input('День рождения Пола Кука в формате dd.mm.yyyy ? :'))
    if answere_8 == data_8:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_8.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_9 in result:
    answere_9 = str (input('День рождения Ринго Старра в формате dd.mm.yyyy ? :'))
    if answere_9 == data_9:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_9.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

if star_10 in result:
    answere_10 = str (input('День рождения Джо Сатриани в формате dd.mm.yyyy ? :'))
    if answere_10 == data_10:
        print ('Верно')
        user_y += 1
    else:
        print ('Неверно !')
        day, month, year = data_10.split('.')
        print(days[day], months [month], year, 'года')
        user_n += 1

print('Количество верных ответов: ' + str(user_y))
print('Количество неверных ответов: ' + str(user_n))

ask = input(' Повторим ?) (Y/N) ?:')
if ask == str ('N'):
    print('Goodbye !')
    exit()
if ask == str ('Y'):
    import random

    result = random.sample(stars, 5)
    print(result)  # [5.1]

    if star_1 in result:
        answere_1 = str(input('День рождения Карлоса Сантаны в формате dd.mm.yyyy ? :'))
        if answere_1 == data_1:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_1.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_2 in result:
        answere_2 = str(input('День рождения Джимми Хендрикса в формате dd.mm.yyyy ? :'))
        if answere_2 == data_2:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_2.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_3 in result:
        answere_3 = str(input('День рождения Риччи Блэкмора в формате dd.mm.yyyy ? :'))
        if answere_3 == data_3:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_3.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_4 in result:
        answere_4 = str(input('День рождения Эрика Клэптона в формате dd.mm.yyyy ? :'))
        if answere_4 == data_4:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_4.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_5 in result:
        answere_5 = str(input('День рождения Марка Нопфлера в формате dd.mm.yyyy ? :'))
        if answere_5 == data_5:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_5.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_6 in result:
        answere_6 = str(input('День рождения Рэнди Роадса в формате dd.mm.yyyy ? :'))
        if answere_6 == data_6:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_6.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_7 in result:
        answere_7 = str(input('День рождения Брайана Мэя в формате dd.mm.yyyy ? :'))
        if answere_7 == data_7:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_7.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_8 in result:
        answere_8 = str(input('День рождения Пола Кука в формате dd.mm.yyyy ? :'))
        if answere_8 == data_8:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_8.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_9 in result:
        answere_9 = str(input('День рождения Ринго Старра в формате dd.mm.yyyy ? :'))
        if answere_9 == data_9:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_9.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    if star_10 in result:
        answere_10 = str(input('День рождения Джо Сатриани в формате dd.mm.yyyy ? :'))
        if answere_10 == data_10:
            print('Верно')
            user_y += 1
        else:
            print('Неверно !')
            day, month, year = data_10.split('.')
            print(days[day], months[month], year, 'года')
            user_n += 1

    print('Количество верных ответов: ' + str(user_y))
    print('Количество неверных ответов: ' + str(user_n))

else:
    print ('Goodbye')
    exit()


