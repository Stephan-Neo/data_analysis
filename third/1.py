import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x, np.sin(x))
plt.title('sin(x)')

plt.subplot(2, 3, 2)
plt.plot(x, np.cos(x))
plt.title('cos(x)')

plt.subplot(2, 3, 3)
plt.plot(x, np.sin(2 * x))
plt.title('sin(2x)')

plt.subplot(2, 3, 4)
plt.plot(x, np.cos(2 * x))
plt.title('cos(2x)')

plt.subplot(2, 3, 5)
plt.plot(x, np.sin(0.5 * x))
plt.title('sin(0.5x)')

plt.subplot(2, 3, 6)
plt.plot(x, np.cos(0.5 * x))
plt.title('cos(0.5x)')

plt.tight_layout()

plt.show()
