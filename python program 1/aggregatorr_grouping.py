import pandas as pd
import numpy as np
import seaborn as sns
pd.set_option('display.max_column', None)


# df = sns.load_dataset('tips')

# print(df.groupby('time')['total_bill'].mean())


### to_frame, naming the aagrigator column 

# average_bill = df.groupby('time')['total_bill'].mean().to_frame('avg_bill').reset_index().sort_values(by='avg_bill',ascending=False)


# print(df.groupby('time')['total_bill'].count())

# print(df.groupby('time')['total_bill'].nunique())

# print(df.groupby('time')['total_bill'].median())

# print(df.groupby('day')['tip'].mean())

# print(df.groupby('sex')['tip'].max())

# print(df.groupby('day')['tip'].quantile(0.9))



# print(df.groupby('time')['total_bill'].agg(['min', 'max', np.median]).rename(columns={'min': 'minimum', 'max':'maximum'}))


# print(df.groupby('time')['total_bill'].describe())


# print(df.groupby(['time', 'day'])[['total_bill', 'total_bill']].mean())



# print(df.groupby(['time', 'day'])[['tip', 'total_bill']].mean())


# print(df.groupby(['time', 'day'])[['tip', 'total_bill']].mean().reset_index())



## transform

# dttransform = sns.load_dataset('tips')

# dttransform['median_bill'] = df.groupby('time')['total_bill'].transform('median')

# print(dttransform.loc[df['time'] == 'Lunch'])

# print(dttransform.loc[dttransform['total_bill'] > dttransform['median_bill']])



### function


# dttransform['zscore'] = df.groupby('time')['total_bill'].transform(lambda x: (x - x.mean()) / x.std() )

# print(dttransform.groupby('time').apply(lambda x: (x['tip']/x['total_bill']).mean()).round(3).to_frame('average_tip_per').reset_index())




df = sns.load_dataset('taxis')


# print(df.groupby(df['pickup'].dt.month)['distance'].mean())


# print(df.nlargest(n=10, columns='total').loc[:,['pickup_zone', 'total']].reset_index(drop=True))



top_10 = df.nlargest(n=10, columns='total').loc[:,['payment', 'total']]

# print(df.groupby('payment')['total'].max())




