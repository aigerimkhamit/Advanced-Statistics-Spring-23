from statistics import mean
import numpy as np

p = 0.3

X1 = []
X2 = []
X3 = []
for i in range(100000):
    a = np.where(np.random.uniform(low = 0, high = 1, size = 10) < p, 1, 0)
    b = np.where(np.random.uniform(low = 0, high = 1, size = 100) < p, 1, 0)
    c = np.where(np.random.uniform(low = 0, high = 1, size = 1000) < p, 1, 0)
    X1.append(a)
    X2.append(b)
    X3.append(c)
    
print("For n = 10:")
print(mean(sum(X1) / len(X1)) * 10)
print(10 * p)
print()
print("For n = 100:")
print(mean(sum(X2) / len(X2)) * 100)
print(100 * p)
print()
print("For n = 1000:")
print(mean(sum(X3) / len(X3)) * 1000)
print(1000 * p)


