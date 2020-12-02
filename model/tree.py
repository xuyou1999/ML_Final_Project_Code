import pandas as pd
import os
from sklearn import tree
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

train = pd.read_csv("../data/train_data.csv")
test = pd.read_csv("../data/test_data.csv")
X_train, y_train, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]
model_tree = tree.DecisionTreeRegressor(max_depth=None)
model_tree = model_tree.fit(X_train, y_train)
y_pred_tree = model_tree.predict(X_test)
print(mean_squared_error(y_test, y_pred_tree))


# Bagging
model_bag = BaggingRegressor(base_estimator=tree.DecisionTreeRegressor(max_depth=None), n_estimators=20).fit(X_train, y_train)
y_pred_bag = model_bag.predict(X_test)
print(mean_squared_error(y_test, y_pred_bag))