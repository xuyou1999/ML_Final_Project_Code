import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

train = pd.read_csv("../data/train_data.csv")
test = pd.read_csv("../data/test_data.csv")
X_train, y_train, X_test, y_test = train.iloc[:, :-1], train.iloc[:, -1], test.iloc[:, :-1], test.iloc[:, -1]
# print(X_train)
# print(y_train)