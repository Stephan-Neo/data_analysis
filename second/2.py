import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)

print("Скалярное произведение с использованием NumPy:", dot_product)

a = [1, 2, 3]
b = [4, 5, 6]

dot_product = sum([a[i] * b[i] for i in range(len(a))])

print("Скалярное произведение без NumPy:", dot_product)
