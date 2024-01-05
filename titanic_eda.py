import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_column', None)



df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/titanic/train.csv')
df1 = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/titanic/test.csv')


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


# print(pd.crosstab(df['Pclass'], df['Embarked'], normalize='columns')*100) 


## survived and age 

# df[df['Survived'] == 1]['Age'].plot(kind='kde', label = "Survived")

# df[df['Survived'] == 0]['Age'].plot(kind='kde', label = "Not Survived")
# plt.legend()
# plt.show()


### Feature engineering 

df = pd.concat([df, df1])

### creating a new column of individual fare
df['individual_fare'] = df['Fare']/(df['SibSp'] + df['Parch']+1)

# print(df[['individual_fare', 'Fare']].describe())

### creating new column by adding sibsp parch and the individual

df['family_size'] = df['SibSp'] + df['Parch'] + 1

### create a new categorical column called family_type with some condition


def transform_family_size(num):
    if num == 1:
        return 'alone'
    elif num >1 and num < 5:
        return 'small'
    else:
        return 'large'
    
df['family_type'] = df['family_size'].apply(transform_family_size)

### prforming bivariate eda on family_type

# print(pd.crosstab(df['Survived'], df['family_type'], normalize='columns')*100)

### working with name column

df['surname']=df['Name'].str.split(',').str.get(0)

df['title']=df['Name'].str.split(',').str.get(1).str.strip().str.split(' ').str.get(0)

# print(df['title'].value_counts())

df['title'] = df['title'].str.replace('Rev.', 'other')
df['title'] = df['title'].str.replace('Dr.', 'other')
df['title'] = df['title'].str.replace('Col.', 'other')
df['title'] = df['title'].str.replace('Jonkheer.', 'other')
df['title'] = df['title'].str.replace('Major.', 'other')
df['title'] = df['title'].str.replace('Capt.', 'other')
df['title'] = df['title'].str.replace('the', 'other')
df['title'] = df['title'].str.replace('Don.', 'other')


# print(df['title'].value_counts())

temp_df=df[df['title'].isin(['Mr.','Miss.','Mrs.','Master.','ootherr'])]
pd.crosstab(temp_df['Survived'], temp_df['title'], normalize='columns')*100


### working with cabin column

df['Cabin'].isna().sum()/len(df['Cabin'])     ### 77 percent of data is missing in this column


df['Cabin'].fillna('M', inplace=True)

df['deck'] = df['Cabin'].str[0]

# print(pd.crosstab(df['deck'], df['Pclass']))

pd.crosstab(df['deck'], df['Survived'], normalize='columns')


