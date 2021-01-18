import numpy as np
import matplotlib.pyplot as plt
import random as r

# Generate fake data
data = []
for a in range(0, 100):
    data.append(r.randint(-2, 100))
fig, axs = plt.subplots()

# Histogram
'''
# We can set the number of bins with the `bins` kwarg
axs.hist(data, bins=20)
axes = plt.gca()
axes.set_xlim([-2,100])
plt.grid(True)
plt.xlabel('Unit')
plt.ylabel('Frequency')
plt.show()
'''

# Box and Whisker
'''
axs.boxplot(data)
plt.ylabel('Unit')
plt.show()
'''

# Count number of hits, average, 
'''
hits = 0
total = 0
sum = 0
for a in range(0, data.__len__()):
    total += 1
    if data[a] == -1:
        sum += data[a]
        hits += 1
print("hit rate:" + str(hits) + " / " + str(total))
print("average: " + str(np.mean(data)))
print("std dev: " + str(np.std(data)))
'''

# Get all files in "viewing/" directory and delete
'''
import os
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("viewing/") if isfile(join("viewing/", f))]
for file in files:
    os.remove("viewing/"+file)
'''
