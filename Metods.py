# Metods popilar list

# 1 Объявление
vegetables = ['tomato', 'cucumber', 'eggplant', 'celery']
print(vegetables)

# 2 Добавление
vegetables.append('radish')
print(vegetables)

# 3 Изменение
vegetables.insert(1, 'pumpkin')
print(vegetables)

vegetables[3] = 'sunflower'
print(vegetables)

# 4 Удаление
del vegetables[0]
print(vegetables)

vegetables.remove('sunflower')
print(vegetables)

# 5 Сортировка
vegetables.sort()
print(vegetables)

vegetables.reverse()
print(vegetables)

# Metods popilar dict
# 1 Объявление
vegetable = {
    'name': 'tomato',
    'weight': 100,
    'food': True
}
print(vegetable)

# 2 Добавление
vegetable['poison'] = False
print(vegetable)

# 3 Изменения
vegetable['weight'] = 200
print(vegetable)

# 4 Удаление
del vegetable['poison']
print(vegetable)

# 5 Получение пар ключ-значение
print(vegetable.items())

# Metods popilar set
cars = {'toyota', 'mersedes', 'tesla', 'lada', 'scania'}
print(cars)

# 1Классификация
truсk_car = {'toyota', 'mersedes', 'scania'}
electro_car = {'tesla'}
rus_car = {'lada'}
#Легоковые автомобили
print(cars - truсk_car)
#номарки
print(cars - rus_car)
#С ДВС
print(cars - electro_car)
# 2 Число элементов в множестве
print(len(truсk_car))

# 3 Принадлежность элемента множеству
print('lada' in cars)

# 4 Объединение элементов множеств
print(rus_car|electro_car)

#5 Перечень автомобилей
for item in cars :
    print(item)


