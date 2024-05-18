# These are examples on how to merely access and fill Pandas' df with data
#   Data coming from CSV or TXT files only (not html, this is another procedure) and saving results to TXT or CSV

import pandas as pd

# 1 Creting a DF manually
certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

# Adding user's headers instead of default numbering 
names = ['Tom', 'Kris', 'Ahmad', 'Beau']
certificates_earned.index = names

# Creating and adding an additional serie based upon the index (names) already existing
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak
print(certificates_earned)

# More operations on series within the DF
certificates_earned['Certificates per month'] = 
round(
    certificates_earned['Certificates'] /
    certificates_earned['Time (in months)'], 2)


# 2 Dealig with an file to open, process and save the selected modified information
file = r"C:\ALEX\SW\Coding\Python\Jupyter\RDP-Reading-Data-with-Python-and-Pandas-master\unit-1-reading-data-with-python-and-pandas\lesson-1-reading-csv-and-txt-files\files\btc-market-price.csv"
with open(file, 'r') as reader:
    content = reader.read()

for i in content.splitlines():
    print(i)


# 2.1
import pandas as pd
csv_file = "c:/ALEX/SW/Coding/Python/Jupyter/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/btc-market-price.csv"
df = pd.read_csv(csv_file,
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'},
                 index_col=[0],
                 parse_dates=[0]) # this last auto detects Timestampt as date type 
# df['Timestamp'] = pd.to_datetime(df['Timestamp']) # casts col TImestamp into date
df.dtypes

# 2.2 
csv_file = "c:/ALEX/SW/Coding/Python/Jupyter/RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/exam_review.csv"
df = pd.read_csv(csv_file, sep='>', decimal=',', skip_blank_lines=True, usecols=['last_name','math_score']) # select cols by name
df = pd.read_csv(csv_file, sep='>', decimal=',', skip_blank_lines=True, usecols=[1,3]) # select cols by position
df = pd.read_csv(csv_file, sep='>', decimal=',', skip_blank_lines=True, usecols=[4]) # select 1 col = only a serie, not a df
# A serie is a 1 dim data set; a DF is a 2-dim or more data set
serie1 = pd.read_csv(csv_file, sep='>', usecols=['last_name']) # a 1 dim data set

# Exporting into file in JSON format the selected data and then print the saved data from file
serie1.to_json(r'c:\tmp\exam_review.JSON')
serie2 = pd.read_json(r'c:\tmp\exam_review.JSON')
print(serie2)


################################################################

file = r"C:\TMP\birthplace-2018-census-csv.csv"
import pandas as pd
pd.read_csv(file, sep=',', na_values=['?'], na_filter='replace')

################################################################
import pandas as pd
import numpy as np
file = r"C:\ALEX\SW\Coding\Python\Jupyter\RDP-Reading-Data-with-Python-and-Pandas-master\unit-1-reading-data-with-python-and-pandas\lesson-2-load-movies-dataset\files\movies1.csv"
column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'gross', 'movie_title', 'num_user_for_reviews', 'country', 'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']
pd.read_csv(file, names=column_names, na_values=['', '?', '-'])

################################################################
import pandas as pd
file_ = r"C:\Users\trona\OneDrive\Desktop\unit-1-reading-data-with-python-and-pandas\lesson-4-tsv-with-the-simpsons-episodes\files\simpsons-episodes.tsv"
col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season', 'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
pd.read_csv(file_, sep='\t')
select_cols = ['Title','Air date','Production code','IMDB rating']
pd.read_csv(file_, sep='\t', names=col_names, usecols=select_cols, )

simpsons = pd.read_csv('simpsons-episodes.tsv',
                 sep='\t',
                 encoding='UTF-8',
                 names=col_names,
                 usecols=select_cols,
                 skiprows=4,
                 index_col='Production code',
                 na_values=['no_val'],
                 parse_dates=['Air date'])


