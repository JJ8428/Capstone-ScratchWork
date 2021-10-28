from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree
import numpy as np

NUMBER = 100
np.random.seed(2021)
x = np.random.uniform(-2, 2, NUMBER)    # x coordinate of the point
y = np.random.uniform(-2, 2, NUMBER)    # y coordinate of the point
all_data = [[x0, y0] for x0, y0 in zip(x, y)]

labels = []
for sample in all_data:
    if (sample[0] * sample[0])/4 + (sample[1] * sample[1]) - 1 > 0:
        labels.append(1)
    else:
        labels.append(0)

training_data = all_data[:80]
testing_data = all_data[80:]
training_labels = labels[:80]
testing_labels = labels[80:]

# -- KNN Code --
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(training_data, training_labels)
label_pred = knn.predict(testing_data)

correct = 0
for a in range(0, testing_labels.__len__()):
    if testing_labels[a] == label_pred[a]:
        correct += 1
print('KNN Accuracy:', correct/testing_labels.__len__())

# -- SVM Code --
my_svm = svm.SVC()
my_svm.fit(training_data, training_labels)
label_pred = my_svm.predict(testing_data)

correct = 0
for a in range(0, testing_labels.__len__()):
    if testing_labels[a] == label_pred[a]:
        correct += 1
print('SVM Accuracy:', correct/testing_labels.__len__())

# -- DT Code -- 
DT = tree.DecisionTreeClassifier()
DT.fit(training_data, training_labels)
label_pred = DT.predict(testing_data)

correct = 0
for a in range(0, testing_labels.__len__()):
    if testing_labels[a] == label_pred[a]:
        correct += 1
print('DT Accuracy:', correct/testing_labels.__len__())