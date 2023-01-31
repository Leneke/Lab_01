# Задание 6. # создаем матрицу, заданного размера, заполненную случайными числами из заданного диапазона

import numpy as np

matrix = np.random.randint(0, 11, size=(3, 4))
print(matrix)
sum_matrix = np.sum(matrix)
print(f'Сумма чисел матрицы: {sum_matrix}')
print(f'Максимальный элемент матрицы: {np.max(matrix)}')
print(f'Сумма чисел 1-й строки: {sum(matrix[0])}')
print(f'Минимальный элемент во 2-ом столбце: {min(matrix[:, 1])}')
print(f'Максимальный элемент главной диагонали: {np.max(np.diag(matrix))}')


# для тренировки матрица с помощью цикла
#
# matrix = []
# for i in range(3):
#     elem = []
#     for j in range(4):
#         elem.append(random.randint(0, 10))
#     matrix.append(elem)
#     print(elem)
#
# матрица list comprehension
# matrix = [[random.randint(0, 10) for x in range(4)] for y in range(3)]
# for elem in matrix:
#     print(elem)


# Сумма всех чисел матрицы
# summa = 0
# for elem in matrix:
#     summa += sum(elem)
# print(f'Сумма всех чисел матрицы = {summa}')
#
# Сумма всех чисел матрицы list comprehension
# summa = sum([sum(elem) for elem in matrix])
# print(f'Сумма всех чисел матрицы = {summa}')


# # максимальный элемент
# maximum = []
# for elem in matrix:
#     maximum.append(max(elem))
# print(f'Максимальный элемент = {max(maximum)}')
#
# максимальный элемент list comprehension
# maximum = max([max(elem) for elem in matrix])
# print(f'Максимальный элемент = {maximum}')


# сумма чисел в 1-й строке
# summa_1 = sum(matrix[0])
# print(f'Сумма чисел в 1-й строке = {summa_1}')


# минимальный элемент во 2-ом столбце
# minim = []
# for elem in matrix:
#     minim.append(elem[1])
# print(f'Минимальный элемент во 2-ом столбце = {min(minim)}')
#
# минимальный элемент во 2-ом столбце list comprehension
# minim = min([elem[1] for elem in matrix])
# print(f'Минимальный элемент во 2-ом столбце = {minim}')


# максимальный элемент по главной диагонали
# diagonal = []
# for i in range(len(matrix)):
#     diagonal.append(matrix[i][i])
#
# print(f'Максимальный элемент по главной диагонали = {max(diagonal)}')
#
# максимальный элемент по главной диагонали list comprehensions
# diagonal = max([matrix[i][i] for i in range(len(matrix))])
# print(f'Максимальный элемент по главной диагонали = {diagonal}')

