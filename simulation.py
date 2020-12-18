import random
import time


def simulate():
    random.seed(time.time())
    simulations1 = 65
    simulations2 = 30
    cost1 = 30
    cost2 = 65
    total1 = 0
    total2 = 0
    for i in range(simulations1):
        drop1 = random.randint(0, 10)
        total1 += drop1
    for i in range(simulations2):
        drop2 = random.randint(12, 16)
        total2 += drop2
    return total1, total2


if __name__ == '__main__':
    total1, total2 = simulate()
    print(total1, total2)

# train = pd.read_csv("./data/train_data.csv")
# validate = pd.read_csv("./data/validate_data.csv")
# test = pd.read_csv("./data/test_data.csv")
#
# feature_num = 7
# for i in range(1, feature_num + 1):
#     loc = []
#     for j in range(1, feature_num + 1):
#         if j != i:
#             loc.append(j)
#     train_i = train.iloc[:, loc]
# k_list = [i for i in range(10, 30)]
# mse_list = []
# score_list = []
# for k in k_list:
#     knn = KNeighborsRegressor(k, weights="distance")  # "distance" gives a better performance than "uniform"
#     knn.fit(X_train, y_train)
#     y_pred = knn.predict(X_validate)
#     score = knn.score(X_validate, y_validate)
#     score_list.append(score)
#     MSE = mean_squared_error(y_validate, y_pred)
#     mse_list.append(MSE)
#     print("MSE:", MSE)
#
# min_i = np.array(mse_list).argmin()
# print("The best k is:", k_list[min_i])
#
# plt.title("mse-k curve")
# plt.ylabel("MSE")
# plt.xlabel("k value")
# plt.plot(k_list, mse_list)
# plt.show()
#
# plt.title("score-k curve")
# plt.ylabel("score")
# plt.xlabel("k value")
# plt.plot(k_list, score_list)
# plt.show()
