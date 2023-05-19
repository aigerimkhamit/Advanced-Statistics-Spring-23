import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv')

X = data['HP'].values.reshape(-1, 1)
Y = np.log(data['MPG']).values
model = LinearRegression()
model.fit(X, Y)
print(model.intercept_, model.coef_)
plt.scatter(X, Y)
plt.plot(X, model.predict(X), color='green')
plt.xlabel("Horsepower")
plt.ylabel("Miles per gallon")
plt.show()