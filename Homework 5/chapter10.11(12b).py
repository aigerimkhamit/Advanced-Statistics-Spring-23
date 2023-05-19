import numpy as np
import scipy.stats

l_0 = 1
n = 20
a = 0.05
simulations = 10000000

c = scipy.stats.norm.ppf(0.975)

np.random.seed(1)
X = np.random.poisson(lam = l_0, size=[simulations, n])
W = (np.mean(X, axis = 1) - l_0) / (np.sqrt(1/n *l_0**2))
reject = np.sum(np.abs(W) > c)
ans = reject / simulations
print(ans) # 0.0557798