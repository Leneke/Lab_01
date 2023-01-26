# Задание 6. # создаем матрицу, заданного размера, заполненную случайными числами из заданного диапозона

import numpy as np

matrix = np.random.randint(0, 11, size=(3, 4))
print(matrix)
sum_matrix = np.sum(matrix)
print(f'Сумма чисел матрицы: {sum_matrix}')
print(f'Максимальный элемент матрицы: {np.max(matrix)}')
print(f'Сумма чисел 1-й строки: {sum(matrix[0])}')
print(f'Минимальный элемент во 2-ом столбце: {min(matrix[:, 1])}')
print(f'Максимальный элемент главной диагонали: {np.max(np.diag(matrix))}')