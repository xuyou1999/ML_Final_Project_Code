# ML_Final_Project_Code
db_class.py: class MyDb, can be used to fetch data from database

DoubanAPI.py: class DoubanAPI, API for Douban, can be used to obtain movie information on Douban

logger_class.py: class Logger, serves as logger, can be used to track information of program execution

extract_id.py: obtain movie IDs on Douban, can set sample size in this file

extract_data.py: extract detailed movie data from Douban, and insert into database

load_data.py: fetch data from database, and save to csv files

The number of lines in "..._pred_avg.csv" and "..._empty.csv" should add up to 3506 (number of movies/sample size).