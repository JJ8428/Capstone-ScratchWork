import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import scipy.stats as st
from sklearn.cluster import KMeans

# Simple scatter plot of all the points provided
def scatter_plot(X, Y):
    plt.scatter(X, Y)
    plt.grid(True)
    plt.ylim(bottom = -180, top = 180)
    plt.xlim(left = -180, right = 180)
    plt.show()

# Gaussian KDE, useful for the most basic of analyses
def gaussian_kde(X, Y):
    xmin, xmax = -180, 180
    ymin, ymax = -180, 180
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([X, Y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    cfset = ax.contourf(xx, yy, f, cmap='Greens')
    plt.show()

# Tunable parameters
file_index = 7
proxi = 5
files = [f for f in listdir('residue_data/') if isfile(join('residue_data/', f))]
print('Tunable paramters: file_index = ' + str(file_index) + ' proxi = ' + str(proxi))

'''
file_index : integer that maps to the file being analyzed in residue_data/

To view the paths of each file in residue_data/, use the following code:
print('Index || filename')
for a in range(0, files.__len__()):
    print(str(a) + ' || ' + files[a])

proxi : the minimum distance that 2 points can be close to one another
'''

# Harvest the data from respective file index
X = []
Y = []
indices = []
files = [f for f in listdir('residue_data/') if isfile(join('residue_data/', f))]
toRead = 'residue_data/' + files[file_index]
r = open(toRead, 'r')
tmp = 0
for line in r.readlines():
    indices.append(tmp)
    tmp += 1
    line = line.split(',')
    X.append(float(line[-2]))
    Y.append(float(line[-1]))
for a in range(0, X.__len__()):
    if Y[a] == 360 or Y[a] == -360:
        Y[a] = 0
    if X[a] == 360 or X[a] == -360:
        X[a] = 0

# Filter X and Y based on proxi
newX = []
newY = []
for a in range(0, X.__len__()):
    if newX.__len__() == 0:
        newX.append(X[a])
        newY.append(Y[a])
    else:
        min_dist = 1000
        for b in range(0, newX.__len__()):
            dist = ((X[a] - newX[b])**2 + (Y[a] - newY[b])**2)**.5
            if min_dist > dist:
                min_dist = dist
        if min_dist > proxi:
            newX.append(X[a])
            newY.append(Y[a])
X = newX
Y = newY

scatter_plot(X, Y)
gaussian_kde(X, Y)

