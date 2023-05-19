from cmath import exp
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

n = 10000
x = norm.rvs(size=n)
y = np.exp(x)

b = np.arange(0.01, 5, step = 0.01)
a = norm.pdf(np.log(b)) / b

plt.hist(y, bins=50, density=True)
plt.plot(b, a, label='true density', color = 'r')
plt.show()

