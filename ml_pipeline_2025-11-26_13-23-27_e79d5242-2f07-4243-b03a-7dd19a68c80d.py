# Random ML Pipeline
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
model = SVC(probability=True)
model.fit(X, y)
print('Prediction:', model.predict(X[:1]))
