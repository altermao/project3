#Создать новый проект, в нем создать модуль 1seq.py. Задание:
#Пользователь вводит количество элементов будущего списка
#После этого по очереди по одной вводит любые цифры
#Сохранить цифры в список
#Отсортировать список по возрастанию и вывести на экран
#Пример работы: Введите количество элементов: 3
#Введите 1 элемент: 5
#Введите 2 элемент: 2
#Введите 3 элемент: 4
#Вывод: [2, 4, 5]

count = int(input('Введите количество элементов:'))

result = []
# цикл for
for i in range (count):
    number = int (input('Введите число'))
    result.append(number)

result.sort ()
print (result)



# мой первоначальный неудачный вариант (ограниченное и заранее изввестное количество элементов)
answere = int(input('Угадайте количество автомобилей на площадке (от 1 до 10) : '))

while answere != 5 :
    print('Неверно')
    answere = int(input('Введите количество автомобилей : '))

a = int(input('Введите номер автомобиля toyota :'))
b = int(input('Введите номер автомобиля mersedes :'))
c = int(input('Введите номер автомобиля tesla :'))
d = int(input('Введите номер автомобиля lada :'))
e = int(input('Введите номер автомобиля scania : '))

cars = [ a, b, c, d, e]

list.sort (cars)
print (cars)

