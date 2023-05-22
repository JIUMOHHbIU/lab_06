"""
Жиляев Антон ИУ7-14Б
Программа меняет местами минимальный чётный и максимальный нечётный элемент списка
"""

import math as m

# Ввод целочисленного списка
while True:
    n = int(input('Введите размер целочисленного списка: '))
    if n > -1:
        break
    print('Размер списка должен быть неотрицательным')

a = [0] * n
field_index_size = int(m.log10(len(a) * 10 + 1))  # Вычисление выделенного места для вывода индекса элемента
for i in range(n):
    a[i] = int(input(f'Введите {i+1:{field_index_size}}-й целочисленный элемент: '))

# Нахождение индексов элементов для перестановки
id_min_max = [-1, -1]
for i in range(0, n):
    if id_min_max[a[i] % 2] < 0:
        id_min_max[a[i] % 2] = i

    if a[i] % 2 and a[i] > a[id_min_max[a[i] % 2]]:
        id_min_max[a[i] % 2] = i

    if a[i] % 2 == 0 and a[i] < a[id_min_max[a[i] % 2]]:
        id_min_max[a[i] % 2] = i

# Проверка на наличие чётных или нечётных элементов
if any(id_min_max[i] < 0 for i in range(2)):
    print(f'Данный список не имеет либо чётных, либо нечётных элементов')
else:
    a[id_min_max[0]], a[id_min_max[1]] = a[id_min_max[1]], a[id_min_max[0]]

    # Вывод изменённого списка
    field_index_size = int(m.log10(len(a) * 10 + 1))  # Вычисление выделенного места для вывода индекса элемента
    print('\nИзменённый список')
    for (i, value) in enumerate(a):
        print(f'{i+1:{field_index_size}}-й элемент: {value}')
