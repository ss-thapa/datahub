import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

# df = pd.read_csv('video_details.csv')

# df['years'] = pd.to_datetime(df['published_date']).dt.strftime('%Y')

# plt.figure(figsize=(12,6))
# plt.plot(df['years'],df['views'])
# plt.plot(df['years'], df['likes'])
# plt.xlabel('years')
# plt.ylabel('views')
# plt.title('number of views over')
# plt.legend(['views', 'likes'])
# plt.show()



# df = pd.read_csv('channel_data.csv')

# plt.figure(figsize=(10,4))
# plt.plot(df['channel_name'], df['subscriber'], marker = 'x')
# plt.show()



# plt.figure(figsize=(10,4))
# plt.scatter(df['channel_name'],df['subscriber'])
# plt.scatter(df['channel_name'],df['views'])
# plt.legend(['subscriber', 'views'])
# plt.show()



# df = pd.read_csv('channel_data.csv')


# sns.barplot(x= df['channel_name'], y=df['subscriber'], data=df)
# plt.title('total')
# plt.show()




df = pd.read_csv('video_details.csv')

# plt.figure(figsize=(8,5))
# sns.scatterplot(x='likes', y='comments', data=df)

# plt.show()


sns.histplot(x='comments', kde=True, bins=20, data=df)
plt.show()