import numpy as np
import matplotlib.pyplot as plt

x  = np.linspace(0, 3, 200)
y1 = x ** 2 + 3
y2 = np.exp(x) + 2
y3 = np.cos(x)

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.fill_between(x, y1, y2, color='green', alpha=0.3)

plt.plot(x, y2, label='y2')
plt.plot(x, y3, label='y3')
plt.fill_between(x, y2, y3, color='yellow', alpha=0.5, hatch='o')

plt.plot(x, y1, label='y1')
plt.plot(x, y3, label='y3')
plt.fill_between(x, y1, y3, color='blue', alpha=0.2, hatch='\\')

plt.legend()

plt.show()
