import numpy as np
import matplotlib.pyplot as plt
import random as r

data = []
for a in range(0, 100):
    data.append(r.randint(-2, 100))
fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs.hist(data, bins=20)
axes = plt.gca()
axes.set_xlim([-2,100])
plt.grid(True)
plt.xlabel('Unit')
plt.ylabel('Frequency')

plt.show()

