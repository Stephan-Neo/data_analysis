import numpy as np


def encode(arr):
    if len(arr) == 0:
        return np.array([]), np.array([])

    unique_elements, element_counts = np.unique(arr, return_counts=True)
    return unique_elements, element_counts


input_array = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
result = encode(input_array)
print(result)
