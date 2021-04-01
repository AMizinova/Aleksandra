"""
Мизинова Александра Андреевна
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Мизинова Александра Андреевна'
i = 11

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл while добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""

h = s.split(' ')
i = 0
while i < len(h):
      fio.append(list(h[i]))
      i += 1

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['М', 'и', 'з', 'и', 'н', 'о', 'в', 'а'], ['А', 'л', 'е', 'к', 'с', 'а', 'н', 'д', 'р', 'а'], ['А', 'н', 'д', 'р', 'е', 'е', 'в', 'н', 'а']]))

""" Задание №3 
Используя цикл for переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

for b, f in enumerate(fio):
    fio[b] = fio[b][::-1]    

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['а', 'в', 'о', 'н', 'и', 'з', 'и', 'М'], ['а', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А'], ['а', 'н', 'в', 'е', 'е', 'р', 'д', 'н', 'А']]))

""" Задание №4
Получите из переменной fio 4-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][6]


"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'к'))

""" Задание №5
Получите из переменной fio 4-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][6]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'к'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len = [len(fio[0]),len(fio[1]),len(fio[2])]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [8, 10, 9]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(fio_len)

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 8))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""

chars = str() 
i = 0
while i < min_len:
      for d in range(len(fio)):
          chars += fio[d][i]
      i += 1

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'аааврнодвннеиаезсрикдМен'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""


reversed_fio_dict = {
        'фамилия': fio[0],
        'имя': fio[1],
        'отчество': fio[2]
    }

"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['а', 'в', 'о', 'н', 'и', 'з', 'и', 'М'], 'имя': ['а', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А'], 'отчество': ['а', 'н', 'в', 'е', 'е', 'р', 'д', 'н', 'А']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values())

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['а', 'в', 'о', 'н', 'и', 'з', 'и', 'М'], ['а', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А'], ['а', 'н', 'в', 'е', 'е', 'р', 'д', 'н', 'А']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(reversed_fio_dict.items())

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['а', 'в', 'о', 'н', 'и', 'з', 'и', 'М']), ('имя', ['а', 'р', 'д', 'н', 'а', 'с', 'к', 'е', 'л', 'А']), ('отчество', ['а', 'н', 'в', 'е', 'е', 'р', 'д', 'н', 'А'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = reversed_fio_dict['фамилия']

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['а', 'в', 'о', 'н', 'и', 'з', 'и', 'М']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = s.lower().replace(' ','')

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'мизиноваалександраандреевна'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

res = {}
for i in s:
    res[i] = s.count(i)
res = list(res.items())

"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('м', 1), ('и', 2), ('з', 1), ('н', 4), ('о', 1), ('в', 2), ('а', 6), ('л', 1), ('е', 3), ('к', 1), ('с', 1), ('д', 2), ('р', 2)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию aleksandraCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов aleksandraCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def aleksandraCharToIndex(hp):
    h = hp.lower()
    return alphabet.find(h)+1


"""------------ конец блока редактирования----------------"""
print('№17 ' + str(aleksandraCharToIndex("Ф") == 22))

""" Задание №18
При помощи функции aleksandraCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""
for i in range(len(fio)):
    k=0
    s = []
    while k < len(fio[i]):
          s.append(aleksandraCharToIndex(fio[i][k]))
          k+=1
    fio[i] = s

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[1, 3, 16, 15, 10, 9, 10, 14], [1, 18, 5, 15, 1, 19, 12, 6, 13, 1], [1, 15, 3, 6, 6, 18, 5, 15, 1]]))


""" +++ КОНЕЦ =) +++ """

