import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_column', None)

# df = pd.read_csv('https://raw.githubusercontent.com/cajjster/data_files/main/online_sales.csv')

### group by (), value_counts() and countplot are closely related

## all there gives the same same result sns will give it in visulize way

# print(df['Country'].value_counts())
# print(df.groupby('Country')['Country'].count().sort_values(ascending=False))


# ax = sns.countplot(data=df, x='Country', color='Green')
# ax.set_xticklabels(labels=ax.get_xticklabels(), rotation = 45, ha= 'center')
# plt.show()


### group by using any aggregation

# print(df.groupby(['Country'])['Quantity'].sum().sort_values(ascending=False))

# print(df.groupby(['Country'])['UnitPrice'].mean().sort_values(ascending=False))

# print(df.groupby(['Country'])['UnitPrice'].median().sort_values(ascending=False))


### how sns.barplot and groupby() are two sides of same coin

# ax= sns.barplot(data=df, x='Country', y='Quantity', errorbar=None, estimator='median')
# ax.set_xticklabels(labels=ax.get_xticklabels(), rotation = 45, ha= 'center')
# plt.show()


# df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


# print(df.groupby('InvoiceDate')['Quantity'].count())

## to work with datetime datatype



# print(df.groupby(pd.Grouper(key='InvoiceDate', freq='M'))['Quantity'].sum())


### create and you your own function



# def calculate_revenue(x):
#     revenue = (x['Quantity'] * x['UnitPrice']).sum()
#     return revenue


# print(df.groupby('Country').apply(calculate_revenue).sort_values(ascending=False))



### selecting several columns in Groupby

# print(df.groupby('Country')[['Quantity', 'UnitPrice']].median())



### agg() method

# print(df.groupby('Country')[['Quantity', 'UnitPrice']].agg(['mean', 'median', 'count']))

# print(df.groupby('Country')[['Quantity', 'UnitPrice']].agg({'Quantity': ['count', 'mean', 'median'], 'UnitPrice':['mean', 'median', 'sum']}))




### Double groupby and sns.barplot with hue are two sides of same coin

df2 = pd.read_csv('https://raw.githubusercontent.com/cajjster/data_files/main/vending_machine_sales_.csv')



# print(df2.groupby(['Location', 'Category'])[['TransTotal']].sum())

### both gives the same result upper double groupby and sns.barplot
# sns.barplot(data=df2, x= 'Location', y='TransTotal', estimator='sum',errorbar=None, hue='Category')
# plt.show()



### while doing double group by always use unstack for easy reading

# sales = df2.groupby(['Location', 'Category'])[['TransTotal']].sum().unstack()

# sns.heatmap(data=sales, annot=True, fmt='.0f')
# plt.show()

