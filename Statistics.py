import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import seaborn as sns
from sklearn.neighbors import KernelDensity 

## for 1 dice roll

# sun=[]
# for i in  range(10000):
#     sun.append(random.randint(1,6))
    


# moon = (pd.Series(sun).value_counts()/ pd.Series(sun).value_counts().sum()).sort_index()

# moon.plot(kind='bar')
# plt.show()




## for 2 dice roll

# sun=[]
# for i in  range(10000):
#     a =random.randint(1,6)
#     b =random.randint(1,6)

#     sun.append(a + b)
    


# moon = (pd.Series(sun).value_counts()/ pd.Series(sun).value_counts().sum()).sort_index()

# moon.plot(kind='bar')
# plt.show()




## CDF of PMF of 2 roll dice

# sun=[]
# for i in  range(10000):
#     a =random.randint(1,6)
#     b =random.randint(1,6)

#     sun.append(a + b)
    


# moon = (pd.Series(sun).value_counts()/ pd.Series(sun).value_counts().sum()).sort_index()

# moon=np.cumsum(moon)

# moon.plot(kind='bar')
# plt.show()




## PDF, Density estimation , Parametric density estimation , assuming normal distribution


# sample = normal(loc=50, scale=5, size=1000)     ## loc is mean and scale is distribution

# ## Plot histogram to understand the distribution of data

# # plt.hist(sample, bins=10)
# # plt.show()

# ## calculate sample mean and sample std dev

# sample_mean = sample.mean()
# sample_std = sample.std()

# ## fitting the distribution with the above parameters

# dist = norm(sample_mean, sample_std)


# values = np.linspace(sample.min(), sample.max(), 100)     ## generating 100 data points between min and max values of my datasets

# probability_density = [dist.pdf(value) for value in values]

# ## plot the histogram and pdf 

# plt.hist(sample, bins=10, density=True)
# plt.plot(values, probability_density)
# plt.show()

# sns.distplot(sample)
# plt.show()



### KDE

sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = np.hstack((sample1, sample2))

# plt.hist(sample, bins=50)
# plt.show()


model = KernelDensity(bandwidth=3, kernel='gaussian')

# convert data to 2d array
sample = sample.reshape((len(sample), 1))

model.fit(sample)

values = np.linspace(sample.min(), sample.max(), 100)
values = values.reshape((len(values), 1))

probabilities = model.score_samples(values)
probabilities = np.exp(probabilities)

## score_samples(value) returens the log- density estimate of the input samples values. This is because the score_sample() method of the KernalDensity class returns the logarithm of the probability density estimate rather than the actual probability density estimate.

# plt.hist(sample, bins=50, density=True)
# plt.plot(values[:], probabilities)
# plt.show()

# sns.kdeplot(sample.reshape(1000), bw_adjust=1)     ## bw_adjust is bandwidth adjustment
# plt.show()




## iris data set PDF

df = sns.load_dataset('iris')

# fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# Plot KDE plots for each variable in different subplots
# sns.kdeplot(data=df, x='sepal_length', hue='species', ax=axes[0, 0])
# sns.kdeplot(data=df, x='sepal_width', hue='species', ax=axes[0, 1])
# sns.kdeplot(data=df, x='petal_length', hue='species', ax=axes[1, 0])
# sns.kdeplot(data=df, x='petal_width', hue='species', ax=axes[1, 1])

# plt.tight_layout()
# plt.show()  

## conclusion is petal_width and petal_length columns can be used in machine learning model



## titanic

# df1 = sns.load_dataset('titanic')

# sns.kdeplot(data=df1, x='age', hue='survived')
# plt.show()


## CDF


# sns.kdeplot(data=df, x='petal_width', hue='species')
# sns.ecdfplot(data=df, x='petal_width', hue='species')
# plt.show()




