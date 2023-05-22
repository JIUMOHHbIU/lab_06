"""
Жиляев Антон ИУ7-14Б
Программа находит значение K-го экстремума в списке
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

# Подсчёт количества экстремумов
counter_ext = 0
for i in range(2, n):
    if a[i] > a[i - 1] < a[i - 2] or a[i] < a[i - 1] > a[i - 2]:
        counter_ext += 1

if counter_ext == 0:
    print('Последовательность не содержит экстремумов')
else:
    # Ввод индекса искомого экстремума
    while True:
        k = int(input('Введите индекс экстремума: '))
        if k <= 0:
            print('Индекс быть положительным')
        elif k > counter_ext:
            print(f'Индекс должен быть не больше, чем {counter_ext}')
        else:
            break

    # Нахождение K-го экстремума
    counter_ext = 0
    for i in range(2, n):
        if a[i] > a[i - 1] < a[i - 2] or a[i] < a[i - 1] > a[i - 2]:
            counter_ext += 1
            if counter_ext == k:
                print(f'Значение {k}-го экстремума равно {a[i - 1]:.5g}')
                break
