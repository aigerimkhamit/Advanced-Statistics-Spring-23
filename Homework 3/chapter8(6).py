import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#  Create a data set (using µ = 5) consisting of n=100 observations.
X = norm.rvs(loc = 5, scale = 1, size = 100)
print(X)
teta = np.exp(5)
teta_hat = np.exp(X.mean())

# Use the bootstrap to get the se and 95 percent confidence interval for θ
B = 10000
bootstr = np.empty(B) 
n = len(X)
for i in range(B):
    xx = np.random.choice(X, n, replace=True)
    bootstr[i] = np.exp(xx.mean()) #adding mean of each simulation to our array

# calculating standard error
se = bootstr.std()
# confidence interval 
Z = 1.96 # for 95%
confidence_int = [teta_hat - Z * se, teta_hat + Z * se]
print("Theta hat: ", teta_hat)
print("Standard error: ", se)
print("Confidence interval for 95%: ", confidence_int)

#Plot a histogram of the bootstrap replications. This is an estimate of the distribution of θ
bins = np.linspace(50, 250, 500)
plt.hist(bootstr, bins, label='bootstrap', color='green', histtype='step', density=True)
plt.axvline(x = teta, color ='black', label = 'θ')
plt.legend(loc='upper left')
plt.show()
