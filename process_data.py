
import numpy as np
import pandas as pd

actor_empty = pd.read_csv('./data/actor_empty.csv')
actor_pred_avg = pd.read_csv('./data/actor_pred_avg.csv')
director_empty = pd.read_csv('./data/director_empty.csv')
director_pred_avg = pd.read_csv('./data/director_pred_avg.csv')
genre_empty = pd.read_csv('./data/genre_empty.csv')
genre_pred_avg = pd.read_csv('./data/genre_pred_avg.csv')
language_empty = pd.read_csv('./data/language_empty.csv')
language_pred_avg = pd.read_csv('./data/language_pred_avg.csv')
region_empty = pd.read_csv('./data/region_empty.csv')
region_pred_avg = pd.read_csv('./data/region_pred_avg.csv')
writer_empty = pd.read_csv('./data/writer_empty.csv')
wirter_pred_avg = pd.read_csv('./data/writer_pred_avg.csv')

actor = pd.merge(actor_empty, actor_pred_avg)

'''
import pandas as pd

f1 = pd.read_csv("./data/actor_pred_avg.csv", header=None, names=['id', 'actor_avg'])
f2 = pd.read_csv("./data/actor_empty.csv", header=None, names=['id', 'actor_avg'])
actor = pd.concat([f1, f2])

f1 = pd.read_csv("./data/director_pred_avg.csv", header=None, names=['id', 'director_avg'])
f2 = pd.read_csv("./data/director_empty.csv", header=None, names=['id', 'director_avg'])
director = pd.concat([f1, f2])

a = pd.merge(actor, director, on="id")
print(a)
'''
