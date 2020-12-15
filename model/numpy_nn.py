import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F


# configure work directory
abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

# configure device, dtype
device = torch.device("cuda:0")  # device = torch.device("cpu")
dtype = torch.float32

# read data
train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                                           validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:,
                                                                                                         1:-1], test.iloc[
                                                                                                                :, -1]

# Series to numpy
X_train = X_train.values
y_train = y_train.values
X_test = X_test.values
y_test = y_test.values


def normalize(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def standardize(data):
    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    return (data - mu) / sigma, mu, sigma


def de_standardize(std_data, mu, sigma):
    return std_data * sigma + mu


# standardize data, record
X_train_data = standardize(X_train)
std_X_train = X_train_data[0]
X_train_mu, X_train_sigma = X_train_data[1], X_train_data[2]

y_train_data = standardize(y_train)
std_y_train = y_train_data[0]
y_train_mu, y_train_sigma = y_train_data[1], y_train_data[2]

X_test_data = standardize(X_test)
std_X_test = X_test_data[0]
X_test_mu, X_test_sigma = X_test_data[1], X_test_data[2]

y_test_data = standardize(y_test)
std_y_test = y_test_data[0]
y_test_mu, y_test_sigma = y_test_data[1], y_test_data[2]

# numpy to tensor
X_in = torch.tensor(std_X_train, dtype=dtype)
y_in = torch.tensor(std_y_train, dtype=dtype)
y_in = y_in.resize(len(y_in), 1)
X_in_test = torch.tensor(std_X_test, dtype=dtype)
y_in_test = torch.tensor(std_y_test, dtype=dtype)
y_in_test = y_in_test.resize(len(y_in_test), 1)

# model parameters
batch_size = len(X_in)
num_features = 7
num_output = 1
num_hidden = 100
B, D_in, H, D_out = batch_size, num_features, num_hidden, num_output


# define model
class Net(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = nn.Linear(n_input, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden)
        self.hidden3 = nn.Linear(n_hidden, n_hidden)
        self.hidden4 = nn.Linear(n_hidden, n_hidden)
        self.hidden5 = nn.Linear(n_hidden, n_hidden)
        self.predict = nn.Linear(n_hidden, n_output)

    def forward(self, data):
        out = self.hidden1(data)
        out = F.relu(out)
        out = self.hidden2(out)
        out = F.relu(out)
        out = self.hidden3(out)
        out = F.relu(out)
        out = self.hidden4(out)
        out = F.relu(out)
        out = self.hidden5(out)
        out = F.relu(out)
        out = self.predict(out)
        return out


# train model
epoch, learning_rate = 5000, 0.05
net = Net(D_in, H, D_out)
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)
loss_func = torch.nn.MSELoss()

for t in range(epoch):
    prediction = net(X_in)
    loss = loss_func(prediction, y_in)

    optimizer.zero_grad()
    loss.backward(retain_graph=True)
    optimizer.step()

# test with test set
pred = net(X_in_test)
loss = loss_func(pred, y_in_test)
print("standardized test prediction:", pred)
print("standardized test mse:", loss)

pred = pred.detach().numpy()  # convert to numpy (de_standardize() takes numpy as argument)
y_pred = de_standardize(pred, y_test_mu, y_test_sigma)
y_pred_tensor = torch.from_numpy(y_pred)  # convert to tensor (loss_func() takes tensor as argument)
y_test_tensor = torch.from_numpy(y_test)  # convert to tensor
print("real test prediction:", y_pred_tensor)
print("ground truth:", y_test_tensor)
print("real test mse:", loss_func(y_pred_tensor, y_test_tensor))  # 3.3533

# plot
truth = y_test
truth_arg = truth.argsort()
truth.sort()
y_pred = [y_pred[arg] for arg in truth_arg]
N = [i for i in range(len(y_test))]
plt.scatter(N, y_pred, s=1)
plt.plot(N, truth, 'r')
plt.title("Model: Neural Network")
plt.xlabel("movie")
plt.ylabel("rating")
plt.legend(("ground truth", "prediction"))
plt.savefig("neural network.png", dpi=400)
plt.show()
