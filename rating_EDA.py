import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
pd.set_option('display.max_column', None)



df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/cuisine_rating.csv')



df = df.rename(columns=({'User ID': 'user_id', 'Area code':'area_code', 'Location':'location', 'Gender':'gender', 'YOB':'yob', 'Marital Status':'marital_status',
       'Activity':'activity', 'Budget':'budget', 'Cuisines':'cuisines', 'Alcohol ':'alcohol', 'Smoker':'smoker', 'Food Rating':'food_rating',
       'Service Rating':'service_rating', 'Overall Rating':'overall_rating', 'Often A S':'frequent'}))


### univariate analysis on categorical columns
##location

df['location'].describe()

# df['location'].value_counts().plot(kind='bar')
# plt.show()

# df['location'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()

## Gender

df['gender'].value_counts()


# df['gender'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()

## Year of birth

df['yob'].value_counts()

def get_decade(year):
    return str(year // 10 * 10) + "s"

# Apply the function to create a new 'decade' column
df['decade'] = df['yob'].apply(get_decade)

df['decade'].describe()

# df['decade'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()

## import datetime 
current_year = datetime.now().year

## Create a new 'age' column by subtracting 'yob' from the current year

df['age'] = current_year - df['yob']

## created new column of decade information
def get_decade_age(age):
    return str(age // 10 * 10) + "s"

df['decade_age']=df['age'].apply(get_decade_age)

df['decade_age'].value_counts()


## maritial status

df['marital_status'].describe()

df['marital_status'].value_counts()

# df['marital_status'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()


## Activity 

df['activity'].describe()

df['activity'].value_counts()

# df['activity'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show() 


## budget

df['budget'].describe()

# df['budget'].plot(kind='hist')
# plt.show()


# df['budget'].plot(kind='box')
# plt.show()


## cusinies

df['cuisines'].value_counts()

df['cuisines'].describe()

# df['cuisines'].value_counts().plot(kind='pie', autopct='%0.1f%%')
# plt.show()

## alcohol
df['alcohol'].value_counts()

df['alcohol'].describe()

# df['alcohol'].value_counts().plot(kind='pie', autopct = '%0.1f%%')
# plt.show()


## smoker

df['smoker'].value_counts()

df['smoker'].describe()

# df['smoker'].value_counts().plot(kind='pie', autopct = '%0.1f%%')
# plt.show()



## food rating 

df['food_rating'].describe()

# df['food_rating'].plot(kind='hist')
# plt.show()

# df['food_rating'].plot(kind='kde')
# plt.show()


## sevice rating


df['service_rating'].describe()

# df['service_rating'].plot(kind='hist')
# plt.show()

# df['service_rating'].plot(kind='kde')
# plt.show()


## overall rating 

df['overall_rating'].describe()

# df['overall_rating'].plot(kind='hist')
# plt.show()

# df['overall_rating'].plot(kind='kde')
# plt.show()


## age 

df['age'].describe()

# df['age'].plot(kind='kde')
# plt.show()


### bivariate analysis with respect of overall rating

## ratings vs location

print(pd.crosstab(df['overall_rating'], df['location'], normalize='columns')*100)


# print(df[df['location'] == 'Market City, MY'])
