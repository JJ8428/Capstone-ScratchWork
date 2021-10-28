import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

'''
Code is based on:
https://outlook.office.com/mail/sentitems/id/AAQkADhmZjM2NzY2LTMzZjEtNDQyMC05NWVlLTg1ZDc5Mzc3ZjlmMAAQALWr4nONFGhPsczwnU4qwwE%3D
'''

# Generate a list of y values 
def gen_data(x):  
    # Generate sin wave with sigma: 1, std: .25  
    y = np.sin(x)+np.random.uniform(1, .25, len(x))
    return y

# Generates 1000 x values between [1, 1000/200], all evenly distributed
x = [i/200 for i in range(1000)]
y = np.array(gen_data(x))
x = np.array(x).reshape(-1,1)

# Show the data generated
plt.scatter(x, y, s=2)
plt.show()

svr = SVR().fit(x, y)
'''
Note to self for future revisit:
Defaults args include:
- degree=3
- epsilon=.1
'''
yfit = svr.predict(x)

# Show the SVR fitted plot compares to the data
plt.scatter(x, y, s=2)
plt.plot(x, yfit, color="r", label="SVR Generated Line")
plt.legend()
plt.show()

score = svr.score(x,y)
print("R-squared:", score) # Tells how strong the correlation is
print("MSE:", mean_squared_error(y, yfit)) # Goal here is to minimize
