"""
Жиляев Антон ИУ7-14Б
Программа добавляет элемент в заданное место целочисленного списка алгоритмически
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

# Ввод параметров нового целочисленного элемента
while True:
    k = int(input('Введите позицию для вставки целочисленного элемента: ')) - 1
    if k < 0:
        print('Позиция для вставки должна быть положительной')
    elif k > n:
        print(f'Позиция для вставки должна быть не больше, чем {n+1}')
    else:
        break
x = int(input('Введите значение целочисленного элемента для вставки: '))

# Добавление элемента в список
a.append(None)
i = n
for i in range(n, k, -1):
    a[i] = a[i - 1]
a[k] = x

# Вывод изменённого списка
field_index_size = int(m.log10(len(a) * 10 + 1))  # Вычисление выделенного места для вывода индекса элемента
print('\nИзменённый список')
for (i, value) in enumerate(a):
    print(f'{i+1:{field_index_size}}-й элемент: {value}')
