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
                                validate.iloc[:, 1:-1], validate.iloc[:, -1], test.iloc[:, 1:-1], test.iloc[:, -1]