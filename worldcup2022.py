import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_column', None)


df = pd.read_csv('/Users/sunilthapa/Desktop/programming/datahub/datas/worldcup_quatar.csv')

# columns_drop = ['possession in contest', 'goal inside the penalty area team1', 'goal inside the penalty area team2', 'goal outside the penalty area team1','goal outside the penalty area team2','assists team1', 'assists team2','attempts inside the penalty area team1','attempts inside the penalty area  team2','attempts outside the penalty area  team1','attempts outside the penalty area  team2',
#         'left channel team1',
#        'left channel team2', 'left inside channel team1',
#        'left inside channel team2', 'central channel team1',
#        'central channel team2', 'right inside channel team1',
#        'right inside channel team2', 'right channel team1',
#        'right channel team2','total offers to receive team1',
#        'total offers to receive team2', 'inbehind offers to receive team1',
#        'inbehind offers to receive team2', 'inbetween offers to receive team1',
#        'inbetween offers to receive team2', 'infront offers to receive team1',
#        'infront offers to receive team2',
#        'receptions between midfield and defensive lines team1',
#        'receptions between midfield and defensive lines team2',
#        'attempted line breaks team1', 'attempted line breaks team2',
#        'completed line breaksteam1', 'completed line breaks team2','crosses team1',
#        'crosses team2', 'crosses completed team1', 'crosses completed team2','switches of play completed team1', 'switches of play completed team2',
#        'forced turnovers team1', 'forced turnovers team2',
#        'defensive pressures applied team1',
#        'defensive pressures applied team2']


# df = df.drop(columns_drop, axis=1)



df['date'] = pd.to_datetime(df['date'])
df['hour'] = pd.to_timedelta(df['hour'])

df = df.rename(columns={'possession team1':'possession_team1', 'possession team2':'possession team2',
       'number of goals team1':'number_of_goals_team1', 'number of goals team2':'number_of_goals_team2',
       'total attempts team1':'total_attempts_team1', 'total attempts team2':'total_attempts_team2',
       'conceded team1':'conceded_team1', 'conceded team2':'conceded_team2', 'on target attempts team1':'on_target_attempts_team1',
       'on target attempts team2':'on_target_attempts_team2', 'off target attempts team1':'off_target_attempts_team1',
       'off target attempts team2':'off_target_attempts_team2', 'attempted defensive line breaks team1':'attempted_defensive_line_breaks_team1',
       'attempted defensive line breaks team2':'attempted_defensive_line_breaks_team2',
       'completed defensive line breaksteam1':'completed_defensive_line_breaks_team1',
       'completed defensive line breaks team2':'completed_defensive_line_breaks_team2', 'yellow cards team1':'yellow_cards_team1',
       'yellow cards team2':'yellow_cards_team2', 'red cards team1':'red_cards_team1', 'red cards team2':'red_cards_team2',
       'fouls against team1':'fouls_against_team1', 'fouls against team2':'fouls_against_team2', 'offsides team1':'offsides_team1',
       'offsides team2':'offsides_team2', 'passes team1':'passes_team1', 'passes team2':'passes_team2',
       'passes completed team1':'passes_completed_team1', 'passes completed team2':'passes_completed_team2', 'corners team1':'corners_team1',
       'corners team2':'corners_team2', 'free kicks team1':'free_kicks_team1', 'free kicks team2':'free_kicks_team2',
       'penalties scored team1':'penalties_scored_team1', 'penalties scored team2':'penalties_scored_team2',
       'goal preventions team1':'goal_preventions_team1', 'goal preventions team2':'goal_preventions_team2', 'own goals team1':'own_goals_team1',
       'own goals team2':'own_goals_team2'})




## total goals by argenttina 

def calculate_total_goals(row):
    if row['team1'] == 'ARGENTINA':
        return row['number_of_goals_team1']
    elif row['team2'] == 'ARGENTINA':
        return row['number_of_goals_team2']
    else:
        return 0


argentina_maches = df.loc[(df['team1'] == 'ARGENTINA') | (df['team2'] == 'ARGENTINA')] 

total_goals = argentina_maches.apply(calculate_total_goals, axis=1).sum()



## total attempts in all the matches of the argentina


def calculate_total_goals(row):
    if row['team1'] == 'ARGENTINA':
        return row['total_attempts_team1']
    elif row['team2'] == 'ARGENTINA':
        return row['total_attempts_team2']
    else:
        return 0


argentina_maches = df.loc[(df['team1'] == 'ARGENTINA') | (df['team2'] == 'ARGENTINA')] 

total_attempt = argentina_maches.apply(calculate_total_goals, axis=1).sum()



### every matches where the goal attempts are more then 10 by both team

sun = df.loc[(df['total_attempts_team1'] > 10) & (df['total_attempts_team2'] > 10)]
print(sun.shape)












