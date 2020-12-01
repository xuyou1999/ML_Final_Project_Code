import pandas as pd
import random

# load csv files, already add headers manually
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
writer_pred_avg = pd.read_csv('./data/writer_pred_avg.csv')

# concatenate _empty.csv and _pred_avg.csv into full data
actor = pd.concat((actor_empty, actor_pred_avg))
director = pd.concat((director_empty, director_pred_avg))
genre = pd.concat((genre_empty, genre_pred_avg))
language = pd.concat((language_empty, language_pred_avg))
region = pd.concat((region_empty, region_pred_avg))
writer = pd.concat((writer_empty, writer_pred_avg))

# merge all attributes(predictors)
attr_lst = [actor, director, genre, language, region, writer]
movie = pd.merge(actor, director)
for attr in range(len(attr_lst)):
    if attr >= 2:
        movie = pd.merge(movie, attr_lst[attr])

# choose the earliest year as date in movie data
origin_movie = pd.read_csv('./data/movie.csv')
for i in range(len(origin_movie)):
    date_str = origin_movie['date'][i]
    date_lst = date_str.strip('"').split(',')
    for j in range(len(date_lst)):
        date_lst[j] = int(date_lst[j][:4])
    date = min(date_lst)
    origin_movie["date"][i] = date
# no warning: for i in range(len(origin_movie)): origin_movie.iloc[i, 1:2] = min([int(d[:4]) for d in [date for date
# in origin_movie.iloc[i, 1:2].str.strip('"').str.split(',')[0]]])


# merge date(predictor)
movie_date = origin_movie[['movie_id', 'date']]
movie = pd.merge(movie, movie_date, on='movie_id')

# merge ratings(label)
movie_rating = origin_movie[["movie_id", "movie_rating"]]
movie = pd.merge(movie, movie_rating, on="movie_id")

# randomly generate training and testing data set
test_i = []
train_i = []
for i in range(len(origin_movie)):
    random.seed(i)  # make sure to get same data on every program execution
    if random.random() >= 0.8:
        test_i.append(i)
    else:
        train_i.append(i)

movie_test = movie.iloc[test_i]
movie_train = movie.iloc[train_i]

movie_test.to_csv('./data/test_data.csv', index=False)
movie_train.to_csv('./data/train_data.csv', index=False)

# if headers not added manually, can do as follows:
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
