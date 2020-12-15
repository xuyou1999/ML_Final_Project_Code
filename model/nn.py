import os
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

device = torch.device("cpu")

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                                           validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:,
                                                                                                         1:-1], test.iloc[
                                                                                                                :, -1]

X_train_tensor = torch.tensor(X_train.values).float()
y_train_tensor = torch.tensor(y_train.values).float()
y_train_tensor = torch.reshape(y_train_tensor, (y_train.shape[0], 1))

batch_size = len(X_train)
num_features = 7
num_output = 1
num_hidden = 10
# dimensions
B, D_in, H, D_out = batch_size, num_features, num_hidden, num_output
m = torch.nn.BatchNorm1d(num_features, affine=True)
n = torch.nn.BatchNorm1d(num_output, affine=True)
X_train_tensor = m(X_train_tensor)
y_train_tensor = n(y_train_tensor)

print(X_train_tensor)
print(y_train_tensor)


class Net(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = nn.Linear(n_input, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden)
        self.predict = nn.Linear(n_hidden, n_output)

    def forward(self, data):
        out = self.hidden1(data)
        out = F.relu(out)
        out = self.hidden2(out)
        out = F.relu(out)
        out = self.predict(out)
        return out


epoch, learning_rate = 5000, 0.05
net = Net(D_in, H, D_out)
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)
loss_func = torch.nn.MSELoss()

for t in range(epoch):
    prediction = net(X_train_tensor)
    loss = loss_func(prediction, y_train_tensor)

    optimizer.zero_grad()
    loss.backward(retain_graph=True)
    optimizer.step()

    if t % 5 == 0:  # plot every 5 epochs
        plt.cla()
        plt.scatter(X_train_tensor[:, 1].detach().numpy(), y_train_tensor.detach().numpy())
        plt.scatter(X_train_tensor[:, 1].detach().numpy(), prediction.data.numpy())
        plt.text(0.5, 0, 'Loss = %.4f' % loss.data, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.05)

plt.ioff()
plt.show()

X_test_tensor = torch.tensor(X_test.values).float()
y_test_tensor = torch.tensor(y_test.values).float()
y_test_tensor = torch.reshape(y_test_tensor, (y_test.shape[0], 1))

X_test_tensor = m(X_test_tensor)
y_test_tensor = n(y_test_tensor)

pred = net(X_test_tensor)
print(pred)
print(loss_func(pred, y_test_tensor))  # 0.0623
