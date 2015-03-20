from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

plength = features[:,2]
is_setosa = (labels == 'setosa')

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()


features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

best_acc = -1.0
best_fi = -1.0
best_t = -1.0

for fi in xrange(features.shape[1]):
    thresh = features[:,fi].copy()
    thresh.sort()
    for t in thresh:
        pred = (features[:,fi] > t)
        acc = (labels[pred] == 'virginica').mean()
        if acc > best_acc:
           best_acc = acc
           best_fi = fi
           best_t = t

plt.scatter(features[labels == 'virginica',2],features[labels == 'virginica',3],marker='o')
plt.scatter(features[labels != 'virginica',2],features[labels == 'virginica',3],marker='x')
plt.show()

