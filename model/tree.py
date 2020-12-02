import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import mean_squared_error

train = pd.read_csv("../data/train_data.csv")
test = pd.read_csv("../data/test_data.csv")
X_train, y_train, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]
model_tree = tree.DecisionTreeRegressor()
model_tree = model_tree.fit(X_train, y_train)
y_pred = model_tree.predict(X_test)
print(mean_squared_error(y_test, y_pred))
