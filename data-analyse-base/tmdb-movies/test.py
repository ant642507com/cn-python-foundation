# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:50:25 2018

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt

movie_df = pd.read_csv('tmdb-movies.csv')

tmp_df = movie_df.head(10)

movie_df.dropna(axis=0, inplace=True, subset=list(['genres']))
movie_df.dropna(axis=0, inplace=True, subset=list(['director']))

def deal_columns_to_rows(movie_df, columnName):
    movie_type_df = movie_df[columnName].str.split('|', expand=True)

    movie_type_df['id'] = movie_df['id']
    
    movie_df_merged = movie_df.merge(movie_type_df)
    
    movie_df_merged.drop_duplicates(subset=None, keep='first', inplace=True)
    
    movie_column = movie_df.columns.values.tolist()
    
    movie_column.remove(columnName)
    
    melted = pd.melt(movie_df_merged, id_vars=movie_column, value_vars=[0, 1, 2, 3, 4],
                     value_name=columnName+'_uniq').drop('variable', axis = 1).dropna()
    
    return melted

melted = deal_columns_to_rows(movie_df, 'genres')

dealed_df = melted.copy()

"""
根据电影种类，统计出最受欢迎的电影类型

mean_dealed_df = dealed_df.groupby('genres_uniq')['popularity'].mean().sort_values(ascending=False)

mean_dealed_df.plot(kind='bar', figsize=(10, 10))
plt.title('Genres VS Average Popularity')
plt.ylabel('popularity')
plt.xlabel('genres')
"""

"""
在最受欢迎的种类的电影中，都是由哪些年出的作品，数量占比是怎样的
"""
popular_df = melted.query('genres_uniq==\'Adventure\'')
#melted = deal_columns_to_rows(popular_df, 'release_year')

dealed_cast_df = melted.copy()

count_of_cast = dealed_cast_df.groupby('release_year')['release_year'].count()

count_of_cast.plot(kind='line',figsize=(18, 18))

plt.ylabel('count')
plt.title('Release Year VS Publish Count With Adventure Movies')


