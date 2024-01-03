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

## survived Column 0 means dead 1 means survived

# df['Survived'].value_counts().plot(kind='bar')
# plt.show()


# df['Survived'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()

# print(df['Survived'].isnull().sum())


# df['Pclass'].value_counts()


# df['Pclass'].value_counts().plot(kind='bar')
# plt.show()


# print(df['Sex'].value_counts())


# df['Sex'].value_counts().plot(kind='bar')
# plt.show()



# print(df['SibSp'].value_counts())


# df['SibSp'].value_counts().plot(kind='bar')
# plt.show()


# print(df['Parch'].value_counts())


# df['Parch'].value_counts().plot(kind='bar')
# plt.show()

#### Paren chaild and siblings can be mered to from a new column called family_size
#### create a new col called is_alone


# print(df['Embarked'].value_counts())


# df['Embarked'].value_counts().plot(kind='bar')
# plt.show()


### conclusion for mixed column need to do feature engineering 



### bivariate analysis

# print(pd.crosstab(df['Survived'], df['Pclass']))    ## cross tabulation or contingency table

# print(pd.crosstab(df['Survived'], df['Pclass'], normalize='columns')*100)     ## changing to percentage 



#print(pd.crosstab(df['Survived'], df['Sex'], normalize='columns')*100)    ## between survived and sex


# print(pd.crosstab(df['Survived'], df['Embarked'], normalize='columns')*100) 


print(pd.crosstab(df['Pclass'], df['Embarked'], normalize='columns')*100) 

