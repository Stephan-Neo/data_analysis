import numpy as np


def matrix_multiply(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одного размера для умножения")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
        for k in range(len(matrix2)):
            element += matrix1[i][k] * matrix2[k][j]
        row.append(element)
        result.append(row)

    return result


def numpy_matrix_multiply(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("Матрицы должны быть согласованного размера для умножения")

    result = np.dot(matrix1, matrix2)
    return result


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


result1 = matrix_multiply(matrix1.tolist(), matrix2.tolist())
print("Результат без NumPy:")
print(result1)


result2 = numpy_matrix_multiply(matrix1, matrix2)
print("Результат с использованием NumPy:")
print(result2)
