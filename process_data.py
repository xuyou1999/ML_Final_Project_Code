import pandas as pd

f1 = pd.read_csv("./data/actor_pred_avg.csv", header=None, names=['id', 'actor_avg'])
f2 = pd.read_csv("./data/actor_empty.csv", header=None, names=['id', 'actor_avg'])
actor = pd.concat([f1, f2])

f1 = pd.read_csv("./data/director_pred_avg.csv", header=None, names=['id', 'director_avg'])
f2 = pd.read_csv("./data/director_empty.csv", header=None, names=['id', 'director_avg'])
director = pd.concat([f1, f2])

a = pd.merge(actor, director, on="id")
print(a)