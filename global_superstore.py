import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_column', None)





df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/superstore.csv')

df=df.drop(columns=['记录数', 'Market', 'Year', 'weeknum'], axis=1)

df=df.rename(columns={'Category':'category', 'City':'city', 'Country':'country', 'Customer.ID':'customer_id', 'Customer.Name':'customer_name',
       'Discount':'discount','Order.Date':'order_date', 'Order.ID':'order_id', 'Order.Priority':'order_priority',
       'Product.ID':'product_id', 'Product.Name':'product_name', 'Profit':'profit', 'Quantity':'quantity', 'Region':'region', 'Row.ID':'row_id',
       'Sales':'total_sales_amount', 'Segment':'segment', 'Ship.Date':'ship_date', 'Ship.Mode':'ship_mode', 'Shipping.Cost':'shipping_cost', 'State':'state',
       'Sub.Category':'sub_category','Market2':'market2'})

df['order_date'] =pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
# df['year'] = pd.to_datetime(df['year'])



categorical_columns = ['category', 'city', 'country', 'order_priority', 'region', 'segment', 'ship_mode', 'state', 'sub_category', 'market2',]

for column in categorical_columns:
    df[column].value_counts()


df['cost_per_unit'] = round(df['total_sales_amount'] / df['quantity'], 2)


## category
df['category'].value_counts()


## city 

df['city'].value_counts().head(5)

# df['city'].value_counts().head(5).plot(kind='bar')
# plt.xticks(rotation = 45)
# plt.show()


## country

df['country'].value_counts().head()

# df['country'].value_counts().head(5).plot(kind='bar')
# plt.xticks(rotation = 45)
# plt.show()


## discount 

df['discount'].describe()

# sns.boxplot(data=df, x='discount')
# plt.show()


# print(df[df['discount'] > 0.5]['discount'].skew())

# print(df[df['discount'] <= 0.5]['discount'].skew())


## order_priority


df['order_priority'].value_counts()


# df['order_priority'].value_counts().head(5).plot(kind='bar')
# plt.xticks(rotation = 45)
# plt.show()



## quantity 

# print(df[df['quantity'] >= 9].shape)

# print(df['quantity'].skew())

# df['quantity'].plot(kind='box')
# plt.show()




## region

# df['region'].value_counts()


# df['region'].value_counts().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()



##total_sales_amount

# print(df['total_sales_amount'].skew())

# sns.boxplot(data=df, x='total_sales_amount')
# plt.show()


# print(df['total_sales_amount'].describe())




## segment

# print(df['segment'].value_counts())

# df['segment'].value_counts().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()      



# order_date

# print(df['order_date'].min())
# print(df['order_date'].max())

# print(df['order_date'].max() - df['order_date'].min())


# adding new column with the information of the days took to ship a product

df['days_took_to_ship'] = (df['ship_date'] - df['order_date']).dt.days


## days

# print(df['days_took_to_ship'].describe())


## ship_mode

# df['ship_mode'].value_counts()


# df['ship_mode'].value_counts().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()    

## shipping cost 

# print(df['shipping_cost'].describe())

# sns.boxplot(data=df, x='shipping_cost')
# plt.show()

# print(df['shipping_cost'].skew())


# sub_category

# df['sub_category'].value_counts()


# df['sub_category'].value_counts().plot(kind='barh')
# plt.xticks(rotation = 45)
# plt.show()




### Multivariate and bivariate analysis


categorical_columns = ['category', 'city', 'country', 'order_priority', 'region', 'segment', 'ship_mode', 'state', 'sub_category', 'market2',]

numerical_columns = ['discount', 'profit', 'quantity', 'total_sales_amount','days_took_to_ship', 'cost_per_unit', 'shipping_cost' ]


# print(df[numerical_columns].cror())


## total sales amount and all others relationship

#total sales amount and category
# sns.catplot(kind='bar', data=df, x='category', y='total_sales_amount', errorbar=None, estimator='sum')
# plt.show()


# print(df.groupby('category')['total_sales_amount'].describe())


## total sales amount and order_priority

# sns.catplot(kind='bar', data=df, x='category', y='total_sales_amount', errorbar=None, estimator='sum')
# plt.show()


# print(df.groupby('order_priority')['total_sales_amount'].describe())


# print(df['total_sales_amount'].describe())

# df1 = df[df['profit'] < 0]

# # df2 = df[df['profit'] > 0]



## total sales amount and region


# sns.catplot(kind='bar', data=df, x='region', y='total_sales_amount', errorbar=None, estimator='sum')
# plt.xticks(rotation=45)
# plt.show()

# sns.catplot(kind='bar', data=df, x='region', y='total_sales_amount', errorbar=None, estimator='mean')
# plt.xticks(rotation=45)
# plt.show()

# print(df.groupby('region')['total_sales_amount'].describe())



# total sales amount and segment

# sns.catplot(kind='bar', data=df, x='segment', y='total_sales_amount', errorbar=None, estimator='sum')
# plt.title('sum')
# plt.xticks(rotation=45)


# sns.catplot(kind='bar', data=df, x='segment', y='total_sales_amount', errorbar=None, estimator='mean')
# plt.title('average')
# plt.xticks(rotation=45)
# plt.show()

# print(df.groupby('segment')['total_sales_amount'].describe())





## max quantity sold as per category and sub category

# print(df.groupby(['category','sub_category'])['quantity'].sum())

# sns.catplot(kind='bar', data=df, x= 'sub_category', y='quantity', estimator='sum', hue='category', errorbar=None)
# plt.xticks(rotation=45)
# plt.show()


## max quantity sold as per which ship mode

df.groupby('ship_mode')['quantity'].sum()

# df.groupby('ship_mode')['quantity'].sum().plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()




## reasons for high shipping cost

# df['shipping_cost'].plot(kind='box')
# plt.show()

# print(df.groupby('region')['shipping_cost'].mean())

# print(df.groupby('market2')['shipping_cost'].mean())




# print(pd.crosstab(index=df['region'], columns=df['ship_mode'],normalize='columns')*100)







