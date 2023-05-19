import numpy as np

X = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]
Y = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]

X = np.array(X)
Y = np.array(Y)

N = 1000000
all_data = np.concatenate([X, Y])
nx = len(X)

# by calculations in part a 
diff_hat = 0.0222
cnt = 0

for i in range(1000000):
    np.random.shuffle(all_data)
    x = all_data[:nx]
    y = all_data[nx:]
    diff = x.mean() - y.mean()
    if diff > diff_hat:
        cnt += 1

p_value = cnt / N

print(p_value)