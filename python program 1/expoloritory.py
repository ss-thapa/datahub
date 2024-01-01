# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.style.use('ggplot')
# pd.set_option('display.max_columns',None)


# df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datasets/coaster_db.csv')

# df2 = df[['coaster_name', 
#     #'Length', 'Speed', 
#        'Location', 'Status',
#         # 'Opening date',
#        #'Type', 
#        'Manufacturer', 
#        #'Height restriction', 'Model', 'Height',
#        #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
#        #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
#        #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
#        #'Track layout', 'Fastrack available', 'Soft opening date.1',
#        #'Closing date', 
#        'Opened', 
#        #'Replaced by', 'Website',
#        #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
#        #'Single rider line available', 'Restraint Style',
#        #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
#        'year_introduced',
#         'latitude', 'longitude', 
#         'Type_Main',
#        'opening_date_clean', 
#        #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
#        'speed_mph', 
#        #'height_value', 'height_unit', 
#        'height_ft',
#        'Inversions_clean', 'Gforce_clean']].copy()

# df2['opening_date_clean'] = pd.to_datetime(df2['opening_date_clean'])   # changing column str to datetype

# df3 = df2.rename(columns={'Location' : 'location', 'Status':'status', 'Manufacturer': 'manufacturer', 'Opened':'opened',  #renaming the columns
#        'Type_Main':'type_main',
#         'Inversions_clean':'inversions',
#        'Gforce_clean':'gforce', 'opening_date_clean': 'opening_date'})

# # print(df3.duplicated(subset='coaster_name'))
# # # print(df3[df3.duplicated()== True])
# # print(df3.query('coaster_name == "Crystal Beach Cyclone"'))
# # print(df3[df3['coaster_name'] == 'Crystal Beach Cyclone'])
# # print(df3['coaster_name'].dtype)
# # print(df3.loc[df3.duplicated(subset='coaster_name')])
# # print(df3.columns)

# df4 = df3.loc[~df3.duplicated(subset=['coaster_name','location', 'opening_date'])]\
#     .reset_index(drop=True) # this line selects and drops all the rows of duplicated values in the rows and assign to mew variable and reset the index no.
                            

# # ax = df4['year_introduced'].value_counts().head(10)\
# #     .plot(kind='bar')
# # ax.set_xlabel('Year Introduced')
# # ax.set_ylabel('Count')
# # ax.set_title('Top Years Coasters Introduced')
# # plt.show()


# # ax = df4['speed_mph'].plot(kind='hist', bins=20)
# # ax.set_title('Coaster Speed (mph)')
# # ax.set_xlabel('speed (mph)')
# # plt.show()


# # ax = df4['speed_mph'].plot(kind='kde')
# # ax.set_title('Coaster Speed (mph)')
# # ax.set_xlabel('speed (mph)')
# # plt.show()



# # ax = df4.plot(kind='scatter', x= 'speed_mph', y='height_ft')
# # ax.set_title('Coaster Speed vs. Height')
# # plt.show()


# # sns.scatterplot(x= 'speed_mph', y='height_ft', data = df4, hue='year_introduced')
# # plt.show()



# # sns.pairplot(data=df4, vars=['year_introduced','speed_mph','height_ft', 'inversions', 'gforce'], hue='type_main')
# # plt.show()



# # df4_corr = df4[['year_introduced','speed_mph','height_ft', 'inversions','gforce']].dropna().corr()
# # sns.heatmap(data=df4_corr, annot=True)
# # plt.show()


# #what are the what are the location with the fastest roller coaster (minimum of 10)

# # ax = df4.query('location != "Other"')\
# #     .groupby('location')['speed_mph']\
# #     .agg(['mean', 'count'])\
# #     .query('count >= 10')\
# #     .sort_values('mean')['mean']\
# #     .plot(kind='barh',figsize=(12,5))
# # ax.set_title('Average Coast Speed')
# # ax.set_xlabel('Average Coaster Speed')
# # plt.show()



