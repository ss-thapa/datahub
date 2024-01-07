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

orders.merge(restaurants, on='restaurant_id')



