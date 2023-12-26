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

sun3 = df.loc[(df['platform'] == 'Wii') & (df['genre'] == 'Role-Playing')].sort_values(by='global_sales', ascending=False)


### filter with or condition













