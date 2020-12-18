# Machine Learning Final Project
## Directory: .
db_class.py: class MyDb, can be used to fetch data from database

DoubanAPI.py: class DoubanAPI, API for Douban, can be used to obtain movie information on Douban

logger_class.py: class Logger, serves as logger, can be used to track information of program execution

extract_id.py: obtain movie IDs on Douban, can set sample size in this file

extract_data.py: extract detailed movie data from Douban, and insert into database

load_data.py: fetch data from database, and save to csv files

process_data.py: process and split data in training/testing/validation sets

utility.py: utility functions, including datetime etc.
## Directory: ./model
knn.py: k-nearest-neighbors model

neural network.py: fully-connected neural network model

tree.py: decision tree, random forest, and boosting tree model

linear/ridge regression.py: linear and ridge regression model
## Directory: ./data
folder to contain data sets
## Directory: ./log
folder to contain log files
## Directory: ./sql
create_db.sql: sql queries (MySQL style) to create database for this project
## Note:
1. The number of lines in "..._pred_avg.csv" and "..._empty.csv" should add up to the number of movies/sample size.
2. Samples and data sets already attached in data folder.
3. Please configure work directory to "./" to run.
4. Please set valid IP proxies in DoubanAPI.py; otherwise will suffer temporary IP ban.
5. Default device in Pytorch is set to GPU (with cuda cores).
## Credits:
