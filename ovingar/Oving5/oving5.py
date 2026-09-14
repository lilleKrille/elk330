from matplotlib import pyplot as plt
import numpy as np

def gauss_curve(t, a, mu, sigma): return a * np.exp(-(t - mu)**2 / (2 * sigma**2))

# Modelling with gauss-curve
l_0 = [0, 10, 50, 100]
a = [100, 125, 150, 200]
mu = [3, 10, 15, 20]
sigma = [1, 2, 3, 4]

# apply gauss-curve to each l_0, a, mu, sigma
# subplots for each mu, 2x2 grid, with shared x-axis, include other values in each subplot
fig, axs = plt.subplots(2, 2, sharex=True)

t = np.linspace(0, 24, 100)
for i in range(len(mu)):
    row, col = divmod(i, 2)
    ax = axs[row, col]
    for j in range(len(mu)):
        ax.plot(t, gauss_curve(t, a[j], mu[i], sigma[j]))
    ax.set_title(f"mu = {mu[i]}, sigma = {sigma[i]}")
    ax.set_xlabel("t")
    ax.set_ylabel("l_0")

plt.tight_layout()
plt.savefig("elk320/elk330/ovingar/Oving5/gauss_curve.png")
plt.show()
