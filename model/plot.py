import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]

loc = []
for i in range(1, 8):
    if i != 6:
        loc.append(i)
X_train = train.iloc[:, loc]
X_test = test.iloc[:, loc]
knn = KNeighborsRegressor(18)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
test_MSE = mean_squared_error(pred, y_test)
test_score = knn.score(X_test, pred)

truth = y_test.values
pred_arg = pred.argsort()
truth = [truth[arg] for arg in pred_arg]
print(pred)
print(pred_arg)
print(pred)
print(truth)
N = [i for i in range(len(y_test))]
plt.scatter(N, truth, s=1)
plt.savefig("123.png",dpi=450)
plt.show()