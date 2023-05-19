import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

n = 100
mu = 5
sigma = 1

X = np.random.normal(mu, sigma, n)

theta = np.exp(mu)
theta_hat = np.exp(np.mean(X))
variance = np.var(X)

#using Delta Method
se_delta = np.abs(np.exp(mu)) * np.sqrt(variance / n)
theta_delta = np.random.normal(theta, se_delta, size=100000)
conf_interval_delta = [theta - 1.96 * se_delta, theta + 1.96 * se_delta]

#using parametric bootstrap
n_param_bootstrap = 100000
theta_param_bootstrap = np.empty(n_param_bootstrap)
for i in range(n_param_bootstrap):
    X_param_bootstrap = np.random.normal(mu, 1, n)
    theta_param_bootstrap[i] = np.exp(np.mean(X_param_bootstrap))

se_param_bootstrap = np.std(theta_param_bootstrap)
conf_interval_param_bootstrap = [theta - 1.96*se_param_bootstrap, theta + 1.96*se_param_bootstrap]

#using non-parametric bootstrap 
n_nonparam_bootstrap = 100000
theta_nonparam_bootstrap = np.empty(n_nonparam_bootstrap)
for i in range(n_nonparam_bootstrap):
    X_nonparam_bootstrap = np.random.choice(X, n, replace=True)
    theta_nonparam_bootstrap[i] = np.exp(np.mean(X_nonparam_bootstrap))

se_nonparam_bootstrap = np.std(theta_nonparam_bootstrap)
conf_interval_nonparam_bootstrap = [theta - 1.96*se_nonparam_bootstrap, theta + 1.96*se_nonparam_bootstrap]

#plotting histograms
plt.figure(figsize=(10, 6))
plt.hist(theta_param_bootstrap, label='Parametric Bootstrap')
plt.hist(theta_nonparam_bootstrap, label='Nonparametric Bootstrap')
plt.hist(theta_delta, label='Delta Method')
plt.axvline(x=theta, color='r', linestyle='dashed', linewidth=2, label='True Value')
plt.xlabel('θ')
plt.ylabel('Density')
plt.title('Comparison of Bootstrap Approximations to True Sampling Distribution of θ')
plt.show()