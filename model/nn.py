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


net = Net(1, 20, 1)
print(net)

optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
loss_func = torch.nn.MSELoss()
