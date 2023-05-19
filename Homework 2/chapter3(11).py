import numpy as np
from scipy.stats import norm, bernoulli
import matplotlib.pyplot as plt

n = 10000
b = 20

Y = 2 * bernoulli.rvs(p = 1/2, loc = 0, size = (b, n)) - 1
X = np.cumsum(Y, axis = 1)

# print(Y)
# print(X)

arr = np.arange(1, n + 1)
# print(arr)
Z = norm.ppf(0.975)
# print(Z)
plt.plot(arr, Z * np.sqrt(arr), color='brown')
plt.plot(arr, -Z * np.sqrt(arr), color='brown')
plt.fill_between(arr, Z * np.sqrt(arr), -Z * np.sqrt(arr), color='brown', alpha=0.05)

for b in range(b):
    plt.plot(arr, X[b])
    
plt.show()
