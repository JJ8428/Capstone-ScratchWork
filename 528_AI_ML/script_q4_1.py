import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

'''
Example based on:
https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html
'''

# Like 4.2, a sine wave will be used
np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()
# Every 5th index, add noise to make data 'realistic'
y[::5] += 1 * (0.5 - np.random.rand(8))

knn = neighbors.KNeighborsRegressor(5, weights='uniform')
y_ = knn.fit(X, y).predict(T)

plt.subplot(1, 1, 1)
# Got rid of 
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, y_, color='navy', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("KNeighborsRegressor (k = 5, weights = 'uniform')")

plt.tight_layout()
plt.show()