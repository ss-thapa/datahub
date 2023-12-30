import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
pd.set_option('display.max_column', None)




df = px.data.gapminder()




country_4 = df[df['country'].isin(['Nepal', 'Panama', 'Poland', 'Puerto Rico'])]

african_conti = df[df['continent'] == 'Africa']

# sns.relplot(data=country_4, x='year', y='gdpPercap', kind='line',hue='country', col='continent')

# plt.show()

# print(df[['year', 'lifeExp', 'pop', 'gdpPercap', ]].corr())


# sns.relplot(data=df, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=4)
# plt.show()


##Histogram

# sns.displot(data=df, x='lifeExp', kind='hist', bins = 10)
# plt.show()


# sns.displot(data=df, x='lifeExp', kind='hist', col='continent', col_wrap=3)
# plt.show()



# sns.displot(data=african_conti, x='lifeExp', kind='kde')
# plt.show()

# sns.displot(data=df, x='lifeExp', kind='kde')
# plt.show()


# sns.displot(data=df, x='gdpPercap', kind='kde')
# plt.show()



# sns.catplot(data=country_4, x= 'country', y='lifeExp', kind='strip')
# plt.show()





# sns.catplot(data=df, x='continent', y='gdpPercap', kind='bar', errorbar=None)
# plt.show()


# sns.catplot(data=df, x='continent', y='gdpPercap', kind='point', errorbar=None)
# plt.show()



