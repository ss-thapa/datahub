import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
pd.set_option('display.max_column', None)




df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/sun_data.csv')

df = df.rename(columns= {'Name':'name', 'Platform':'platform', 'Year':'year', 'Genre':'genre', 'Publisher':'publisher',
       'NA_Sales':'na_sales', 'EU_Sales':'eu_sales', 'JP_Sales':'jp_sales', 'Other_Sales':'other_sales', 'Global Sales':'global_sales'})


# print(df[[col for col in df.columns if df[col].nunique() > 50]])

# print(df['year'].value_counts())


# df['genre'].value_counts().sort_index().plot.bar()
# plt.show()


##loc[] and iloc[]
##start:stop:step
# df.iloc[0:10:2]


## slicing with columns and rows

# print(df.iloc[:,0:4])
# print(df.iloc[0:11, 3:6])


# print(df.loc[:5, 'platform'])


# print(df.loc[58, 'genre'])


### filter with conditional logic using loc[] method 

# for i in df[['name', 'platform', 'year', 'genre', 'publisher']]:
#     print(i.upper())
#     print(df[i].unique())



### select everything where the platfrom is Wii
# wii = df['platform'] == 'Wii'
# print(df.loc[wii].head())
## OR
# print(df.loc[df['platform']=='Wii'].shape)



### select names of the game where japan sales is greater the eu_sales
# sun2 = df.loc[df['jp_sales'] > df['eu_sales']]


###select names of the ga,e where japan sales is greater then na_sales, eu_sales and other sales
# sun = df.loc[(df['jp_sales'] > df['eu_sales']) & (df['jp_sales'] > df['na_sales']) & (df['jp_sales'] > df['other_sales']), 'name']


###all roll-playing game with nintando wii

# sun3 = df.loc[(df['platform'] == 'Wii') & (df['genre'] == 'Role-Playing')].sort_values(by='global_sales', ascending=False)


### filter with or condition 

sun4 = df.loc[(df['genre']== 'Action') | (df['genre']== 'Shooter')]


### filter with both or and And 


sun5 = df.loc[(df['year'] >= 2010) & ((df['genre'] == 'Action') | (df['genre']== 'Shooter'))]



### Top 3 publishers isin() method

top_3_publishers = df['publisher'].isin(['Electronic Arts','Activision', 'Namco Bandai Games'])

df.loc[top_3_publishers]


### top 3 publichers where genres are sports action or shooter and sales >= 2m

genres = df['genre'].isin(['Sports', 'Action', 'Shooter'])

sales_2m = df['global_sales'] >= 2

df.loc[genres & top_3_publishers & sales_2m]


# between method

between_2m_10m = df['global_sales'].between(2,10)

y_90s = df['year'].between(1990, 1999)
y_00s = df['year'].between(2000, 2009)
y_10s = df['year'].between(2010, 2019)


df.loc[between_2m_10m & y_90s, 'genre'].value_counts(normalize=True).round(2)

df.loc[between_2m_10m & y_00s, 'genre'].value_counts(normalize=True).round(2)

df.loc[between_2m_10m & y_10s, 'genre'].value_counts(normalize=True).round(2)



# negating just genre condition
df.loc[df['genre'].isin(['Puzzles', 'Strategy', 'Adventure']) & y_10s].head(4).reset_index(drop=True)


# negating the both geanre and year condition
df.loc[-(df['genre'].isin(['Puzzles', 'Strategy', 'Adventure']) & y_10s)].head(4).reset_index(drop=True)


## find out which racing games had the highest sales in eu compared to na, jp and other sales between the year 2000-2009

#longer version
df.loc[(df['genre'] == 'Racing') & (df['year'].between(2000, 2009)) & ((df['eu_sales'] > df['na_sales']) & (df['eu_sales'] > df['jp_sales']) & (df['eu_sales'] > df['other_sales'])), ['name', 'eu_sales']].sort_values(by='eu_sales',ascending=False).reset_index(drop=True)

# break down version

racing = df['genre'] == 'Racing'
year_1w = df['year'].between(2000, 2009)
higher_then_other = (df['eu_sales'] > df['na_sales']) & (df['eu_sales'] > df['jp_sales']) & (df['eu_sales'] > df['other_sales'])

df.loc[(racing & year_1w & higher_then_other), ['name', 'eu_sales']].sort_values(by='eu_sales', ascending=False).reset_index(drop=True)



#### unique() and ununique


# print(df['platform'].unique())
# print(df.nunique())

# print(df.select_dtypes('object'))

# for i in df.select_dtypes('object'):     ### itirating orver all the columns which have object datatypes and printing the unique values of those columns
#     print(df[i].unique())

ps3 = df.loc[df['platform'] == 'PS3']

### nlargest and nsmallest

ps3.nlargest(n=10, columns = 'na_sales').set_index('name').loc[:,'na_sales']

ps3.nsmallest(n=5, columns='global_sales').loc[:, ('name', 'global_sales')]




### matplot

# fig, ax = plt.subplots(2,2, figsize =(20,20))


# ps3.nlargest(n=10, columns = 'na_sales').set_index('name').loc[:,'na_sales'].plot.bar(ax = ax[0][0])
# ax[0][0].set_title('North America')

# ps3.nlargest(n=10, columns = 'jp_sales').set_index('name').loc[:,'jp_sales'].plot.bar(ax = ax[0][1])
# ax[0][1].set_title('Japan')

# ps3.nlargest(n=10, columns = 'eu_sales').set_index('name').loc[:,'eu_sales'].plot.bar(ax = ax[1][0])
# ax[1][0].set_title('Europe')

# ps3.nlargest(n=10, columns = 'other_sales').set_index('name').loc[:,'other_sales'].plot.bar(ax = ax[1][1])
# ax[1][1].set_title('Other')


# fig.suptitle("Most Sold PS3 Games By Continent", fontsize = 20)
# fig.tight_layout()
# plt.show()
# # fig.savefig('ps3_sales.jpg')



## value_counts()


# top_100 = ps3.nlargest(n=100, columns='global_sales')

# top_100['genre'].value_counts(normalize=True)


# #barh subplots

# fig, ax = plt.subplots(1,2, figsize = (16,8))

# top_100['genre'].value_counts(normalize=True).plot.barh(ax=ax[0])

# top_100['publisher'].value_counts(normalize=True).plot.barh(ax=ax[1])
# fig.tight_layout()
# plt.show()




## sort_values


# print(ps3.sort_values(by='genre', ascending=True))
# print(ps3.sort_values(by='year',ascending=False))
print(ps3.sort_values(by= ['year','global_sales'], ascending=False))


