import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mode

# 1
x = np.arange(0, 1001, 1)
y = x**2 + 3*x + 5
z = [x_val / 2 if x_val % 2 == 0 else None for x_val in x]

target_sequence = ["First", "Second", "Second", "Third", None]
target = [target_sequence[i % len(target_sequence)] for i in range(len(x))]

df_test = pd.DataFrame({'x': x, 'y': y, 'z': z, 'target': target})

# 2
print(df_test.head(4))

print("Количество пропущенных значений:")
print(df_test.isnull().sum())

print("Информация о колонках:")
print(df_test.info())

# 3
mean_without_mode = df_test['z'].mean()
df_test['z'].fillna(mean_without_mode, inplace=True)
mode_target = mode(df_test['target'])
df_test['target'].fillna(mode_target, inplace=True)

# 4
plt.figure(figsize=(10, 6))
plt.scatter(df_test['x'], df_test['y'], color='blue', alpha=0.5)
plt.title('График рассеяния между x и y')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
df_test['target'].value_counts().plot(kind='bar', color='green', alpha=0.7)
plt.title('Распределение значений в столбце "target"')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# 5
df = pd.read_csv('train.csv')

df.dropna(inplace=True)
print(df.info())

plt.figure(figsize=(8, 5))
df['age'].hist(bins=20, color='purple', edgecolor='black')
plt.title('Распределение возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.show()
