import pandas as pd
import datetime
import numpy as np
from datetime import timedelta
import tqdm

# load the datasets
inpath1 = "../dati/td_ita.dta" # insert system path for time diary !
inpath2 = "../dati/data4diarynew_ITA.dta" # insert system path for demographics! !

td_dataset = pd.read_stata(inpath1)  # time diaries dataset
demo_dataset = pd.read_stata(inpath2) # demographics dataset

""" --- Cleaning procedure of the time diaries dataset --- """
""" we need to apply various steps:
1. consider only first two weeks of the survey
2. consider only the variables we want to investigate:
    - id of the user, 
    - date, 
    - what the user is doing,
    - with who, 
    - where and what type of sport activity
3. consider only the sport activities"""

# cleaning 1
td_cleaned = td_dataset[td_dataset['first2w'] == 'First two weeks']

# cleaning 3
td_cleaned= td_cleaned[(td_cleaned["what"]=="Sport") | (td_cleaned["what"]=="I will participate in sports activities")]


""" Variable transformation """
"""
we want to add new variables:
- time session: duration of the sport activity

we want to reclassify the following variables:
- where column: the new categories are 'indoor', 'outdoor'
- with who: the new categories are 'company', 'alone'
- time: the new categories are 'morning', 'midday', 'afternoon', 'evening', 'night'
"""

# time session variable
new_td = td_cleaned
new_td['date_not'] = pd.to_datetime(new_td['date_not'])
new_td['date_dur'] = new_td['date_not'] - timedelta(hours = 5)

new_td = new_td .sort_values('date_dur') # sort the dataframe according to "date_dur"
new_td['time_diff'] = new_td['date_dur'].diff() # compute the time difference between adjacent rows

new_session = (new_td['time_diff'] > pd.Timedelta(minutes=30)) | new_td['time_diff'].isnull() # search for new start session
new_td['session'] = new_session.cumsum() # Creazione di un nuovo identificatore di sessione basato su new_session

collapsed_sessions = new_td.groupby(['id', 'session']).agg(
    start_time=('date_not', 'first'),
    end_time=('date_not', 'last'),
    duration=('date_dur', lambda x: ((x.max() - x.min()).total_seconds() / 60)+30)
).reset_index()

collapsed_sessions = collapsed_sessions.drop(columns='session')

# merge the two datasets
td_cleaned = td_cleaned.merge(collapsed_sessions, left_on=['id', 'date_not'], right_on=['id', 'start_time']) # inner join of the two datasets

# where variable
td_cleaned['where recoded'] = td_cleaned['where'].replace(['Home apartment /room', 'Weekend home or holiday apartment', 'House (friends others)', 'Relatives Home', 'Home garden/patio/courtyard',
                                                           'Another indoor place', 'Gym, swimming pool, Sports centre …', 'Other university place', 'Countryside/mountain/hill/beach', 'In the street', 'Another outdoor place', 'Café, pub, bar', 'Shops, shopping centres',
                                                           'Not answer'],
                                                          ['indoor', 'indoor', 'indoor', 'indoor', 'indoor',
                                                           'outdoor', 'outdoor', 'outdoor', 'outdoor', 'outdoor', 'outdoor', 'outdoor', 'outdoor',
                                                           'Not answer where'])

# with who variable
td_cleaned['withw recoded'] = td_cleaned['withw'].replace(['Partner', 'Friend(s)', 'Relative(s)', 'Roommate(s)', 'Other', 'Colleague(s)', 'Classmate(s)',
                                                           'Alone',
                                                           'Not answer'],
                                                          ['company', 'company', 'company', 'company', 'company', 'company', 'company',
                                                           'alone',
                                                           'Not answer withw'])

# time variable
td_cleaned['hours'] = td_cleaned['date_not'].dt.hour

# sport variable
td_cleaned['sport recoded'] = td_cleaned['sport'].replace(['Walking, Trekking, and hiking',
                                                           'Jogging and running',
                                                           'Cycling, skiing, and skating', 'Ball games', 'Other outdoor activities',
                                                           'Gymnastics and fitness',
                                                           'Water sports', 'Other indoor activities'],
                                                          ['Walking, Trekking, and hiking',
                                                           'Jogging and running',
                                                           'Outdoor activities', 'Outdoor activities', 'Outdoor activities',
                                                           'Gymnastics and fitness',
                                                           'Other indoor activities', 'Other indoor activities'])


# function for reclassification of the hours
def timeslot_reclass(row):
    if row["hours"] < 12:
        new_class = "morning"
    elif row["hours"] >= 12 and row["hours"] < 14:
        new_class = "midday"
    elif row["hours"] >= 14 and row["hours"] < 19:
        new_class = "afternoon"
    elif row["hours"] >= 19 and row["hours"] < 21:
        new_class = "evening"
    else:
        new_class = "night"
    return new_class

td_cleaned['hours recoded'] = td_cleaned.apply(timeslot_reclass, axis=1)

# conversion of the userid into an integer
td_cleaned['id'] = td_cleaned['id'].astype(int)
demo_dataset['userid'] = demo_dataset['userid'].astype(int)

# consider only the variables we want to investigate
td_cleaned = td_cleaned[['id', 'start_time', 'week', 'DD_not', 'hh_not', 'sport', 'duration', 'where recoded', 'withw recoded', 'hours recoded','sport recoded']]

# where variable
where_df = td_cleaned.pivot(columns=['where recoded'], values='duration')
where_df = where_df.fillna(0)
where_df = where_df[['indoor', 'outdoor', 'Not answer where']]

# with who variable
withw_df = td_cleaned.pivot(columns=['withw recoded'], values='duration')
withw_df = withw_df.fillna(0)
withw_df = withw_df[['alone', 'company', 'Not answer withw']]

# time variable
time_df = td_cleaned.pivot(columns=['hours recoded'], values='duration')
time_df = time_df.fillna(0)
time_df = time_df[['morning', 'midday', 'afternoon', 'evening', 'night']]

# sport variable
sport_df = td_cleaned.pivot(columns=['sport recoded'], values='duration')
sport_df = sport_df.fillna(0)
sport_df = sport_df[['Walking, Trekking, and hiking', 'Jogging and running', 'Outdoor activities', 'Gymnastics and fitness', 'Other indoor activities']]

# merge all the dataframes together
final_data = {'id': pd.Series(td_cleaned['id']),
              'indoor': pd.Series(where_df['indoor']),
              'outdoor': pd.Series(where_df['outdoor']),
              'alone': pd.Series(withw_df['alone']),
              'company': pd.Series(withw_df['company']),
              'morning': pd.Series(time_df['morning']),
              'midday': pd.Series(time_df['midday']),
              'afternoon': pd.Series(time_df['afternoon']),
              'evening': pd.Series(time_df['evening']),
              'night': pd.Series(time_df['night']),
              'walking': pd.Series(sport_df['Walking, Trekking, and hiking']),
              'running': pd.Series(sport_df['Jogging and running']),
              'outdoor activities': pd.Series(sport_df['Outdoor activities']),
              'fitness': pd.Series(sport_df['Gymnastics and fitness']),
              'indoor activities': pd.Series(sport_df['Other indoor activities']),
              }

final_dataset = pd.DataFrame(data=final_data)
final_dataset = final_dataset.groupby('id', as_index=False).sum()

# merge the td_cleaned dataset with the demographic dataset
almost_dataset = final_dataset.merge(demo_dataset, left_on='id', right_on='userid', how='left')
complete_dataset = almost_dataset.merge(total_dur, left_on='id', right_on='id', how='left')

cat_dataset = td_cleaned.merge(demo_dataset, left_on='id', right_on='userid', how='left')

# clean the dataset by keeping only the variables we want to investigate
complete_dataset = complete_dataset[['id', 'duration', 'indoor', 'outdoor', 'alone', 'company', 'morning', 'midday',
                                     'afternoon', 'evening', 'night','walking',
                                     'running', 'outdoor activities', 'fitness', 'indoor activities',
                                     'degree', 'department', 'w1_A01']]

cat_dataset.to_csv('data/categorical_sport_dataset.csv', index=False)
complete_dataset.to_csv('data/continuous_sport_dataset.csv', index=False)
