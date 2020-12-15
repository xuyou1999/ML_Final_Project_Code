import os
import torch
import matplotlib.pyplot as plt
import pandas as pd

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

dtype = torch.float32
# device = torch.device("cpu")
device = torch.device("cuda:0")

train = pd.read_csv("../data/train_data.csv")
validate = pd.read_csv("../data/validate_data.csv")
test = pd.read_csv("../data/test_data.csv")

X_train, y_train, X_validate, y_validate, X_test, y_test = train.iloc[:, 1:-1], train.iloc[:, -1], \
                                                           validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:,
                                                                                                         1:-1], test.iloc[
                                                                                                                :, -1]
X = torch.tensor(X_train.values).float()
y = torch.tensor(y_train.values).float()
y = torch.reshape(y, (y_train.shape[0], 1))
print("size of X:", X.size())
print("size of y:", y.size())
num_features = 7
num_output = 1
# dimensions
B, D_in, H, D_out = len(X_train), num_features, 3, num_output
m = torch.nn.BatchNorm1d(num_features)
n = torch.nn.BatchNorm1d(num_output)
X = m(X)
print("after norm:", X)
y = n(y)
print("after norm:", y)
# data
#x = torch.randn(B, D_in, device=device, dtype=dtype)
#y = torch.randn(B, D_out, device=device, dtype=dtype)

# Model parameters are encapsulated inside torch.nn.Linear
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
)
# Use 'sum' reduction, creating SSE
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4
epoch = 500

sse = []

for t in range(epoch):
    # Input data: x, the last dimension of x must be equal to D_in
    y_pred = model(X)
    print(y_pred)
    loss = loss_fn(y_pred, y)

    sse.append(loss.item())

    # compute gradient
    loss.backward(retain_graph=True)

    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad
        # clear parameter gradients
        model.zero_grad()

plt.plot(sse)
plt.xlabel("epoch")
plt.ylabel("training sse")
plt.show()
print(sse[-1])