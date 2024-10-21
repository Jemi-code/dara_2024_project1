#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:42:56 2024

@author: dara
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")

#print(file)
#print(file.info())
#print(file.Rating.describe())

data = {
        'Rank': file.Rank,
        'Title': file.Title,
        'Genre': file.Genre,
        'Description': file.Description,
        'Director': file.Director,
        'Actors': file.Actors,
        'Year': file.Year,
        'Runtime/m': file.Runtime_minutes,
        'Rating': file.Rating,
        'Votes': file.Votes,
        'Revenue/mil': file.Revenue_Millions,
        'Metascore': file.Metascore,
        }

df = pd.DataFrame(data)
#print(df.Rating)

print(df['Title'][df['Rating'] > 10])