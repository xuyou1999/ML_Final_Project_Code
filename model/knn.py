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


k_list = [i for i in range(1, 100)]
mse_list = []
for k in k_list:
    knn = KNeighborsRegressor(k, weights="distance")  # "distance" gives a better performance than "uniform"
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_validate)
    MSE = mean_squared_error(y_validate, y_pred)
    mse_list.append(MSE)
min_i = np.array(mse_list).argmin()
curr_lowest_MSE = mse_list[min_i]
curr_best_k = k_list[min_i]
print("Initial MSE: %f" % curr_lowest_MSE)
print("Initial best k: %d" % curr_best_k)

# feature selection
removed_index_list = []
removed_feature_list = []
feature_num = 7
while len(removed_index_list) < feature_num:  # can at most remove all features
    best_k_list = []
    lowest_MSE_list = []
    round_num = len(removed_index_list) + 1
    suffix = "st" if round_num == 1 else "nd" if round_num == 2 else "rd" if round_num == 3 else "th"
    print("%d%s round of feature selection..." % (round_num, suffix))
    for i in range(1, feature_num + 1):  # run knn on all possible combinations of features
        loc = []
        for j in range(1, feature_num + 1):  # combine all possible features
            if j != i and j not in removed_index_list:
                loc.append(j)
        X_train_i = train.iloc[:, loc]
        X_validate_i = validate.iloc[:, loc]
        k_list = [n for n in range(1, 100)]
        mse_list = []
        for k in k_list:  # run knn on one possible combination
            knn = KNeighborsRegressor(k, weights="distance")
            knn.fit(X_train_i, y_train)
            y_pred = knn.predict(X_validate_i)
            MSE = mean_squared_error(y_validate, y_pred)
            mse_list.append(MSE)
        min_index = np.array(mse_list).argmin()
        lowest_MSE = mse_list[min_index]
        lowest_MSE_list.append(lowest_MSE)
        best_k = k_list[min_index]
        best_k_list.append(best_k)
    best_index = np.array(lowest_MSE_list).argmin()
    best_mse = lowest_MSE_list[best_index]
    best_k = best_k_list[best_index]
    # update best MSE and best k in a round
    if best_mse < curr_lowest_MSE:
        curr_lowest_MSE = best_mse
        curr_best_k = best_k
        removed_index = best_index
        removed_feature = train.columns[removed_index + 1]
        removed_index_list.append(removed_index)
        removed_feature_list.append(removed_feature)
        print('removing feature "%s"...' % removed_feature)
    else:  # if cannot update, break while loop to terminate feature selection
        print("Cannot update best MSE, end feature selection...")
        break
print("Final MSE: %f" % curr_lowest_MSE)
print("Final best k: %d" % curr_best_k)
print("Features removed during selection: ", removed_feature_list)

# test with test set
loc = []
for i in range(1, feature_num + 1):
    if i not in removed_index_list:
        loc.append(i)
X_train = train.iloc[:, loc]
X_test = test.iloc[:, loc]
knn = KNeighborsRegressor(curr_best_k)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
test_MSE = mean_squared_error(pred, y_test)
test_score = knn.score(X_test, pred)
print("Test MSE: %f" % test_MSE)
print("Test Score: %f" % test_score)

# plot
pred_arg = pred.argsort()
pred.sort()
truth = y_test.values
truth = [truth[arg] for arg in pred_arg]
N = [i for i in range(len(y_test))]
plt.plot(N, pred, 'r')
plt.plot(N, truth, 'b')
plt.title("Model: KNN")
plt.xlabel("movie")
plt.ylabel("rating")
plt.legend(("prediction", "ground truth"))
plt.savefig("knn.png")
plt.show()

