import numpy as np
import matplotlib.pyplot as plt

data = []

num_distributions = 10
num_samples = 2048
num_bins = 100

for _ in range(num_distributions):
    mean = np.random.uniform(0, 10)
    std = np.random.uniform(0.1, 2.0)
    samples = np.random.normal(mean, std, num_samples)
    data.append(samples)

colors = plt.cm.viridis(np.linspace(0, 1, num_distributions))

plt.figure(figsize=(10, 6))

for i in range(num_distributions):
    plt.hist(data[i], num_bins, alpha=0.5, color=colors[i], label=f'Distribution {i + 1}')

plt.title('10 Different Normal Distributions')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
