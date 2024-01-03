import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_column', None)



df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/titanic/train.csv')
# df_test = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/titanic/test.csv')


### Performing thhe univariate analysis on the age column

# df['Age'].describe()

#print(df.isnull().sum()/ len(df['Age']))     ## this thows the percentage of null values in each column

# df['Age'].plot(kind='hist')
# plt.show()

# df['Age'].plot(kind='kde')
# plt.show()

# print(df['Age'].skew())

# df['Age'].plot(kind='box')
# plt.show()


# print(df[df['Age'] > 65])    ## checking the outliers datas as shown in the box plot


### Conclusion : Age is normally(almost) disrributed , 20% of the values are missing , There are some outliers .



### performing univariate analysis on fare

# print(df['Fare'].describe())

# df['Fare'].plot(kind='hist')
# plt.show()

# df['Fare'].plot(kind='kde')
# plt.show()

# print(df['Fare'].skew())

# df['Fare'].plot(kind='box')
# plt.show()


# print(df[df['Fare'] > 250])

# print(df['Fare'].isna().sum())


### Conclusion : the data is highley (positively) skewed , Fare column actually contains group fare not individual fare this might be an issue
### we need to create a new column called individual fare



### univariate analysis on categorical column 






