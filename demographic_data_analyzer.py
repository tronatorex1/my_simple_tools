# tronatorex1 : 20240502
# Exercise1 : Mean-Variance-Standard Deviation Calculator (freecodecamp)
"""
+How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
What is the average age of men?
What is the percentage of people who have a Bachelor's degree?
What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
What percentage of people without advanced education make more than 50K?
What is the minimum number of hours a person works per week?
What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.
"""
import pandas as pd
import numpy as np

def read_csv():
    csv_file = r"adult.data.csv"
    df = pd.read_csv(csv_file,
                    na_values=[' '], 
                    skiprows=0,
                    names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']) 
    df.shape
    df.info

avg_men = df.mean([df['sex'] == "Male"])# / df['age'].size

df.iloc[:, 0].mean



# df.query('age > 50' & 'salary = ')
df.query('sex = "Male"')
