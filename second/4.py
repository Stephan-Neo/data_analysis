import numpy as np


def build_cumulative_sum_array(X):
    cumulative_sums = np.cumsum(X, axis=1)

    return cumulative_sums


X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = build_cumulative_sum_array(X)
print(result)
