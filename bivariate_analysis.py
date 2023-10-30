import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''load the datasets'''
sport_att = pd.read_csv("data/sport_attitude_dataset.csv")
sport_demo = pd.read_csv("data/sport_demo_dataset.csv")

''' --- bivariate analysis for sport behaviour and user attitudes --- '''

# 1. attitudes and place
'''hypothesis:
persone più socievoli avranno maggiore probabilità di frequentare luoghi pubblici (palestre) per fare sport rispetto a persone meno socievoli 
'''
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

sns.boxplot(data=sport_att, x="new where", y="Extraversion", ax=axes[0,0], hue="new where")
axes[0,0].set_title('Extraversion')
axes[0,0].set_ylabel('')
axes[0,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new where", y="Agreeableness", ax=axes[0,1], hue="new where")
axes[0,1].set_title('Agreeableness')
axes[0,1].set_ylabel('')
axes[0,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new where", y="Conscientiousness", ax=axes[1,0], hue="new where")
axes[1,0].set_title('Conscientiousness')
axes[1,0].set_ylabel('')
axes[1,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new where", y="Neuroticism", ax=axes[1,1], hue="new where")
axes[1,1].set_title('Neuroticism')
axes[1,1].set_ylabel('')
axes[1,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new where", y="Openness", ax=axes[2,0], hue="new where")
axes[2,0].set_title('Openness')
axes[2,0].set_ylabel('')
axes[2,0].set_xlabel('')

fig.delaxes(axes[2,1])

plt.suptitle("Location of sport session by users attitudes")
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/where_by_attitude.png', format="png")
plt.show()

# 2. attitudes and company
'''hypothesis:
persone più socievoli avranno maggiore probabilità di frequentare luoghi pubblici per fare sport rispetto a persone meno socievoli
'''
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

sns.boxplot(data=sport_att, x="new withw", y="Extraversion", ax=axes[0,0], hue="new withw")
axes[0,0].set_title('Extraversion')
axes[0,0].set_ylabel('')
axes[0,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new withw", y="Agreeableness", ax=axes[0,1], hue="new withw")
axes[0,1].set_title('Agreeableness')
axes[0,1].set_ylabel('')
axes[0,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new withw", y="Conscientiousness", ax=axes[1,0], hue="new withw")
axes[1,0].set_title('Conscientiousness')
axes[1,0].set_ylabel('')
axes[1,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new withw", y="Neuroticism", ax=axes[1,1], hue="new withw")
axes[1,1].set_title('Neuroticism')
axes[1,1].set_ylabel('')
axes[1,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new withw", y="Openness", ax=axes[2,0], hue="new withw")
axes[2,0].set_title('Openness')
axes[2,0].set_ylabel('')
axes[2,0].set_xlabel('')

fig.delaxes(axes[2,1])

plt.suptitle("Company of sport session by users attitudes")
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/company_by_attitude.png', format="png")
plt.show()

# 3. attitudes and daily routine
'''hypothesis:
to implement
'''
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

sns.boxplot(data=sport_att, x="new time", y="Extraversion", ax=axes[0,0], hue="new time")
axes[0,0].set_title('Extraversion')
axes[0,0].set_ylabel('')
axes[0,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new time", y="Agreeableness", ax=axes[0,1], hue="new time")
axes[0,1].set_title('Agreeableness')
axes[0,1].set_ylabel('')
axes[0,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new time", y="Conscientiousness", ax=axes[1,0], hue="new time")
axes[1,0].set_title('Conscientiousness')
axes[1,0].set_ylabel('')
axes[1,0].set_xlabel('')

sns.boxplot(data=sport_att, x="new time", y="Neuroticism", ax=axes[1,1], hue="new time")
axes[1,1].set_title('Neuroticism')
axes[1,1].set_ylabel('')
axes[1,1].set_xlabel('')

sns.boxplot(data=sport_att, x="new time", y="Openness", ax=axes[2,0], hue="new time")
axes[2,0].set_title('Openness')
axes[2,0].set_ylabel('')
axes[2,0].set_xlabel('')

fig.delaxes(axes[2,1])

plt.suptitle("Routine of sport session by users attitudes")
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/routine_by_attitude.png', format="png")
plt.show()


''' --- bivariate analysis for sport behaviour and user demographics --- '''

# 1. gender and place
'''hypothesis:
female tend to practice more often sports in close places (safety reasons + type of sport?)
'''
sns.catplot(data=sport_demo, x="new where", kind="count", hue="w1_A01")
plt.title('sport sessions by gender and location')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/where_by_gender.png', format="png")
plt.show()

# 2. age and session duration
sns.boxplot(data=sport_demo, x="cohort", y="duration")
plt.title('sport sessions by age and session duration')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/duration_by_age.png', format="png")
plt.show()

''' --- bivariate analysis for sport behaviour --- '''

# 1. place and company
'''hypothesis:
based on the location of session sport the company could be different
'''
sns.catplot(data=sport_demo, x="new where", kind="count", hue="new withw")
plt.title('sport sessions by company and location')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/where_by_company.png', format="png")
plt.show()

# 2. place and time
'''hypothesis:
based on the time of the day the user is practicing sport, the location will be different
'''
sns.catplot(data=sport_demo, x="new where", kind="count", hue="new time")
plt.title('sport sessions by time and location')
#plt.legend(loc='upper right', title='Time')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/where_by_time.png', format="png")
plt.show()