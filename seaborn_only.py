import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
pd.set_option('display.max_column', None)


df_tips = sns.load_dataset('tips')

df_iris = sns.load_dataset('iris')

### Relational figures
## axis level

# sns.scatterplot(data=df, x='total_bill', y='tip')
# plt.show()


## figure level
# sns.relplot(data=df, x='total_bill', y='tip', kind='scatter', hue='sex', style='time', size='size')
# plt.show()



## line plot 

# gap = px.data.gapminder()

# india_only = gap.loc[gap['country']== 'India']
# nepal_only = gap.loc[gap['country']== 'Nepal']
# chin_only = gap.loc[gap['country']== 'China']


# three_country = gap.loc[gap['country'].isin(['Nepal', 'Brazil', 'Germany'])]

# sns.relplot(data=three_country, x='year', y='lifeExp', kind='line', hue='country', style='continent' )
# plt.show()

 

#facit plot

# sns.relplot(data=df, x='total_bill', y='tip', kind='scatter', row='day', col='sex')
# plt.show()

# wrap in facip plot
# sns.relplot(data=df, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=4)
# plt.show()



###Distribution Types of plotting
## histogram figure level

# sns.displot(data=df, x='total_bill', kind='hist',bins=20)
# plt.show()

## histogram axis level

# sns.histplot(data=df, x='total_bill', bins=20)
# plt.show()

## histogram with catagorical datas acts like a count plot of that data
# sns.displot(data=df, x='day', kind='hist')
# plt.show()

# df_titanic = sns.load_dataset('titanic')

# sns.displot(data=df_titanic, x='age', kind='hist', element = 'step', col='sex')
# plt.show()


## KDE Plot

# sns.displot(data=df, x='total_bill', kind='kde')
# plt.show()

# sns.displot(data=df, x='total_bill', kind='kde', hue='sex')
# plt.show()


#Bivariate histogram  2 column histogeam 

# sns.displot(data=df, x='total_bill', y='tip', kind='hist' )
# plt.show()


# biveriate kde plot

# sns.displot(data=df, x='total_bill', y='tip', kind='kde' )
# plt.show()




## Heat map

# pivited =gap.pivot(index='country', columns='year', values='lifeExp')

# europe_only = gap[gap['continent']== 'Europe'].pivot(index='country', columns='year', values='lifeExp')

# plt.figure(figsize=(15,10))
# sns.heatmap(europe_only, annot=True,cmap='summer')
# plt.show()



#Cluster map


# df2 = px.data.iris()


# sns.clustermap(df2.iloc[:, [0,1,2,3]])
# plt.show()




### categorical Plots
##categorical scatter plots
##strip plot:

#axis level
# sns.stripplot(data=df_tips, x='day', y='total_bill')
# plt.show()


#fig level
# sns.catplot(data=df_tips, x = 'day', y='total_bill', kind='strip', jitter= False)
# plt.show()

##swarm plot

# sns.catplot(data=df_tips, x='day', y='total_bill', kind='swarm')
# plt.show()


## Box plot
## axis level

# sns.boxplot(data=df_tips, x= 'day', y='total_bill')
# plt.show()

##fig level
# sns.catplot(data=df_tips, x= 'day', y='total_bill', kind='box', hue='sex')
# plt.show()

# sns.catplot(data=df_tips, y= 'total_bill', kind='box')
# plt.show()


##Violinplot
#fig level
# sns.catplot(data=df_tips, x='day', y='total_bill', kind='violin')
# plt.show()


### Bar plot

# sns.catplot(data=df_tips, x= 'sex', y='total_bill', kind='bar', errorbar=None, estimator='sum')
# plt.show()

##point plot
# sns.catplot(data=df_tips, x= 'sex', y='total_bill', kind='point', errorbar=None)
# plt.show()



##count plot

# sns.catplot(data=df_tips, x = 'sex', kind='count')
# plt.show()


## faciting using catplot

# sns.catplot(data=df_tips, x='sex', y='total_bill', kind='box', col='smoker', row='time')
# plt.show()


### regplot

# sns.regplot(data=df_tips, x='total_bill', y = 'tip')
# plt.show()

### lmplot 

# sns.lmplot(data=df_tips, x='total_bill', y = 'tip')
# plt.show()


### resid plot

# sns.residplot(data=df_tips, x='total_bill', y='tip')
# plt.show()



# sns.catplot(data=df_tips, x='sex', y='total_bill', kind='bar', col='day', row='time', errorbar=None)
# plt.show()



### facit grid  

# sun = sns.FacetGrid(data=df_tips,col='day',row='time' )

# sun.map(sns.barplot,'sex','total_bill')
# plt.show()






### pair plot


# sns.pairplot(df_iris, kind='scatter')
# plt.show()




### pair grid 

# g=sns.PairGrid(data=df_iris)
# g.map(sns.scatterplot)
# plt.show()


# g = sns.PairGrid(data=df_iris, hue='summer')
# g.map_diag(sns.histplot)
# g.map_offdiag(sns.scatterplot)
# plt.show()


# g = sns.PairGrid(data=df_iris, hue='species')
# g.map_diag(sns.histplot)
# g.map_offdiag(sns.scatterplot)
# g.add_legend()
# plt.show()



# g = sns.PairGrid(data=df_iris, hue='species')
# g.map_diag(sns.histplot)
# g.map_upper(sns.kdeplot)
# g.map_lower(sns.scatterplot)
# g.add_legend()
# plt.show()







