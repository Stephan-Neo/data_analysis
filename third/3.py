import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()

fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.ravel()):
    ax.imshow(digits.images[i], cmap=plt.cm.gray_r)
    ax.set_title(digits.target[i])
plt.show()

plt.hist(digits.target, bins=10, rwidth=0.8, align='left', color='skyblue', alpha=0.75)
plt.xticks(range(10))
plt.xlabel('Цифры')
plt.ylabel('Частота')
plt.title('Распределение цифр в наборе данных')
plt.show()

feature1 = 0
feature2 = 45

plt.scatter(digits.data[:, feature1], digits.data[:, feature2], c=digits.target, cmap=plt.cm.get_cmap('viridis', 10))
plt.colorbar(label='Цифры')
plt.xlabel(f'Признак {feature1}')
plt.ylabel(f'Признак {feature2}')
plt.title(f'Диаграмма рассеяния между признаками {feature1} и {feature2}')
plt.show()

fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.ravel()):
    mean_image = np.mean(digits.images[digits.target == i], axis=0)
    ax.imshow(mean_image, cmap=plt.cm.gray_r)
    ax.set_title(i)
plt.show()
