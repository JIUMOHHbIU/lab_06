"""
Жиляев Антон ИУ7-14Б
Программа находит наиболее длинную непрерывную знакочередующуюся последовательность нечётных чисел
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

# Нахождение искомой последовательности
max_len_seq = 0
current_len_seq = 0
id_start_seq = 0
for i in range(1, n):
    if not (a[i - 1] % 2 and a[i] % 2):
        current_len_seq = 0
        continue
    if a[i - 1] * a[i] < 0:
        current_len_seq += 1
        if current_len_seq + 1 > max_len_seq:
            max_len_seq = current_len_seq + 1
            id_start_seq = i - current_len_seq
    else:
        current_len_seq = 0

print("\nИскомая последовательность: ")
field_index_size = int(m.log10(max_len_seq * 10 + 1))  # Вычисление выделенного места для вывода индекса элемента
for i in range(id_start_seq, id_start_seq + max_len_seq):
    print(f'{i+1-id_start_seq:{field_index_size}}-й элемент: {a[i]}')