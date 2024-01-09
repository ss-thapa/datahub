import seaborn as sns 
import pandas as pd
import datetime as dt 
pd.set_option('display.max_column', None)

df = sns.load_dataset('taxis')


df['pickup'].dt.day_name()

df['pickup'].max()-df['pickup'].min()



df[df['pickup'].dt.month == 3]['fare'].max()


# print(df['fare'].resample('M').max())


df['year'] = pd.to_datetime(df['pickup'].dt.is_month_end)

df['year'].head()


### time stamp

dates = ['2019/12/22', '2019/12/23','2019/12/24']

pd.to_datetime(dates)

print(dates)


