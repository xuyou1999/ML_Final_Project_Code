import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

train = pd.read_csv("../data/train_data.csv")
test = pd.read_csv("../data/test_data.csv")
