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


top_10_densed = df_stats.groupby(['country','region']).agg(density=('density', 'max')).sort_values(by='density', ascending=False).head(10)
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




## country region and fertility rate
# df_stats['fertility_rate'].plot(kind='box')
# plt.show()

# print(df_stats[df_stats['fertility_rate'] > 5])

top_10_fertile = df_stats.groupby(['country','region']).agg(fertile=('fertility_rate', 'max')).sort_values(by='fertile', ascending=False).head(10)
# sns.catplot(kind='bar', data=top_10_fertile,x='country', y='fertile', hue='region' )
# plt.xticks(rotation=45)
# plt.show()



bottom_10_fertile = df_stats.groupby(['country','region']).agg(fertile=('fertility_rate', 'max')).sort_values(by='fertile', ascending=False).tail(10)
# sns.catplot(kind='bar', data=bottom_10_fertile,x='country', y='fertile', hue='region' )
# plt.xticks(rotation=45)
# plt.show()




df_population = pd.merge(df_stats[['country', 'region']],df_population, on='country')  ## merging region column in the population dataframe 



## population change of nepal over the years 

nepal_only = df_population.loc[df_population['country'] == 'Nepal']

population_columns = df_population.columns[2:]


# plt.figure(figsize=(10, 6))
# plt.plot(nepal_only[population_columns].values.flatten(), marker='o', linestyle='-', color='skyblue')
# plt.title(f'Population Changes Over the Years for {nepal_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.fill_between(range(len(population_columns)), nepal_only[population_columns].values.flatten(), color='skyblue', alpha=0.7)
# plt.title(f'Population Changes Over the Years for {nepal_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()


## using seaborn

transformed_data_nepal = pd.melt(frame=nepal_only, id_vars=['country'], value_vars=population_columns, var_name='year', value_name='population')
#transforming year as int for creating bins
transformed_data_nepal['year'] = transformed_data_nepal['year'].astype(int)
# Create bins
bin_labels = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
transformed_data_nepal['Year Bins'] = pd.cut(transformed_data_nepal['year'], bins=range(1950, 2031, 10), labels=bin_labels, right=False)

# sns.relplot(kind='line', data=transformed_data_nepal, x='year', y='population', height=6, aspect=2, markers=True, style="Year Bins", markersize=8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {nepal_only.iloc[0]["country"]}')
# plt.xticks(rotation=90)
# plt.xlabel('year')
# plt.ylabel('population')
# plt.grid(True)
# plt.show()



## population change of india over the years 

india_only = df_population[df_population['country']=='India']

population_columns = df_population.columns[2:]

transformed_data_india = pd.melt(india_only, id_vars=['country'], value_vars=population_columns, var_name='Year', value_name='Population')




# plt.figure(figsize=(12,6))
# sns.relplot(kind='line', data=transformed_data_india, markers='o', x='Year', y='Population')
# plt.title(f'Population Changes Over the Years for {india_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()



# plt.figure(figsize=(12, 6))
# sns.lineplot(x='Year', y='Population', data=melted_data, marker='o', color='skyblue')
# plt.title(f'Population Changes Over the Years for {nepal_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()

