import numpy as np


def sum_even_diagonal_elements(matrix):
    matrix = np.array(matrix)
    n, m = matrix.shape

    if n != m:
        return 0

    diagonal_elements = np.diag(matrix)
    even_diagonal_elements = diagonal_elements[diagonal_elements % 2 == 0]

    if len(even_diagonal_elements) == 0:
        return 0

    result = np.sum(even_diagonal_elements)

    return result


matrix = np.array([[1, 2, 3],
                   [4, 2, 6],
                   [7, 8, 9]])

result = sum_even_diagonal_elements(matrix)
print(result)
