from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]

k_list = [i for i in range(5, 20)]
mse_list = []
score_list = []
for k in k_list:
    knn = KNeighborsRegressor(k, weights="distance")  # "distance" gives a better performance than "uniform"
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_validate)
    score = knn.score(X_validate, y_validate)
    score_list.append(score)
    MSE = mean_squared_error(y_validate, y_pred)
    mse_list.append(MSE)
    print("MSE:", MSE)

min_i = np.array(mse_list).argmin()
print("The best k is:", k_list[min_i])

plt.title("mse-k curve")
plt.ylabel("MSE")
plt.xlabel("k value")
plt.plot(k_list, mse_list)
plt.show()

plt.title("score-k curve")
plt.ylabel("score")
plt.xlabel("k value")
plt.plot(k_list, score_list)
plt.show()