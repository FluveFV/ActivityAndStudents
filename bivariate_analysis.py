import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''load the datasets'''
sport_data = pd.read_csv("data/sport_dataset.csv")

''' --- bivariate analysis for sport behaviour and user demographics --- '''

# 1. gender and place
sns.countplot(data=sport_data, x="new where", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_gender.png', format="png")
plt.show()

# 2. gender and company
sns.countplot(data=sport_data, x="new withw", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and comapny')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_gender.png', format="png")
plt.show()

# 3. gender and type of activity
sns.countplot(data=sport_data, x="sport", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and sport activity')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('type of sport activity')
plt.savefig('graphs/bivariate_graphs/activity_by_gender.png', format="png")
plt.show()

# 4. gender and daily routine
day_order = ["morning", "midday", "afternoon", "evening", "night"]
sns.countplot(data=sport_data, x="new time", hue="w1_A01", stat="percent", order=day_order)
plt.title('sport sessions by gender and sport routine')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('part of the day (recoded)')
plt.savefig('graphs/bivariate_graphs/ruotine_by_gender.png', format="png")
plt.show()

# 5. department and session duration
sns.violinplot(data=sport_data, x="duration", hue="department", fill=False, inner='point')
plt.title('sport sessions by duration and user department')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.xlabel('duration of sport session')
plt.legend(loc='lower right', title='unitn departments', fontsize='xx-small')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/duration_by_department.png', format="png")
plt.show()

# 6. department and type of activity
sns.countplot(data=sport_data, x="sport", hue="department", stat="percent")
plt.title('sport sessions by department and sport activity')
plt.xticks(rotation=45, fontsize="small", ha="right")
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='x-small', title='unitn departments')
plt.xlabel('type of sport activity')
plt.savefig('graphs/bivariate_graphs/activity_by_department.png', format="png")
plt.show()


''' --- bivariate analysis for sport behaviour --- '''

# 1. type of activity and place
sns.countplot(data=sport_data, x="new where", hue="sport", stat="percent")
plt.title('sport sessions by location and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_activity.png', format="png")
plt.show()

# 2. type of activity and company
sns.countplot(data=sport_data, x="new withw", hue="sport", stat="percent")
plt.title('sport sessions by company and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_activity.png', format="png")
plt.show()

# 3. type of activity and routine
sns.countplot(data=sport_data, x="new time", hue="sport", stat="percent", order=day_order)
plt.title('sport sessions by time and activity type')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('part of the day (recoded)')
plt.savefig('graphs/bivariate_graphs/time_by_activity.png', format="png")
plt.show()

# 4. place and company
sns.countplot(data=sport_data, x="new where", hue="new withw", stat="percent")
plt.title('sport sessions by company and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, title='with who (recoded)')
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_company.png', format="png")
plt.show()

# 5. place and routine
sns.countplot(data=sport_data, x="new where", hue="new time", stat="percent", hue_order=day_order)
plt.title('sport sessions by time and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='part of the day (recoded)', ncol=2)
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_time.png', format="png")
plt.show()

# 6. company and routine
sns.countplot(data=sport_data, x="new withw", hue="new time", stat="percent", hue_order=day_order)
plt.title('sport sessions by location and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='part of the day (recoded)', ncol=2)
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_time.png', format="png")
plt.show()
