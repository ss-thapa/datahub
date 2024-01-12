import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
pd.set_option('display.max_column', None)


df1 = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/world_population/world_country_stats.csv')
df2 = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/world_population/world_population_by_country_2023.csv')
df_population = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/world_population/world_population_by_year_1950_2023.csv')


df1 = df1.drop(columns=['fertility_rate', 'median_age'])



df_stats = pd.merge(df1, df2, on='country')



columns = ['country', 'region', 'land_area_x', 'population', 'yearly_change','net_change', 'density', 'land_area_y', 'net_migrants',
       'fertility_rate', 'median_age', 'population_urban', 'world_share']





## top 10 countries with highest land

# top_10_country = df_stats.groupby(['country', 'region']).agg(area=('land_area_x', 'max')).sort_values(by='area',ascending=False).head(10)
# sns.catplot(kind='bar', data=top_10_country, x='country', y='area', hue='region')
# plt.xticks(rotation=45)
# plt.show()


# df_stats.groupby('country')['land_area_x'].max().sort_values(ascending=False).head(10).plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()



## top 10 countries with low land

# df_stats.groupby('country')['land_area_x'].max().sort_values(ascending=False).tail(10).plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

# bottom_10_country = df_stats.groupby(['country', 'region']).agg(area=('land_area_x', 'max')).sort_values(by='area',ascending=False).tail(10)
# sns.catplot(kind='bar', data=bottom_10_country, x='country', y='area', hue='region')
# plt.xticks(rotation=45)
# plt.show()


## country and density top 10


# top_10_densed = df_stats.groupby(['country','region']).agg(density=('density', 'max')).sort_values(by='density', ascending=False).head(10)
# sns.catplot(kind='bar', data=top_10_densed,x='country', y='density', hue='region' )
# plt.xticks(rotation=45)
# plt.show()

# df_stats.groupby('country').agg(density=('density', 'max')).sort_values(by='density', ascending=False).head(10).plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

## country and density bottom 10

bottom_10_densed = df_stats.groupby(['country','region']).agg(density=('density', 'max')).sort_values(by='density', ascending=False).tail(10)
# sns.catplot(kind='bar', data=bottom_10_densed,x='country', y='density', hue='region' )
# plt.xticks(rotation=45)
# plt.show()

# df_stats.groupby('country').agg(density=('density', 'max')).sort_values(by='density', ascending=False).head(10).plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()




