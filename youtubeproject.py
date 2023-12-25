import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
plt.style.use('fivethirtyeight')
pd.set_option('display.max_column', None)

api_key = 'AIzaSyBXj3PMrOpPj51Q5WRiJR7khLDm7kxfrpI'

channel_ids = ['UC7eHZXheF8nVOfwB2PEslMw',
               'UCsTcErHg8oDvUnTzoqsYeNw',
               'UCBJycsmduvYEL83R_U4JriQ',
               'UCj22tfcQrWG7EMEKS0qLeEg',
               'UCcAd5Np7fO8SeejB1FVKcYw',
               'UCOhHO2ICt0ti9KAh-QHvttQ']


youtube = build('youtube', 'v3', developerKey=api_key)

##function to get channel stat

def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part = "snippet,contentDetails,statistics",
        id = ','.join(channel_ids))
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(channel_name = response['items'][i]['snippet']['title'],
                    subscriber = response['items'][i]['statistics']['subscriberCount'],
                    views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])

        all_data.append(data)
    return all_data

channels_stat = get_channel_stats(youtube, channel_ids)


df = pd.DataFrame(channels_stat)
df[['subscriber', 'views', 'Total_videos']] = df[['subscriber', 'views', 'Total_videos']].astype(int)

df = df.rename(columns= {'Total_videos' : 'total_videos'}) 

##plotting just the stats
# sns.set(rc={'figure.figsize':(10,8)})
# sns.barplot(x='channel_name', y='total_videos', data=df)
# plt.show()

##fetiching the video ids of the channel
##funtion to get video ids


playlist_id = df.loc[df['channel_name']=='CarryMinati', 'playlist_id'].iloc[0]


def get_video_ids(youtube, playlist_id):
    request = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = playlist_id,
        maxResults = 50)
    
    response = request.execute()

    video_ids = []
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
    
    next_page_token = response.get('nextPageToken')
    more_pages = True
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part = 'contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
    
            response = request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')



    return video_ids

video_ids = get_video_ids(youtube, playlist_id)



#funtion to get video details 

# def get_video_details(youtube, video_ids):
#     all_video_details = []
#     for i in range(0, len(video_ids), 50):    ##retriving the video details 50 at a time
#         request = youtube.videos().list(
#                     part = 'snippet,statistics',
#                     id = ','.join(video_ids[i:i+50]))
#         response = request.execute()

#         for video in response['items']:      ##storing details 50 at a time 
#             video_stats = dict(Title = video['snippet']['title'],
#                                Published_date = video['snippet']['publishedAt'],
#                                Views = video['statistics']['viewCount'],
#                                Likes = video['statistics']['likeCount'],
#                                comments = video['statistics']['commentCount'])
            
#             all_video_details.append(video_stats)

#     return len(all_video_details)

# print(get_video_details(youtube, video_ids))


# video_data = pd.DataFrame(video_details)

# video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).pd.date

# df[['subscriber', 'views', 'Total_videos']] = df[['subscriber', 'views', 'Total_videos']].astype(int)








def get_video_details(youtube, video_ids):
    all_video_details = []
    for i in range(0, len(video_ids), 50):    ##retrieving the video details 50 at a time
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i + 50]))
        response = request.execute()

        for video in response.get('items', []):      ##storing details 50 at a time 
            snippet = video.get('snippet', {})
            statistics = video.get('statistics', {})

            video_stats = dict(
                Title=snippet.get('title', ''),
                Published_date=snippet.get('publishedAt', ''),
                Views=statistics.get('viewCount', ''),
                Likes=statistics.get('likeCount', ''),
                Comments=statistics.get('commentCount', ''),
                Dislikes = statistics.get('dislikeCount')
            )

            all_video_details.append(video_stats)

    return all_video_details

result = get_video_details(youtube, video_ids)

df2 = pd.DataFrame(result)


df2 = df2.rename(columns={'Title': 'title', 'Published_date': 'published_date', 'Views': 'views', 'Likes': 'likes', 'Comments': 'comments', 'Dislikes': 'dislikes'})

# Convert specific columns to integers, handling non-numeric values
numeric_columns = ['views', 'likes', 'comments', 'dislikes']
df2[numeric_columns] = df2[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)      #when there are empty columns this should be done

# df2['published_date'] = pd.to_datetime(df2['published_date']).astype(int) // 10**9

df2['published_date'] = pd.to_datetime(df2['published_date']).dt.date

# df2_sorted = df2.sort_values(by='views', ascending=False).head(10)

# sns.barplot(x='views', y='title', data=df2_sorted)
# plt.show()


df2['month'] = pd.to_datetime(df2['published_date']).dt.strftime('%b')     #To extract month from date time column and add to month column

videos_per_month = df2.groupby('month', as_index=False).size()       #created new dataframe with month and total videos uploaded in those month

sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']

videos_per_month.index = pd.CategoricalIndex(videos_per_month['month'],categories = sort_order, ordered=True)

videos_per_month = videos_per_month.sort_index()

ax2 = sns.barplot(x='month', y='size', data=videos_per_month)

plt.show()