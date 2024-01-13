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

population_columns_nepal = df_population.columns[2:]

transformed_data_nepal = pd.melt(frame=nepal_only, id_vars=['country'], value_vars=population_columns_nepal, var_name='year', value_name='population')
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

#transforming year as int for creating bins

transformed_data_nepal['year'] = transformed_data_nepal['year'].astype(int)
## Create bins
bin_labels_nepal = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
transformed_data_nepal['year_bins'] = pd.cut(transformed_data_nepal['year'], bins=range(1950, 2031, 10), labels=bin_labels_nepal, right=False)

# sns.relplot(kind='line', data=transformed_data_nepal, x='year', y='population', height=6, aspect=2, markers=True, style="year_bins", markersize=8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {nepal_only.iloc[0]["country"]}')
# plt.xticks(rotation=90)
# plt.xlabel('year')
# plt.ylabel('population')
# plt.grid(True)
# plt.show()



### population change of india over the years 

india_only = df_population[df_population['country'] == 'India']

population_columns_india = df_population.columns[2:]

transformed_data_india = pd.melt(india_only, id_vars=['country'], value_vars=population_columns_india, var_name='year', value_name='population')

## Convert 'year' to numerical values for creating bins
transformed_data_india['year'] = transformed_data_india['year'].astype(int)

## Create bins
bin_labels_india = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
transformed_data_india['year_bins'] = pd.cut(transformed_data_india['year'], bins=range(1950, 2031, 10), labels=bin_labels_india, right=False)


## Set the figure size using relplot's height parameter
# sns.relplot(kind='line', data=transformed_data_india, x='year', y='population', height=6, aspect=2, markers=True, style='year_bins', markersize=8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {india_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()



## population change of china over the years 

china_only = df_population[df_population['country']== 'China']

population_columns_china = df_population.columns[2:]

transformed_data_china = pd.melt(china_only, id_vars=['country'], value_vars=population_columns_china, var_name='year', value_name='population')

transformed_data_china['year'] = transformed_data_china['year'].astype(int)

bin_labels_china = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]

transformed_data_china['year_bins'] = pd.cut(transformed_data_china['year'], bins=range(1950, 2031, 10), labels=bin_labels_china, right=False)

# sns.relplot(kind='line', data=transformed_data_china, x='year', y='population', height=6, aspect=2, markers=True, style='year_bins', markersize = 8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {china_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()



## combined graph of india nepal and china

combines_data = pd.concat([transformed_data_nepal, transformed_data_india, transformed_data_china], ignore_index=True)


# sns.relplot(kind='line', data=combines_data, x='year', y='population',hue='country', height=6, aspect=2, markers=True, style='year_bins', markersize = 8, linestyle='--', ci=None)
# plt.title('Population change trend')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()




## population growth according to the region 


# transformed_data_continent = pd.melt(df_population, id_vars=['country', 'region'], var_name='year', value_name='population')

# transformed_data_continent['year'] = transformed_data_continent['year'].astype(int)

# bin_labels_all =  [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]

# transformed_data_continent['year_bins'] = pd.cut(transformed_data_continent['year'], bins=range(1950, 2031, 10), labels=bin_labels_all, right=False)


# sns.relplot(kind='line', data=transformed_data_continent, x='year', y='population',hue='region', height=6, style='year_bins', markersize = 8, linestyle='--', aspect=2, markers=True, ci=None)
# plt.title('Population change trend')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()




## japan only

# Japan_only = df_population[df_population['country'] == 'Japan']

# population_columns_Japan = df_population.columns[2:]

# transformed_data_Japan = pd.melt(Japan_only, id_vars=['country'], value_vars=population_columns_Japan, var_name='year', value_name='population')

# ## Convert 'year' to numerical values for creating bins
# transformed_data_Japan['year'] = transformed_data_Japan['year'].astype(int)

# ## Create bins
# bin_labels_Japan = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
# transformed_data_Japan['year_bins'] = pd.cut(transformed_data_Japan['year'], bins=range(1950, 2031, 10), labels=bin_labels_Japan, right=False)


# # Set the figure size using relplot's height parameter
# sns.relplot(kind='line', data=transformed_data_Japan, x='year', y='population', height=6, aspect=2, markers=True, style='year_bins', markersize=8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {Japan_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()





# Canada_only = df_population[df_population['country'] == 'Canada']

# population_columns_Canada = df_population.columns[2:]

# transformed_data_Canada = pd.melt(Canada_only, id_vars=['country'], value_vars=population_columns_Canada, var_name='year', value_name='population')

# ## Convert 'year' to numerical values for creating bins
# transformed_data_Canada['year'] = transformed_data_Canada['year'].astype(int)

# ## Create bins
# bin_labels_Canada = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
# transformed_data_Canada['year_bins'] = pd.cut(transformed_data_Canada['year'], bins=range(1950, 2031, 10), labels=bin_labels_Canada, right=False)


# # Set the figure size using relplot's height parameter
# sns.relplot(kind='line', data=transformed_data_Canada, x='year', y='population', height=6, aspect=2, markers=True, style='year_bins', markersize=8, linestyle='--')
# plt.title(f'Population Changes Over the Years for {Canada_only.iloc[0]["country"]}')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.grid(True)
# plt.show()





def change_country(country:str):
    df_population = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/world_population/world_population_by_year_1950_2023.csv')
    country_only = df_population[df_population['country'] == country]

    population_columns = df_population.columns[2:]

    transformed_data = pd.melt(country_only, id_vars=['country'], value_vars=population_columns, var_name='year', value_name='population')

    transformed_data['year'] = transformed_data['year'].astype(int)

    bin_labels = [f'{start}-{end}' for start, end in zip(range(1950, 2024, 10), range(1960, 2031, 10))]  # Adjust bin ranges as needed
    transformed_data['year_bins'] = pd.cut(transformed_data['year'], bins=range(1950, 2031, 10), labels=bin_labels, right=False)

    sns.relplot(kind='line', data=transformed_data, x='year', y='population', height=6, aspect=2, markers=True, style='year_bins', markersize=8, linestyle='--')
    plt.title(f'Population Changes Over the Years for {country_only.iloc[0]["country"]}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()


# change_country('Portugal')








