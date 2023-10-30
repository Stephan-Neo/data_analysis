import numpy as np


def transform_array(X, a=1):
    transformed_X = X.copy()
    transformed_X[1::2] = a
    transformed_X[0::2] **= 3
    reversed_X = transformed_X[::-1]
    result = np.concatenate((X, reversed_X))

    return result


x = np.array([100, 200, 300, 400, 500])
transformed_x = transform_array(x)
print(transformed_x)
