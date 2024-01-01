import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option('display.max_column', None)





df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/netflix_1.csv')


df = df.rename(columns={'Title':'title', 'Available Globally?':'global_available', 'Release Date':'release_date', 'Hours Viewed':'hours_viewed',
       'Number of Ratings':'no_of_ratings', 'Rating':'rating', 'Genre':'genre', 'Key Words':'key_words', 'Description':'description'})

columns_with_zeros = df.columns[df.eq('0').any()].tolist()

df = df[(df['release_date'] != '0') & (df['release_date'] != 'Release Date')]

df['release_date'] = pd.to_datetime(df['release_date'])

df['hours_viewed'] = df['hours_viewed'].astype(int)

df = df.drop([3591, 7181, 7180])


df = df[df['no_of_ratings'] != "Number of Ratings"]

df['rating'] = df['rating'].astype(float)

df['no_of_ratings'] = pd.to_numeric(df['no_of_ratings'])


## mask returns the boolean value where the datas of genre does or doent start and end with []
mask = ~df['genre'].str.startswith('[') | ~df['genre'].str.endswith(']')

## changing the true values and adding [] to those object
df.loc[mask, 'genre'] = '[' + df.loc[mask, 'genre'] + ']'


top10_movies_with_highest_ratings = df.nlargest(n=10,columns='rating').loc[:,['title', 'rating']].reset_index(drop=True)

bottom10_movies_lowest_rating = df.nsmallest(n=10, columns='rating').loc[:, ['title', 'rating']].reset_index(drop=True)



year_12_14= df['release_date'].dt.year.between(2012, 2014)
year_15_17= df['release_date'].dt.year.between(2015, 2017)
year_18_20= df['release_date'].dt.year.between(2018, 2020)
year_21_23= df['release_date'].dt.year.between(2021, 2023)


view_time_less_40 = df['hours_viewed'] < 400000000
view_time_more_40 = df['hours_viewed'] > 400000000



## all movies which were between 2012-2014 and whose view time were less the 40crore and it is globally available 

# print(df.loc[view_time_less_40 & year_12_14 & (df['global_available']== 'Yes')])

## all movies which were between 2012-2014 and whose view time were less the 40crore and it is globally available  and show only mentioned tables

# print(df.loc[(view_time_less_40 & year_12_14 & (df['global_available']== 'Yes')), ['title', 'release_date', 'hours_viewed']].reset_index(drop=True))

##all movies which are between 2021 and 2023 view time more then 40 crore and not globally available

# print(df.loc[(year_21_23) & (view_time_more_40) & (df['global_available']=='No')].shape) 




## correlation there is no corelation between hous_viewed no of rating and rating 

# print(df.select_dtypes(['int64', 'float64']).corr())


##aggriators

# print(df['rating'].mean())


# print(df[['rating', 'hours_viewed', 'no_of_ratings']].agg({'rating':['mean', 'median'], 'hours_viewed':['mean', 'median', 'min', 'max'], 'no_of_ratings': ['mean', 'median', 'min', 'max']}).unstack()) 




## cut and qcut

# print(pd.cut(x=df['hours_viewed'], bins=5).value_counts())


# print(pd.qcut(x = df['hours_viewed'], q=4, precision=50).value_counts())




##groupby


# print(df.groupby('global_available')['no_of_ratings'].count())

# average_rating = df.groupby('global_available')['rating'].count()


# average_rating.plot.bar()
# plt.show()



sns.relplot(data=df, x='hours_viewed', y='no_of_ratings', kind='scatter', hue='global_available')
plt.show()

