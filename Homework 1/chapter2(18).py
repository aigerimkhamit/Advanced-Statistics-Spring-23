import numpy as np
from scipy.stats import norm

#X ~ N(3, 16)

x = "P(X < 7): "
#cdf(x, loc=0, scale=1) = Cumulative distribution function.
y = norm.cdf(7, loc=3, scale=4)
print(x + str(y))

x = "P(X > -2): "
y = 1 - norm.cdf(-2, loc=3, scale=4)
print(x + str(y))

x = "Find x such that P(X > x) = 0.05: "
#ppf(q, loc=0, scale=1) = Percent point function (inverse of cdf — percentiles).
y = norm.ppf(0.95, loc=3, scale=4)
print(x + str(y))

x = "Find P(0 ≤ X < 4): "
y = norm.cdf(4, loc=3, scale=4) - norm.cdf(0, loc=3, scale=4)
print(x + str(y))

x = "Find x such that P(|X| > |x|) = 0.05: "
y = norm.ppf(0.975, loc=3, scale=4)
print(x + str(y))