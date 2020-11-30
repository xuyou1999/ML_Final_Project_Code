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
