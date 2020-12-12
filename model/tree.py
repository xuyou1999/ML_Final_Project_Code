import os

import pandas as pd
from sklearn import tree
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor


abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]

# tree with not limitation on max_features
model_tree = tree.DecisionTreeRegressor(max_depth=None, random_state=1)
model_tree = model_tree.fit(X_train, y_train)
y_pred_tree = model_tree.predict(X_test)
print('Tree error', mean_squared_error(y_test, y_pred_tree))


# Random forest by setting the number of trees using val set, max_features is by deault as sqrt
opt_estimators = 1
opt_error = 100
for i in range(1, 200):
    model_random_forest = RandomForestRegressor(random_state=1, n_estimators=i).fit(X_train, y_train)
    y_pred_random_forest = model_random_forest.predict(X_validate)
    error = mean_squared_error(y_validate, y_pred_random_forest)
    if error < opt_error:
        opt_error = error
        opt_estimators = i
    print('Ramdom forest error:', error)

print(opt_error) # 0.09151789030831993
print(opt_estimators) # 159

