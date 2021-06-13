import sklearn
from sklearn import datasets
 
# load iris dataset
iris = datasets.load_iris()

# bagi atribut dan target, assign ke dalam variable x, y
x=iris.data
y=iris.target

from sklearn.model_selection import cross_val_score
from sklearn import tree
 
clf = tree.DecisionTreeClassifier()

# mengevaluasi performa model dengan cross_val_score
scores = cross_val_score(clf, x, y, cv=5)
scores