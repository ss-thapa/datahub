import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_column', None)




product_category_name_translation = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/product_category_name_translation.csv')
olist_sellers_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_sellers_dataset.csv')
olist_products_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_products_dataset.csv')
olist_orders_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_orders_dataset.csv')
olist_order_reviews_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_order_reviews_dataset.csv')
olist_order_items_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_order_items_dataset.csv')
olist_geolocation_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_geolocation_dataset.csv')
olist_customers_dataset = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/brazil_online data_set/olist_customers_dataset.csv')



## all orders after 2017 

olist_orders_dataset['order_purchase_timestamp'] = pd.to_datetime(olist_orders_dataset['order_purchase_timestamp'])

# orders_after_2017 = olist_orders_dataset[olist_orders_dataset['order_purchase_timestamp'].dt.year > 2017]


## customers who have ordered most in 2017 and after years

# merged_data = olist_orders_dataset.merge(olist_customers_dataset, on='customer_id')

# merged_data[merged_data['order_purchase_timestamp'].dt.year >= 2017].groupby(['customer_unique_id','customer_city','customer_state'])['customer_unique_id'].count().sort_values(ascending=False).head(10)


### which category is sold most in 2018

# merged_data_set = olist_orders_dataset.merge(olist_order_items_dataset, on='order_id').merge(olist_products_dataset, on='product_id')

# merged_data_set[merged_data_set['order_purchase_timestamp'].dt.year == 2018].groupby('product_category_name')['product_category_name'].count().sort_values(ascending=False).head(5)



## sales of 2018 ad plotting the valeus according to the category

# merged_data_set = olist_orders_dataset.merge(olist_order_items_dataset, on='order_id').merge(olist_products_dataset, on='product_id')

# fina_data = merged_data_set[merged_data_set['order_purchase_timestamp'].dt.year == 2018].groupby('product_category_name').agg(total_count=('product_category_name', 'count'))
# sorted_df = fina_data.sort_values(by='total_count', ascending=False).head(5)
# sns.catplot(data=sorted_df, x='product_category_name', y='total_count', kind='bar', height=7)
# plt.show()





