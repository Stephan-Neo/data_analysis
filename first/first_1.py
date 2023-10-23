def f(first, second):
    common = []
    for item in first:
        if item in second:
            common.append(item)
    return common


a = [1, 2, 3, 5]
b = [4, 1, 6, 5]
print(f(a, b))
