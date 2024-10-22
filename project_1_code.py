# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:38:45 2024

@author: JEMIMA
"""

import pandas as pd
#pd.reset_option('all')

"""

#Load csv file
df = pd.read_csv("movie_dataset.csv")

#pd.reset_option('display.max_columns') 

#Renaming columns Runtime (Minutes) and Revenue (Millions)
df.columns = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime_minutes',
             'Rating', 'Votes', 'Revenue_millions', 'Metascore']

#Dropping Rank column
df.drop(['Rank'], inplace=True, axis=1)

#Changing Year to proper integer format
df['Year'] = df['Year'].astype(int) 

#There are some few empty cells the Revenue_millions column so I'm finding the mean and using that to replace em
revenue_ave = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(revenue_ave, inplace=True)

#Doing same for metascore column
metascore_ave = df["Metascore"].mean()
df["Metascore"].fillna(metascore_ave, inplace=True)

# Create a new 'Rank' column starting from 1
df['Rank'] = df.index + 1
#making this Rank the first column
df = df[['Rank'] + [col for col in df.columns if col != 'Rank']]

#Saving(loading) the cleaned data removing the panda index
df.to_csv("movie_dataset_cleaned.csv", index=False)
#print(df_clean)

"""


#Now solving the questions using the cleaned data
df_clean = pd.read_csv("movie_dataset_cleaned.csv")




"""
Question 1
What is the highest rated movie in the dataset?

python output
54    The Dark Knight
Name: Title, dtype: object
"""

#Find the highest rating
#print(df_clean['Rating'].max())
#print(df_clean['Title'][df_clean['Rating'] == 9.0].astype(str))

"""
What is the average revenue of all movies in the dataset? 

python output
82.95637614678898
"""

#print(df_clean['Revenue_millions'].mean())



"""
Question 3

What is the average revenue of movies from 2015 to 2017 in the dataset?
Note, since the answer will be effected by how you dealt with missing values a range has been provided. 

python output
63.44658789732184
"""

# Figuring out unique values in the 'Year' column
#print("Unique values in 'Year':", df_clean['Year'].unique())
#Unique values in 'Year': [2014 2012 2016 2015 2007 2011 2008 2006 2009 2010 2013]

# Filter the DataFrame for years greater than 2015 only
filtered_ave_revenue = df_clean['Revenue_millions'][df_clean['Year'] > 2015]

# Find the avereage filtered DataFrame
#print(filtered_ave_revenue.mean())



"""
Question 4

How many movies were released in the year 2016?

python output
297
"""

movies_2016 = df_clean[df_clean['Year'] == 2016]
#print(len(movies_2016))


"""
Question 5

How many movies were directed by Christopher Nolan?

python output
5
"""

chris_movies = df_clean[df_clean['Director'] == 'Christopher Nolan']
#print(len(chris_movies))


"""
Question 6

How many movies in the dataset have a rating of at least 8.0?

python output
78
"""

rating_least_8 = df_clean[df_clean['Rating'] >= 8.0]
#print(len(rating_least_8))



"""
Question 7

What is the median rating of movies directed by Christopher Nolan?

python output
8.680000000000001
"""

chris_movies_rating = df_clean['Rating'][df_clean['Director'] == 'Christopher Nolan']
#print(chris_movies_rating.mean())


"""
Question 8

Find the year with the highest average rating?

python output
2006
"""

average_ratings = df_clean.groupby('Year')['Rating'].mean()
average_ratings_1dec = average_ratings.round(1)
#print(average_ratings_1dec)
"""
2006    7.1
2007    7.1
2008    6.8
2009    7.0
2010    6.8
2011    6.8
2012    6.9
2013    6.8
2014    6.8
2015    6.6
2016    6.4
Name: Rating, dtype: float64
"""

#idxmax() returns the index (year) of the maximum average rating.
highest_avg_rating_year = average_ratings_1dec.idxmax() 
max_ave_rating = average_ratings_1dec.max()
#print(highest_avg_rating_year)


"""
Question 9

What is the percentage increase in number of movies made between 2006 and 2016?

python output
85.18518518518519
"""
#Find movies made in 2006 and 2016
count_2006 = len(df_clean[df_clean['Year'] == 2006])
count_2016 = len(df_clean[df_clean['Year'] == 2016])
#print(count_2006)
#44
#print(count_2016)
#297

#percentage increase
percentage_increase = (count_2016-count_2006)/count_2016 * 100
#print(percentage_increase)


"""
Question 10
Find the most common actor in all the movies?

Note, the "Actors" column has multiple actors names. You must find a way to search for the most common actor in all the movies.
"""

"""
Question 11
How many unique genres are there in the dataset?

Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.
"""

"""
Question 12
Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

And what advice can you give directors to produce better movies?
"""

"""
For raw unfiltered data
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None

For column names changes and rank removed

RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Title             1000 non-null   object 
 1   Genre             1000 non-null   object 
 2   Description       1000 non-null   object 
 3   Director          1000 non-null   object 
 4   Actors            1000 non-null   object 
 5   Year              1000 non-null   int64  
 6   Runtime_minutes   1000 non-null   int64  
 7   Rating            1000 non-null   float64
 8   Votes             1000 non-null   int64  
 9   Revenue_millions  872 non-null    float64
 10  Metascore         936 non-null    float64
dtypes: float64(3), int64(3), object(5)
memory usage: 86.1+ KB
None


Cleaned data .info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Rank              1000 non-null   int64  
 1   Title             1000 non-null   object 
 2   Genre             1000 non-null   object 
 3   Description       1000 non-null   object 
 4   Director          1000 non-null   object 
 5   Actors            1000 non-null   object 
 6   Year              1000 non-null   int64  
 7   Runtime_minutes   1000 non-null   int64  
 8   Rating            1000 non-null   float64
 9   Votes             1000 non-null   int64  
 10  Revenue_millions  1000 non-null   float64
 11  Metascore         1000 non-null   float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""
