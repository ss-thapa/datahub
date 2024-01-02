import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
pd.set_option('display.max_column', None)


df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/online_retail.csv')


##What does the distribution of the quantity sold look like?
df['Description'].value_counts().head(10)

##Which are the top-selling products?

# top_10_products = df.groupby('Description').agg(total_sum=('Quantity', 'sum')).sort_values(ascending=False, by='total_sum').head(10)
# sns.catplot(kind='bar', data=top_10_products, y='Description', x='total_sum', height=7)
# plt.show()

##How is the unit price distributed?

# sns.displot(x='UnitPrice', data=df, bins=50, kde=True, kind='hist')
# plt.xticks(rotation=90)
# plt.show()

##What is the revenue trend over time?

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['total_cost'] = df['Quantity'] * df['UnitPrice']


# df['months'] = df['InvoiceDate'].dt.month_name()

# monthly_revenue = df.groupby('months').agg(monthly_sum=('total_cost','sum'))

# print(monthly_revenue)
# sns.relplot(kind='line', x='months', y='monthly_sum', data=monthly_revenue)
# plt.show()


# monthly_revenue = df.resample('M', on='InvoiceDate')['total_cost'].sum()
# print(monthly_revenue)

##Which countries contribute the most to sales?
# Top_10_country = df.groupby('Country').agg(total_revenue=('total_cost', 'sum')).sort_values(by='total_revenue', ascending=False).head(10)

# sns.catplot(kind='bar', data=Top_10_country, x='Country', y='total_revenue', color='purple')
# plt.show()



## What is the distribution of the total cost of transactions?

# sns.histplot(x='total_cost', data=df, bins=50)
# plt.show()



### How does the quantity sold vary for different product categories (StockCode)?

# top_10_by_stock = df.groupby('StockCode').agg(total_sum = ('Quantity', 'sum')).sort_values(by='total_sum', ascending=False).head(10)

# sns.catplot(kind='bar', x='StockCode', y='total_sum', data=top_10_by_stock)
# plt.xticks(rotation=90)
# plt.show()




## How is the distribution of transactions across different days of the week?


# df['day_name']=df['InvoiceDate'].dt.day_name()

# sns.catplot(kind='count', x= 'day_name', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='plasma')
# plt.xticks(rotation=45)
# plt.show()



#What is the correlation between quantity, unit price, and total cost?

# correletaion = df[['Quantity','UnitPrice','total_cost']].corr()

# sns.heatmap(data=correletaion, annot=True, fmt='.2f')
# plt.show()



## What is the distribution of transactions over time?

# df.resample('D', on='InvoiceDate')['InvoiceNo'].count().plot()
# plt.show()


# sun=df.groupby(df['InvoiceDate'].dt.day).agg(total_count=('InvoiceNo', 'count'))
# sns.relplot(kind='line', x='InvoiceDate', y='total_count',data=sun)
# plt.show()



## What is the average quantity of products sold in each country?


# average_product_country = df.groupby('Country').agg(average=('Quantity', 'mean'))
# sns.catplot(kind='bar', data=average_product_country, x='Country', y='average', color='seagreen')
# plt.xticks(rotation=90)
# plt.show()


## How does the distribution of unit price vary for different countries?

# sns.catplot(x='Country', y='UnitPrice', data=df, showfliers=False, kind='box')
# plt.xticks(rotation=90)
# plt.show()


# sns.catplot(x='Country', y='UnitPrice', data=df, kind='bar', errorbar=None)
# plt.xticks(rotation=90)
# plt.show()



### What is the monthly distribution of sales for the top 5 countries?


# df.resample('m', on='InvoiceDate')['total_cost'].sum().sort


# print(df.groupby(['months', 'Country'])['total_cost'].sum().sort_values(ascending=False).head(5))




## Filter data for top 5 countries
# top_countries = df.groupby('Country')['total_cost'].sum().sort_values(ascending=False).head(5).index

# df_top_countries = df[df['Country'].isin(top_countries)]

# monthly_distribution_top_countries = df_top_countries.groupby(['Country', df_top_countries['InvoiceDate'].dt.to_period("M")])['total_cost'].sum().unstack()




## What is the distribution of the number of unique products per transaction?


# unique_products_per_transaction = df.groupby('InvoiceNo')['Description'].nunique()

# sns.displot(kind='hist',data=unique_products_per_transaction, bins = 30, kde=True)
# plt.show()



#How is the average unit price changing over time?

# avg_unit_price_over_time = df.groupby(df['InvoiceDate'].dt.to_period("M"))['UnitPrice'].mean()

# print(avg_unit_price_over_time)



## how the average unit price of the most selling object changes over time
# df['StockCode'].value_counts().head(1)

# most_selling_stock = df[df['StockCode'] == '85123A']

# avg_unit_price_over_time = most_selling_stock.groupby(most_selling_stock['InvoiceDate'].dt.to_period("M"))['UnitPrice'].mean()

# avg_unit_price_over_time.plot(kind='line',marker='o')
# plt.show()




##Which are the top customers in terms of total spending?

# top_cust = df.groupby('CustomerID').agg(total_sum=('total_cost','sum')).sort_values(by='total_sum',ascending=False).head(10)

# sns.catplot(kind='bar', x='CustomerID', y='total_sum', data=top_cust)
# plt.xticks(rotation=45)
# plt.show()



## How does the distribution of quantities sold vary between weekdays and weekends?

# def extract(x):
#     if x >= 5:
#         return 'Weekend'
#     else:
#         return 'Weekday'

# df['DayType'] = df['InvoiceDate'].dt.dayofweek.apply(extract)


# sns.catplot(data=df, kind='bar', x='DayType', y='Quantity', errorbar=None)
# plt.show()

# sns.catplot(data=df, kind='box', x='DayType', y='Quantity', showfliers=False)
# plt.show()


## What is the average unit price for each country?

# average_unit_price = df.groupby('Country').agg(avg_price=('UnitPrice', 'mean'))

# sns.catplot(kind='bar',x='Country', y='avg_price', data=average_unit_price)
# plt.xticks(rotation=90)
# plt.show()



## How are the top 5 product categories distributed across different countries?

# top_categories = df.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(5).index

# df_top_catagories = df[df['StockCode'].isin(top_categories)]


# sns.catplot(kind='count', x='Country', data=df_top_catagories, hue='StockCode')
# plt.xticks(rotation=90)
# plt.show()


## What is the relationship between quantity and total cost?

# sns.relplot(kind='scatter', data=df, x='Quantity', y='total_cost')
# plt.show()



## What is the distribution of the number of transactions per customer?

# number_of_cust_per_transcation = df.groupby('CustomerID')['InvoiceNo'].nunique()

# sns.displot(kind='hist', data=number_of_cust_per_transcation, bins=30, kde=True, color='salmon')
# plt.show()




## How does the average unit price vary for different product descriptions?

# all_product_discription = df.groupby('Description').agg(average_value=('UnitPrice', 'mean')).sort_values(by='average_value', ascending=False).head(10)

# sns.catplot(kind='bar', data=all_product_discription, x='Description', y='average_value')
# plt.xticks(rotation = 90)
# plt.show()


## What is the distribution of transaction quantities for the top 5 countries?


# top_5_countries = df['Country'].value_counts().head(5).index

# df_top_5_countries = df[df['Country'].isin(top_5_countries)]

# df_top_5_countries.groupby('Country').agg(total_count=('InvoiceNo', 'count')).sort_values(by='total_count', ascending=False)


## What is the average total cost per transaction for each country?

# average_total_cost = df.groupby('Country').agg(total_average=('total_cost', 'mean')).sort_values(by='total_average', ascending=False)

# sns.catplot(kind='bar', x='Country', y='total_average', data=average_total_cost)
# plt.xticks(rotation=90)
# plt.show()



## What is the hourly distribution of transactions during the day?

# df['hour_of_day'] = df['InvoiceDate'].dt.hour

# sns.catplot(kind='count', x='hour_of_day',data=df)
# plt.show()


## What is the distribution of the quantity of products sold for the top 10 products?

# top_10_products = df.groupby('Description').agg(tota_sum=('Quantity', 'sum')).sort_values(by='tota_sum',ascending=False).head(10)

# sns.catplot(kind='bar', x='Description', y='tota_sum', data=top_10_products)
# plt.xticks(rotation=90)
# plt.show()


##How does the unit price vary across different months?

# df['month'] = df['InvoiceDate'].dt.to_period('M')


# sns.catplot(kind='bar', x='month', y='UnitPrice', data=df, errorbar=None)
# plt.xticks(rotation=45)
# plt.show()



## What is the distribution of transaction quantities for the top 5 product categories?


# top_categories_quantity = df.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(5).index

# df_top_categories_quantity = df[df['StockCode'].isin(top_categories_quantity)]

# sns.catplot(kind='box', x='StockCode', y='Quantity', data=df_top_categories_quantity, showfliers=False)
# plt.xticks(rotation=45)
# plt.show()


## What is the trend of total sales for each product category over time?

# df['month'] = df['InvoiceDate'].dt.to_period("M")

# total_sales_by_category = df.groupby(['StockCode', 'month'])['total_cost'].sum().unstack()


## How does the distribution of unit price vary for different days of the week?

# plt.figure(figsize=(12, 6))
# sns.boxplot(x='DayOfWeek', y='UnitPrice', data=df, showfliers=False, palette='coolwarm')
# plt.title('Distribution of Unit Price Across Days of the Week')
# plt.xlabel('Day of the Week')
# plt.ylabel('Unit Price')
# plt.show()



