from sklearn.linear_model import LogisticRegression

# This is the dataset manually typed
data = [
    (0.50, 0),
    (0.75, 0),
    (1.00, 0),
    (1.25, 0),
    (1.50, 0),
    (1.75, 0),
    (1.75, 1),
    (2.00, 0),
    (2.25, 1),
    (2.50, 0),
    (2.75, 1),
    (3.00, 0),
    (3.25, 1),
    (3.50, 0),
    (4.00, 1),
    (4.25, 1),
    (4.50, 1),
    (4.75, 1),
    (5.00, 1),
    (5.50, 1)
] 
x = []
y = []
for a in range(0, data.__len__()):
    x.append([data[a][0]])
    y.append(data[a][1])

model = LogisticRegression(C=1e5)
model.fit(x, y)

# Our numbers, atleast those printed in the console, match the textbook
print(model.coef_)
print(model.intercept_)