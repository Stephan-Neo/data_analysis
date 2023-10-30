import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return [i*i for i in x]


def f2(x):
    return [i + i for i in x]


def f3(x):
    return [i*4 for i in x]


def f4(x):
    return [i*i -i for i in x]


x = np.linspace(0, 10, 10000)
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
y1 = f1(x)
plt.plot(x, y1)
plt.title('График f1(x)')
plt.xlabel('x')
plt.ylabel('f1(x)')

plt.subplot(2, 2, 2)
y2 = f2(x)
plt.plot(x, y2)
plt.title('График f2(x)')
plt.xlabel('x')
plt.ylabel('f2(x)')

plt.subplot(2, 2, 3)
y3 = f3(x)
plt.plot(x, y3)
plt.title('График f3(x)')
plt.xlabel('x')
plt.ylabel('f3(x)')

plt.subplot(2, 2, 4)
y4 = f4(x)
plt.plot(x, y4)
plt.title('График f4(x)')
plt.xlabel('x')
plt.ylabel('f4(x')

plt.tight_layout()

plt.show()