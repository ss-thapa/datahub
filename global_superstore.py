import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_column', None)





df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/superstore.csv')

df=df.drop(columns=['记录数', 'Market'], axis=1)

df=df.rename(columns={'Category':'category', 'City':'city', 'Country':'country', 'Customer.ID':'customer_id', 'Customer.Name':'customer_name',
       'Discount':'discount','Order.Date':'order_date', 'Order.ID':'order_id', 'Order.Priority':'order_priority',
       'Product.ID':'product_id', 'Product.Name':'product_name', 'Profit':'profit', 'Quantity':'quantity', 'Region':'region', 'Row.ID':'row_id',
       'Sales':'total_sales_amount', 'Segment':'segment', 'Ship.Date':'ship_date', 'Ship.Mode':'ship_mode', 'Shipping.Cost':'shipping_cost', 'State':'state',
       'Sub.Category':'sub_category', 'Year':'year', 'Market2':'market2'})

df['order_date'] =pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
# df['year'] = pd.to_datetime(df['year'])



categorical_columns = ['category', 'city', 'country', 'order_priority', 'region', 'segment', 'ship_mode', 'state', 'sub_category', 'market2']

for column in categorical_columns:
    df[column].value_counts()



numerical_columns = ['dicount', 'profit', 'quantity', 'sales', ]

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


df['order_priority'].value_counts().head(5).plot(kind='bar')
plt.xticks(rotation = 45)
plt.show()
