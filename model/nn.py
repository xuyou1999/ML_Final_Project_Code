import os
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch.autograd import Variable

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                                           validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:,
                                                                                                         1:-1], test.iloc[
                                                                                                                :, -1]

X_train_tensor = torch.tensor(X_train.values).float()
y_train_tensor = torch.tensor(y_train.values).float()
y_train_tensor = torch.reshape(y_train_tensor, (y_train.shape[0],1))

print(X_train_tensor.size())
print(y_train_tensor.size())

class Net(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = nn.Linear(n_input, n_hidden)
        # self.hidden2 = nn.Linear(n_hidden, n_hidden)
        # self.hidden3 = nn.Linear(n_hidden, n_hidden)
        # self.hidden4 = nn.Linear(n_hidden, n_hidden)
        # self.hidden5 = nn.Linear(n_hidden, n_hidden)
        self.predict = nn.Linear(n_hidden, n_output)

    def forward(self, data):
        out = self.hidden1(data)
        out = F.relu(out)
        # out = self.hidden2(out)
        # out = F.relu(out)
        # out = self.hidden3(out)
        # out = F.relu(out)
        # out = self.hidden4(out)
        # out = F.relu(out)
        # out = self.hidden5(out)
        # out = F.relu(out)
        out = self.predict(out)
        return out


net = Net(7, 1, 1)

optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
loss_func = torch.nn.MSELoss()

for t in range(500):
    prediction = net(X_train_tensor)
    loss = loss_func(prediction, y_train_tensor)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

#     if t%5 ==0:
#         plt.cla()
#         plt.scatter(X_train.iloc[:, 1].to_numpy(), y_train.to_numpy())
#         plt.plot(X_train.iloc[:, 1].to_numpy(), prediction.data.numpy(), 'r-', lw=5)
#         plt.text(0.5, 0, 'Loss = %.4f' % loss.data, fontdict={'size': 20, 'color': 'red'})
#         plt.pause(0.05)

# plt.ioff()
# plt.show()

X_test_tensor = torch.tensor(X_test.values).float()
y_test_tensor = torch.tensor(y_test.values).float()
y_test_tensor = torch.reshape(y_test_tensor, (y_test.shape[0],1))
pred = net(X_test_tensor)
print(pred)
print(loss_func(pred, y_test_tensor))