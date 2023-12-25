import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_column', None)


df_zomato = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/Zomatodataset/zomato.csv',encoding='latin-1')



# x = [features for features in df.columns if df[features].isna().sum() > 0]     ## this returns the list of column name which have at least one empty value

# sns.heatmap(df.isna(), yticklabels=False,cbar=False,cmap='viridis')
# plt.show()

df_countrycode = pd.read_excel('/Users/sunilthapa/Desktop/programming/datahub/datas/Zomatodataset/country_code.xlsx')


final_df = pd.merge(df_zomato,df_countrycode, on='Country Code', how='left')



final_df = final_df.rename(columns= {'Restaurant ID': 'restaurant_id', 'Restaurant Name':'restaurant_name', 'Country Code':'country_code', 'City':'city', 'Address':'address',
       'Locality':'locality', 'Locality Verbose':'locality_v', 'Longitude':'longitude', 'Latitude':'latitude', 'Cuisines':'cuisines',
       'Average Cost for two':'average_cost_for_two', 'Currency':'currency', 'Has Table booking':'has_table_booking',
       'Has Online delivery':'has_online_delivery', 'Is delivering now':'is_delivery_now', 'Switch to order menu':'switch_to_order_menu',
       'Price range':'price_range', 'Aggregate rating':'aggregate_rating', 'Rating color':'rating_color', 'Rating text':'rating_text',
       'Votes':'votes', 'Country':'country'})



# # country_names = final_df.country.value_counts().index

# # country_values = final_df.country.value_counts().values

# # #zomato top 5 countries maximum records
# # plt.pie(x=country_values[:5],labels=country_names[:5], autopct='%1.2f%%', radius=1.8)
# # plt.show()

ratings = final_df.groupby(['aggregate_rating', 'rating_color', 'rating_text']).size().reset_index().rename(columns={0:'rating_count'})

## observe the rating df by barplot

# plt.figure(figsize=(12,5))
# sns.barplot(x='aggregate_rating', y='rating_count', data=ratings, hue='rating_color')
# plt.show()


##observe the rating df by countplot

# sns.countplot(x='rating_color', data=ratings)
# plt.show()


##countries who have given the zero rating and their count

result3 = final_df[final_df['aggregate_rating'] == 0].groupby('country').size().reset_index(name='countof')

##finding out which currency is used by which country

result4 = final_df.loc[final_df['country'].notnull(), ['country', 'currency']].drop_duplicates().sort_values('country').reset_index(drop=True)

#using group by function both of them gives same result

result5 = final_df[['country', 'currency']].groupby(['country', 'currency']).size().reset_index().sort_values('country')


##which countries do have online deliveries option

result6 = final_df[final_df['has_online_delivery'] == "Yes"].country.value_counts()


##create a pie chart for cities distribution

# city_values = final_df.city.value_counts().values

# city_names = final_df.city.value_counts().index 

# plt.pie(x = city_values[:5], labels=city_names[:5],radius=1.4)
# plt.show()


