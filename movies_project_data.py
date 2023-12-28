import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure
pd.set_option('display.max_column', None)
# %matplotlib inline
# plt.matplotlib.rcParams[figure.figsize]= (12,8)


df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/movies.csv')


#### DATA CLEANING




# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull())
#     print('{} - {}%'.format(col, pct_missing))

df = df.dropna()


df['budget']=df['budget'].astype('int64')
df['gross']=df['gross'].astype('int64')


# df['year_correct'] = df['released'].astype(str).str[10:14]

# print(df['year_correct'])



df['yearcorrect'] = df['released'].astype(str).str.split().str[2]


df = df.sort_values(by=['gross'], inplace=False, ascending=False)


# print(df.select_dtypes(['float64', 'int64']).corr())

## scatter plot with budget and gross

# plt.scatter(x=df['budget'], y=df['gross'])
# plt.title('Budget vs gross earnings')
# plt.xlabel('Budget')
# plt.ylabel('Gross')
# plt.show()

## plot budget vs gross using seaborn

# sns.regplot(x=df['budget'], y=df['gross'], data=df, scatter_kws={'color':'red'}, line_kws={'color':'blue'})
# plt.show()


### different correlation method

# print(df.select_dtypes(['int64','float64']).corr(method='pearson'))

# print(df.select_dtypes(['int64','float64']).corr(method='kendall'))

# print(df.select_dtypes(['int64','float64']).corr(method=spearman))


### visualize the correlation

# correlation_matrix =df.select_dtypes(['int64','float64']).corr(method='pearson')

# sns.heatmap(correlation_matrix, annot=True)
# plt.show()


## look at company 
## This code goes through all the object data types columns and find the unique datas ad give the unique datas its numeric values

# df_numerized = df

# for col_name in df_numerized.columns:
#     if (df_numerized[col_name].dtypes == 'object'):
#         df_numerized[col_name] = df_numerized[col_name].astype('category')
#         df_numerized[col_name] = df_numerized[col_name].cat.codes


# correlation_matrix = df_numerized.corr(method='pearson')
# sns.heatmap(correlation_matrix, annot=True)
# plt.title('correlation matric for numeric features')
# plt.xlabel('Movie features')
# plt.ylabel('Movie features')
# plt.show()

# correlation_matrix = df_numerized.corr()
# corr_pairs = correlation_matrix.unstack()
# sorted_pairs = corr_pairs.sort_values()
# high_correlation = sorted_pairs[(sorted_pairs) >= 0.5]
# high_correlation








