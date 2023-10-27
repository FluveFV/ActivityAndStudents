import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load the descriptive dataset
des_dataset = pd.read_csv("data/descriptive_dataset.csv")
print(des_dataset)
print(des_dataset.columns)

'''descriptive statistics for the dataset'''
des_dataset = des_dataset.fillna("no information")

# distribution of sport behaviour: location of the user
sns.countplot(des_dataset, x="new where", stat="percent")
plt.title('sport sessions by location of the user')
plt.xlabel('location')
plt.savefig('graphs/session_by_location.png', format="png")
plt.show()

# distribution of sport behaviour: presence of others
sns.countplot(des_dataset, x="new withw", stat="percent")
plt.title('sport sessions by company')
plt.xlabel('company')
plt.savefig('graphs/session_by_company.png', format="png")
plt.show()

# distribution of sport behaviour: type of activity
sns.countplot(des_dataset, x="sport", stat="percent")
plt.title('sport sessions by type of activity')
plt.xlabel('type of activity')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.savefig('graphs/session_by_activity.png', format="png")
plt.show()

# distribution of sport behaviour: duration
sns.countplot(des_dataset, x="duration", stat="percent")
plt.title('sport sessions by time duration')
plt.xlabel('duration of the activity (minutes)')
plt.xticks(rotation=45, fontsize="xx-small", ha="center")
plt.savefig('graphs/session_by_duration.png', format="png")
plt.show()

# distribution of sport behaviour: day
sns.countplot(des_dataset, x="new time", stat="percent")
plt.title('sport sessions by daily routine')
plt.xlabel('daily routine')
plt.savefig('graphs/session_by_dailyroutine.png', format="png")
plt.show()

# distribution of sport behaviour: date
days = list(des_dataset["date"].unique())
days.sort()

sns.countplot(des_dataset, x="date", stat="percent", order=days)
plt.title('sport sessions by date')
plt.xlabel('days of the survey')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.savefig('graphs/session_by_date.png', format="png")
plt.show()
