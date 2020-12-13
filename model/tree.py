import os

import pandas as pd
from sklearn import tree
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor


abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]

def tree_reg(X_train, y_train):
    # tree without limitation on max_features
    model_tree = tree.DecisionTreeRegressor(max_depth=None, random_state=1)
    model_tree = model_tree.fit(X_train, y_train)
    return model_tree

def find_random_forest(X_train, y_train, X_validate, y_validate):
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
    return random_forest(X_train, y_train, opt_estimators)

def random_forest(X_train, y_train, n):
    model_random_forest = RandomForestRegressor(random_state=1, n_estimators=n).fit(X_train, y_train)
    return model_random_forest

def find_boosting(X_train, y_train, X_validate, y_validate):
    # boosting
    opt_estimators = 1
    opt_error = 100
    for i in range(1, 200):
        model_grad_boost = GradientBoostingRegressor(loss='ls', random_state=1, n_estimators=i).fit(X_train, y_train)
        y_pred_grad_boost = model_grad_boost.predict(X_validate)
        error = mean_squared_error(y_validate, y_pred_grad_boost)
        if error < opt_error:
            opt_error = error
            opt_estimators = i
        print('Gradient boosting error:', error)
    print(opt_error) # 0.0943017905460884
    print(opt_estimators) # 169
    return boosting(X_train, y_train, opt_estimators)

def boosting(X_train, y_train, n):
    model_grad_boost = GradientBoostingRegressor(loss='ls', random_state=1, n_estimators=n).fit(X_train, y_train)
    return model_grad_boost

def mse(model, X_test, y_test):
    pred = model.predict(X_test)
    error = mean_squared_error(y_test, pred)
    return error

def main(X_train, y_train, X_validate, y_validate, X_test, y_test):
    print('tree mse:', mse(tree_reg(X_train, y_train), X_test, y_test))
    print('random_forest mse:', mse(random_forest(X_train, y_train, 159), X_test, y_test))
    print('boosting mse:', mse(boosting(X_train, y_train, 169), X_test, y_test))

main(X_train, y_train, X_validate, y_validate, X_test, y_test)
