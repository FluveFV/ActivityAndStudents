import pandas as pd
import datetime
import tqdm

# load the datasets
inpath1 = "../dati/td_ita.dta" # insert system path for time diary !
inpath2 = "../dati/data4diarynew_ITA.dta" # insert system path for demographics! !
inpath3 = "../dati/meteo_nov_2020.csv" # insert system path for weather !

td_dataset = pd.read_stata(inpath1)  # time diaries dataset
demo_dataset = pd.read_stata(inpath2) # demographics dataset

""" Cleaning procedure of the time diaries dataset """
""" we need to apply various steps:
1. consider only first two weeks of the survey
2. consider only the variables we want to investigate
3. consider only the physical activities"""

# cleaning 1
td_cleaned = td_dataset[td_dataset['first2w'] == 'First two weeks']

# cleaning 2
td_cleaned = td_cleaned[['id', 'date_not','what', 'withw', 'where', 'sport']]

# cleaning 3
td_cleaned= td_cleaned[(td_cleaned["what"]=="Sport") | (td_cleaned["what"]=="I will participate in sports activities")]

print(f"From the first cleaning process we obtain the dataset: \n {td_cleaned}")

""" Variable transformation """
"""
we want to add new variables:
- weather: the categories are 'level of precipitation'
- time session: duration of the sport activity

we want to apply a reclassification of the following variables:
- where column: the new categories are 'indoor - home', 'indoor - gym', 'outdoor'
- with who: the new categories are 'company', 'alone'
- time slot: the new categories are 'morning', 'lunch', 'afternoon', 'dinner', 'night'
"""

# time session variable
new_td = td_cleaned
new_td['date_not'] = pd.to_datetime(new_td['date_not'])
new_td['date_dur'] = new_td['date_not'] - timedelta(hours = 5) # in this way we can consider sport sessions across two days as single sport sessions

new_td = new_td .sort_values('date_dur') # sort the dataframe according to "date_not"
new_td['time_diff'] = new_td['date_dur'].diff() # compute the time difference between adjacent rows

new_session = (new_td['time_diff'] > pd.Timedelta(minutes=30)) | new_td['time_diff'].isnull() # search for new start session
new_td['session'] = new_session.cumsum() # Creazione di un nuovo identificatore di sessione basato su new_session

collapsed_sessions = new_td.groupby(['id', 'session']).agg(
    start_time=('date_not', 'first'),
    end_time=('date_not', 'last'),
    duration=('date_not', lambda x: ((x.max() - x.min()).total_seconds() / 60)+30)
).reset_index()

collapsed_sessions = collapsed_sessions.drop(columns='session')

# merge the two datasets
td_cleaned = td_cleaned.merge(collapsed_sessions, left_on=['id', 'date_not'], right_on=['id', 'start_time']) # inner join of the two datasets
print(f"From the first transformation process we obtain the dataset: \n {td_cleaned}")

# where variable
indoor_home = ['Home apartment /room', 'Weekend home or holiday apartment', 'House (friends others)', 'Relatives Home']
indoor_gym = ['Another indoor place', 'Gym, swimming pool, Sports centre …', 'Other university place']
outdoor = ['Countryside/mountain/hill/beach', 'Home garden/patio/courtyard', 'In the street', 'Another outdoor place',
           'Café, pub, bar', 'Shops, shopping centres']

# function for reclassification
def where_reclass(row):
    if row['where'] in indoor_dome:
        new_class = 'indoor - home'
    elif row['where'] in outdoor:
        new_class = 'outdoor'
    elif row['where'] in indoor_gym:
        new_class = 'indoor - gym'
    else:
        new_class = np.nan

    return new_class

td_cleaned['new where'] = td_cleaned.apply(where_reclass, axis=1)

# with who variable
company = ['Partner', 'Friend(s)', 'Relative(s)', 'Roommate(s)', 'Other', 'Colleague(s)', 'Classmate(s)']

# function for reclassification
def with_reclass(row):
    if row["withw"] in company:
        new_class = "company"
    else:
        new_class = "alone"

    return new_class

td_cleaned['new withw'] = td_cleaned.apply(with_reclass, axis=1)
print(f"From the second transformation process we obtain the dataset: \n {td_cleaned}")

# date variable reclass
def date_reclass(row):
    elements = str(row["date_not"])[:10].split("-")
    year = int(elements[0])
    month = int(elements[1])
    day = int(elements[2])
    new_date = datetime.date(year, month, day)

    return new_date

td_cleaned['date'] = td_cleaned.apply(date_reclass, axis=1)

# date variable reclass
def time_reclass(row):
    cleaning_1 = str(row["date_not"])
    hours = int(cleaning_1[11:13])
    minutes = int(cleaning_1[14:16])
    new_time = datetime.time(hours, minutes, 0)

    return new_time

td_cleaned['time'] = td_cleaned.apply(time_reclass, axis=1)
print(f"From the third transformation process we obtain the dataset: \n {td_cleaned}")

# function for reclassification of the hours
def timeslot_reclass(row):
    if row['time'] >= datetime.time(5, 0, 0) and row["time"] < datetime.time(12, 0, 0): 
        new_class = "morning"
    elif row["time"] >= datetime.time(12, 0, 0) and row["time"] < datetime.time(14, 0, 0):
        new_class = "midday"
    elif row["time"] >= datetime.time(14, 0, 0) and row["time"] < datetime.time(19, 0, 0):
        new_class = "afternoon"
    elif row["time"] >= datetime.time(19, 0, 0) and row["time"] < datetime.time(21, 0, 0):
        new_class = "evening"
    else:
        new_class = "night"
    return new_class

td_cleaned['new time'] = td_cleaned.apply(timeslot_reclass, axis=1)
print(f"From the fourth transformation process we obtain the dataset: \n {td_cleaned}")

# weather variable
nov_meteo = pd.read_csv(inpath3)
print(f"weather for the month of all the days of november 2020: \n {nov_meteo.head()}")

# reclass of day variable (in order to merge with td_cleaned dataset)
vals = list(nov_meteo["date"].values)
new_vals = []

for el in vals:
    current_el = el.split(" ")
    day = int(current_el[1])
    new_date = datetime.date(2020, 11, day)
    new_vals.append(new_date)

# new meteo dataset
meteo_data = {'date': pd.Series(new_vals),
              'prec': nov_meteo['prec'],
              'tmin': nov_meteo['tmin'],
              'tmax': nov_meteo['tmax']}

new_nov_meteo = pd.DataFrame(data=meteo_data)
print(f"weather dataset cleaned is now: \n {new_nov_meteo}")

# converion of the userid into an integer
td_cleaned['id'] = td_cleaned['id'].astype(int)
demo_dataset['userid'] = demo_dataset['userid'].astype(int)

# we save a dataset for descritpive analysis
td_cleaned.to_csv('descriptive_dataset.csv', index=False)

# merge the two datasets
td_cleaned = td_cleaned[['id', 'duration', 'new where', 'new withw', 'date', 'new time']]
td_cleaned = td_cleaned.merge(new_nov_meteo, left_on='date', right_on='date', how='left') # left join of the two datasets

# merge the td_cleaned dataset with the demographic dataset
final_dataset = td_cleaned.merge(demo_dataset, left_on='id', right_on='userid', how='left')

print(f"the final dataset with sport sessions and demographic features is: \n {sport_demo}")
final_demo.to_csv('sport_dataset.csv', index=False)
