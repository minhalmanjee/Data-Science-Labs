import pandas
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv("/content/drive/MyDrive/dslab02data/iris.csv", names=names)
print("Dataset size:", dataset.shape)
class_distribution = dataset.groupby('class').size()
print("Class distribution:\n", class_distribution)
Dataset size: (151, 5)
Class distribution:
class
Iris-setosa 50
Iris-versicolor 50
Iris-virginica 50
Species 1
dtype: int64
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
t_size = 0.20
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)
le = LabelEncoder()
dataset['Species'] = le.fit_transform(dataset['Species'])
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_test)
print("Accuracy Score:", accuracy_score(Y_test, predictions))
print("Confusion Matrix:\n", confusion_matrix(Y_test, predictions))
print("Classification Report:\n", classification_report(Y_test, predictions))




Q2


import pandas
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv("/content/drive/MyDrive/dslab02data/occupancy.csv", names=names)
print("Dataset size:", dataset.shape)
class_distribution = dataset.groupby('class').size()
print("Class distribution:\n", class_distribution)
Dataset size: (151, 5)
Class distribution:
class
Iris-setosa 50
Iris-versicolor 50
Iris-virginica 50
Species 1
dtype: int64
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
t_size = 0.20
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)
le = LabelEncoder()
dataset['Species'] = le.fit_transform(dataset['Species'])
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_test)
print("Accuracy Score:", accuracy_score(Y_test, predictions))
print("Confusion Matrix:\n", confusion_matrix(Y_test, predictions))
print("Classification Report:\n", classification_report(Y_test, predictions))








Q3
import numpy as np

def chi_squared_distance(x, y):
    return np.sum((x - y) ** 2 / (x + y))

def kNN(train_data, train_labels, test_data, k):
    predictions = []

    for test_point in test_data:
        # Calculate distances between the test point and all training points
        distances = [chi_squared_distance(test_point, train_point) for train_point in train_data]

        # Get indices of k-nearest neighbors
        neighbors_indices = np.argsort(distances)[:k]

        # Get the labels of the k-nearest neighbors
        neighbors_labels = [train_labels[i] for i in neighbors_indices]

        # Predict the label for the test point based on majority voting
        prediction = max(set(neighbors_labels), key=neighbors_labels.count)
        predictions.append(prediction)

    return np.array(predictions)

# Example usage
# Assuming X_train, Y_train, X_test are already defined
# You also need to implement chi_squared_distance function based on your data

k_value = 3  # You can adjust the value of k

# Use the kNN classifier
predictions = kNN(X_train, Y_train, X_test, k_value)

# Print evaluation metrics
print("Accuracy Score:", accuracy_score(Y_test, predictions))
print("Confusion Matrix:\n", confusion_matrix(Y_test, predictions))
print("Classification Report:\n", classification_report(Y_test, predictions))


