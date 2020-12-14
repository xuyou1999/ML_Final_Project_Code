import os

import pandas as pd
from sklearn import tree
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from matplotlib import pyplot as plt

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")
test.sort_values('movie_rating', inplace=True)

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                                           validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:,
                                                                                                         1:-1], test.iloc[
                                                                                                                :, -1]


def tree_reg(X_train, y_train):
    # tree without limitation on max_features
    model_tree = tree.DecisionTreeRegressor(max_depth=None, random_state=1)
    model_tree.fit(X_train, y_train)
    return model_tree


def find_random_forest(X_train, y_train, X_validate, y_validate):
    # Random forest by setting the number of trees using val set, max_features is by default as sqrt
    opt_estimators = 1
    opt_error = 100
    for i in range(1, 200):
        model_random_forest = RandomForestRegressor(random_state=1, n_estimators=i)
        model_random_forest.fit(X_train, y_train)
        y_pred_random_forest = model_random_forest.predict(X_validate)
        error = mean_squared_error(y_validate, y_pred_random_forest)
        if error < opt_error:
            opt_error = error
            opt_estimators = i
    #     print('Random forest error:', error)
    # print(opt_error)  # 0.09151789030831993
    # print(opt_estimators)  # 159
    return random_forest(X_train, y_train, opt_estimators)


def random_forest(X_train, y_train, n):
    model_random_forest = RandomForestRegressor(random_state=1, n_estimators=n)
    model_random_forest.fit(X_train, y_train)
    return model_random_forest


def find_boosting(X_train, y_train, X_validate, y_validate):
    # boosting
    opt_estimators = 1
    opt_error = 100
    for i in range(1, 200):
        model_grad_boost = GradientBoostingRegressor(loss='ls', random_state=1, n_estimators=i)
        model_grad_boost.fit(X_train, y_train)
        y_pred_grad_boost = model_grad_boost.predict(X_validate)
        error = mean_squared_error(y_validate, y_pred_grad_boost)
        if error < opt_error:
            opt_error = error
            opt_estimators = i
    #     print('Gradient boosting error:', error)
    # print(opt_error)  # 0.0943017905460884
    # print(opt_estimators)  # 169
    return boosting(X_train, y_train, opt_estimators)


def boosting(X_train, y_train, n):
    model_grad_boost = GradientBoostingRegressor(loss='ls', random_state=1, n_estimators=n)
    model_grad_boost.fit(X_train, y_train)
    return model_grad_boost


def mse(model, X_test, y_test):
    pred = model.predict(X_test)
    error = mean_squared_error(y_test, pred)
    return error

def method(name, X_train, y_train, X_validate=None, y_validate=None):
    if name == 'tree':
        return tree_reg(X_train, y_train)
    elif name == 'random forest':
        return find_random_forest(X_train, y_train, X_validate, y_validate)
    elif name == 'boosting':
        return find_boosting(X_train, y_train, X_validate, y_validate)

def feature_selection(method_name, current_model, X_train, y_train, X_validate, y_validate):
    if X_train.shape[1] == 1:
        return current_model, X_train, X_validate
    origin_model = current_model
    opt_model = origin_model
    origin_mse = mse(origin_model, X_validate, y_validate)
    opt_mse = origin_mse
    for i in range(X_train.shape[1]):
        X_train_i = X_train.iloc[:, X_train.columns != X_train.columns[i]]
        X_validate_i = X_validate.iloc[:, X_validate.columns != X_validate.columns[i]]
        new_model = method(method_name, X_train_i, y_train, X_validate_i, y_validate)
        new_mse = mse(new_model, X_validate_i, y_validate)
        # print('new_mse:', new_mse)
        if new_mse < opt_mse:
            opt_mse = new_mse
            opt_model = new_model
            new_X_train = X_train_i
            new_X_validate = X_validate_i
    
    if opt_mse == origin_mse:
        return origin_model, X_train, X_validate
    else:
        return feature_selection(method_name, opt_model, new_X_train, y_train, new_X_validate, y_validate)

def operate_selection(X_train, y_train, X_validate, y_validate, X_test, y_test):
    # tree
    origin_tree = tree_reg(X_train, y_train)
    print('tree mse:', mse(origin_tree, X_test, y_test))
    select_tree, new_X_train_tree, new_X_validate_tree = feature_selection('tree', origin_tree, X_train, y_train, X_validate, y_validate)
    print('tree mse after feature selection:', mse(select_tree, X_test.loc[:, new_X_train_tree.columns], y_test))
    print('new features:', new_X_train_tree.columns)
    # random forest
    origin_random_forest = random_forest(X_train, y_train, 159)
    print('random forest mse:', mse(origin_random_forest, X_test, y_test))
    select_random_forest, new_X_train_random_forest, new_X_validate_random_forest = feature_selection('random forest', origin_random_forest, X_train, y_train, X_validate, y_validate)
    print('random forest after feature selection:', mse(select_random_forest, X_test.loc[:, new_X_train_random_forest.columns], y_test))
    print('new_features:', new_X_train_random_forest.columns)
    # boosting
    origin_boosting = boosting(X_train, y_train, 169)
    print('boosting mse:', mse(origin_boosting, X_test, y_test))
    select_boosting, new_X_train_boosting, new_X_validate_boosting = feature_selection('boosting', origin_boosting, X_train, y_train, X_validate, y_validate)
    print('boosting after feature selection:', mse(select_boosting, X_test.loc[:, new_X_train_boosting.columns], y_test))
    print('new_features:', new_X_train_boosting.columns)
    '''
    tree mse: 0.18073499662845582
tree mse after feature selection: 0.17862440997977072
new features: Index(['actor_rating', 'director_rating', 'language_rating', 'region_rating',
       'writer_rating', 'date'],
      dtype='object')
random forest mse: 0.10051179087685266
random forest after feature selection: 0.10107273203267343
new_features: Index(['actor_rating', 'director_rating', 'genre_rating', 'region_rating',
       'writer_rating', 'date'],
      dtype='object')
boosting mse: 0.10242035066395254
boosting after feature selection: 0.10307454709516191
new_features: Index(['actor_rating', 'director_rating', 'genre_rating', 'region_rating',
       'writer_rating', 'date'],
      dtype='object')
    '''

def main(X_train, y_train, X_validate, y_validate, X_test, y_test):
    X_train_tree = X_train.iloc[:, X_train.columns != 'genre_rating']
    X_validate_tree = X_validate.iloc[:, X_validate.columns != 'genre_rating']
    X_test_tree = X_test.iloc[:, X_test.columns != 'genre_rating']

    tree_model = tree_reg(X_train_tree, y_train)
    tree_pred = tree_model.predict(X_test_tree)
    print('tree mse:', mse(tree_model, X_test_tree, y_test))

    N = [i for i in range(len(y_test))]
    plt.plot(N, y_test, 'r')
    plt.scatter(N, tree_pred, s=1)
    plt.title("Model: Tree")
    plt.xlabel("movie")
    plt.ylabel("rating")
    plt.legend(("ground truth", "prediction"))
    plt.savefig("tree.png")
    plt.show() 

    random_forest_model = random_forest(X_train, y_train, 159)
    random_forest_pred = random_forest_model.predict(X_test)
    print('random forest mse:', mse(random_forest_model, X_test, y_test))
    
    N = [i for i in range(len(y_test))]
    plt.plot(N, y_test, 'r')
    plt.scatter(N, random_forest_pred, s=1)
    plt.title("Model: Random forest")
    plt.xlabel("movie")
    plt.ylabel("rating")
    plt.legend(("ground truth", "prediction"))
    plt.savefig("random_forest.png")
    plt.show() 

    boosting_model = boosting(X_train, y_train, 169)
    boosting_pred = boosting_model.predict(X_test)
    print('boosting error:', mse(boosting_model, X_test, y_test))

    N = [i for i in range(len(y_test))]
    plt.plot(N, y_test, 'r')
    plt.scatter(N, boosting_pred, s=1)
    plt.title("Model: Boosting")
    plt.xlabel("movie")
    plt.ylabel("rating")
    plt.legend(("ground truth", "prediction"))
    plt.savefig("boosting.png")
    plt.show() 

main(X_train, y_train, X_validate, y_validate, X_test, y_test)
