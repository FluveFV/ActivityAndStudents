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
#plt.ylabel('sport session')
plt.xlabel('location')
plt.show()

plt.savefig('graphs/session_by_location.png')

# distribution of sport behaviour: presence of others
sns.countplot(des_dataset, x="new withw", stat="percent")
plt.title('sport sessions by company')
#plt.ylabel('sport session')
plt.xlabel('company')

plt.show()
plt.savefig('graphs/session_by_company.png')

# distribution of sport behaviour: type of activity
sns.countplot(des_dataset, x="sport", stat="percent")
plt.title('sport sessions by type of activity')
#plt.ylabel('sport session')
plt.xlabel('type of activity')
plt.xticks(rotation="vertical", fontsize="xx-small", visible=True)

plt.show()
plt.savefig('graphs/session_by_activity.png')

# distribution of sport behaviour: duration
sns.countplot(des_dataset, x="duration", stat="percent")
plt.title('sport sessions by time duration')
#plt.ylabel('sport session')
plt.xlabel('duration of the activity (minutes)')
plt.xticks(rotation="vertical", fontsize="small")

plt.show()
plt.savefig('graphs/session_by_duration.png')

# distribution of sport behaviour: day
sns.countplot(des_dataset, x="new time", stat="percent")
plt.title('sport sessions by daily routine')
#plt.ylabel('sport session')
plt.xlabel('daily routine')

plt.show()
plt.savefig('graphs/session_by_dailyroutine.png')









