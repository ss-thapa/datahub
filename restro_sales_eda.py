import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_column', None)




orders = pd.read_excel('/Users/sunilthapa/Desktop/programming/datahub/datas/restaurant_orders/Orders.xlsx')

restaurants = pd.read_excel('/Users/sunilthapa/Desktop/programming/datahub/datas/restaurant_orders/Restaurants.xlsx')

orders = orders.rename(columns={'Order ID': 'order_id', 'Customer Name':'customer_name', 'Restaurant ID':'restaurant_id','Order Date':'order_date',
       'Quantity of Items':'quantity_of_items', 'Order Amount':'order_amount', 'Payment Mode':'payment_mode',
       'Delivery Time Taken (mins)':'delivery_time_taken', 'Customer Rating-Food':'customer_rating_food',
       'Customer Rating-Delivery':'customer_rating_delivery'})

restaurants = restaurants.rename(columns={'RestaurantID':'restaurant_id', 'RestaurantName':'restaurant_name', 'Cuisine':'cuisine', 'Zone':'zone', 'Category':'category'})
print(restaurants.columns)

df =orders.merge(restaurants, on='restaurant_id')


### univariate analysis 

## quantity_of items

orders['quantity_of_items'].describe()

## order amount 

orders['amount_per_item'] = round(orders['order_amount'] / orders['quantity_of_items'], 2)

## payment mode

orders['payment_mode'].value_counts()

## delivery taken time

orders['delivery_time_taken'].describe()


orders['delivery_time_taken'].skew()

# orders['delivery_time_taken'].plot(kind='box')
# plt.show()



## customer_rating_food

orders['customer_rating_food'].skew()

orders['customer_rating_food'].describe()

# orders['delivery_time_taken'].plot(kind='box')
# plt.show()


## customer_rating_delivery

orders['customer_rating_delivery'].describe()

orders['customer_rating_delivery'].skew()

# orders['customer_rating_delivery'].plot(kind='box')
# plt.show()


# Which restaurant received the most orders?

df.groupby('restaurant_name')['order_id'].count().sort_values(ascending=False)


# which restaurant did the most sales in terms of total revenue 

df.groupby('restaurant_name')['order_amount'].sum().sort_values(ascending=False)

# which restro did the best sales as per items

df.groupby('restaurant_name')['quantity_of_items'].sum().sort_values(ascending=False)

# Which customer ordered the most?

orders.groupby('customer_name')['order_id'].count().sort_values(ascending=False)

# When do customers order more in a day?

orders['time_of_day'] = pd.to_datetime(orders['order_date']).dt.strftime('%I:%M %p')

orders['time_of_day'].value_counts()

pd.to_datetime(orders['order_date']).dt.strftime('%I:%M %p').value_counts()


# orders['time_of_day'].value_counts().plot(kind='barh')
# plt.show()


# Which is the most liked cuisine as per sales

df.groupby('cuisine')['order_id'].count().sort_values(ascending=False)


# which is the most liked as per food ratings


top_rated =df[df['customer_rating_food'] == 5]

# top_rated['cuisine'].value_counts().plot(kind='bar')
# plt.show()

# which 5 restaurant have taken less time to deliver then average delivery time 

df[df['delivery_time_taken'] < (df['delivery_time_taken'].mean())].groupby('restaurant_name')['order_id'].count().sort_values(ascending=False).head(5)

# df[df['delivery_time_taken'] < (df['delivery_time_taken'].mean())].groupby('restaurant_name')['order_id'].count().sort_values(ascending=False).head(5).plot(kind='bar')
# plt.xticks(rotation= 45)
# plt.show()



# how many times did any restro took max delivery time to deliver food 

df[df['delivery_time_taken'] == (df['delivery_time_taken'].max())]['restaurant_name'].value_counts()

# Which zone has the most sales?

# df.groupby('zone')['order_id'].count().plot(kind='bar')
# plt.xticks(rotation = 45)
# plt.show()



## Cross tab function


#print(pd.crosstab(index=df['cuisine'], colnames=df['payment_mode']))      ## this gives frequency by default

#print(pd.crosstab(index=df['cuisine'], columns=df['payment_mode'], values=df['order_amount'], aggfunc='sum'))     # this gives sum of sale according to the payment mode and cusinnes 

#print(pd.crosstab(index=df['cuisine'], columns=df['payment_mode'], rownames=['cuisine_name'],colnames=['payment_done_by']))     # this changes the name of the row and column

#print(pd.crosstab(index=df['cuisine'], columns=[df['payment_mode'], df['zone']]))    # adding three columns

#print(pd.crosstab(index=df['cuisine'], columns=df['payment_mode'],margins=True, normalize='index' )*100)  # normalize according to the column or index or overall 









