import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

'''load the dataset'''
sport_data = pd.read_csv("data/sport_dataset.csv")

''' --- bivariate analysis and plots  --- '''

# 1. gender and place: Chi-squared test of independency
crosstable_1 = pd.crosstab(sport_data['w1_A01'], sport_data['new where'])
print(f"contingency table is: {crosstable_1}")

chi2_1, p_1, dof_1, expected_1 = chi2_contingency(crosstable_1)
print(f"Chi-squared value is {chi2_1}, p-value is {p_1} \n")

sns.countplot(data=sport_data, x="new where", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_gender.png', format="png")
plt.show()

# 2. gender and company: Chi-squared test of independency
crosstable_2 = pd.crosstab(sport_data['w1_A01'], sport_data['new withw'])
print(f"contingency table is: {crosstable_2}")

chi2_2, p_2, dof_2, expected_2 = chi2_contingency(crosstable_2)
print(f"Chi-squared value is {chi2_2}, p-value is {p_2} \n")

sns.countplot(data=sport_data, x="new withw", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and comapny')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_gender.png', format="png")
plt.show()

# 3. gender and type of activity: Chi-squared test of independency
crosstable_3 = pd.crosstab(sport_data['w1_A01'], sport_data['sport'])
print(f"contingency table is: {crosstable_3}")

chi2_3, p_3, dof_3, expected_3 = chi2_contingency(crosstable_3)
print(f"Chi-squared value is {chi2_3 }, p-value is {p_3} \n")

sns.countplot(data=sport_data, x="sport", hue="w1_A01", stat="percent")
plt.title('sport sessions by gender and sport activity')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('type of sport activity')
plt.savefig('graphs/bivariate_graphs/activity_by_gender.png', format="png")
plt.show()

# 4. gender and daily routine: Chi-squared test of independency
crosstable_4 = pd.crosstab(sport_data['w1_A01'], sport_data['new time'])
print(f"contingency table is: {crosstable_4}")

chi2_4, p_4, dof_4, expected_4 = chi2_contingency(crosstable_4)
print(f"Chi-squared value is {chi2_4}, p-value is {p_4} \n")

day_order = ["morning", "midday", "afternoon", "evening", "night"]
sns.countplot(data=sport_data, x="new time", hue="w1_A01", stat="percent", order=day_order)
plt.title('sport sessions by gender and sport routine')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='sex', loc='upper right', ncol=2)
plt.xlabel('part of the day (recoded)')
plt.savefig('graphs/bivariate_graphs/ruotine_by_gender.png', format="png")
plt.show()

# 5. department and session duration: Chi-squared test of independency
crosstable_5 = pd.crosstab(sport_data['department'], sport_data['duration'])
print(f"contingency table is: {crosstable_5}")

chi2_5, p_5, dof_5, expected_5 = chi2_contingency(crosstable_5)
print(f"Chi-squared value is {chi2_5}, p-value is {p_5} \n")

sns.violinplot(data=sport_data, x="duration", hue="department", fill=False, inner='point')
plt.title('sport sessions by duration and user department')
plt.xticks(rotation=45, fontsize="xx-small", ha="right")
plt.xlabel('duration of sport session')
plt.legend(loc='lower right', title='unitn departments', fontsize='xx-small')
plt.tight_layout()
plt.savefig('graphs/bivariate_graphs/duration_by_department.png', format="png")
plt.show()

# 6. department and type of activity: Chi-squared test of independency
crosstable_6 = pd.crosstab(sport_data['department'], sport_data['sport'])
print(f"contingency table is: {crosstable_6}")

chi2_6, p_6, dof_6, expected_6 = chi2_contingency(crosstable_6)
print(f"Chi-squared value is {chi2_6}, p-value is {p_6} \n")

sns.countplot(data=sport_data, x="sport", hue="department", stat="percent")
plt.title('sport sessions by department and sport activity')
plt.xticks(rotation=45, fontsize="small", ha="right")
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='x-small', title='unitn departments')
plt.xlabel('type of sport activity')
plt.savefig('graphs/bivariate_graphs/activity_by_department.png', format="png")
plt.show()

# 7. type of activity and place: Chi-squared test of independency
crosstable_7 = pd.crosstab(sport_data['sport'], sport_data['new where'])
print(f"contingency table is: {crosstable_7}")

chi2_7, p_7, dof_7, expected_7 = chi2_contingency(crosstable_7)
print(f"Chi-squared value is {chi2_7}, p-value is {p_7} \n")

sns.countplot(data=sport_data, x="new where", hue="sport", stat="percent")
plt.title('sport sessions by location and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_activity.png', format="png")
plt.show()

# 8. type of activity and company: Chi-squared test of independency
crosstable_8 = pd.crosstab(sport_data['sport'], sport_data['new withw'])
print(f"contingency table is: {crosstable_8}")

chi2_8, p_8, dof_8, expected_8 = chi2_contingency(crosstable_8)
print(f"Chi-squared value is {chi2_8}, p-value is {p_8} \n")

sns.countplot(data=sport_data, x="new withw", hue="sport", stat="percent")
plt.title('sport sessions by company and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_activity.png', format="png")
plt.show()

# 9. type of activity and daily routine: Chi-squared test of independency
crosstable_9 = pd.crosstab(sport_data['sport'], sport_data['new time'])
print(f"contingency table is: {crosstable_9}")

chi2_9, p_9, dof_9, expected_9 = chi2_contingency(crosstable_9)
print(f"Chi-squared value is {chi2_9}, p-value is {p_9} \n")

sns.countplot(data=sport_data, x="new time", hue="sport", stat="percent", order=day_order)
plt.title('sport sessions by time and activity type')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, fontsize='small', title='sport activities')
plt.xlabel('part of the day (recoded)')
plt.savefig('graphs/bivariate_graphs/time_by_activity.png', format="png")
plt.show()

# 10. place and company: Chi-squared test of independency
crosstable_10 = pd.crosstab(sport_data['new withw'], sport_data['new where'])
print(f"contingency table is: {crosstable_10}")

chi2_10, p_10, dof_10, expected_10 = chi2_contingency(crosstable_10)
print(f"Chi-squared value is {chi2_10}, p-value is {p_10} \n")

sns.countplot(data=sport_data, x="new where", hue="new withw", stat="percent")
plt.title('sport sessions by company and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(ncol=2, title='with who (recoded)')
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_company.png', format="png")
plt.show()

# 11. place and daily routine: Chi-squared test of independency
crosstable_11 = pd.crosstab(sport_data['new time'], sport_data['new where'])
print(f"contingency table is: {crosstable_11}")

chi2_11, p_11, dof_11, expected_11 = chi2_contingency(crosstable_11)
print(f"Chi-squared value is {chi2_11}, p-value is {p_11} \n")

sns.countplot(data=sport_data, x="new where", hue="new time", stat="percent", hue_order=day_order)
plt.title('sport sessions by time and location')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='part of the day (recoded)', ncol=2)
plt.xlabel('where (recoded)')
plt.savefig('graphs/bivariate_graphs/where_by_time.png', format="png")
plt.show()

# 12. company and daily routine: Chi-squared test of independency
crosstable_12 = pd.crosstab(sport_data['new withw'], sport_data['new time'])
print(f"contingency table is: {crosstable_12}")

chi2_12, p_12, dof_12, expected_12 = chi2_contingency(crosstable_12)
print(f"Chi-squared value is {chi2_12}, p-value is {p_12} \n")

sns.countplot(data=sport_data, x="new withw", hue="new time", stat="percent", hue_order=day_order)
plt.title('sport sessions by location and sport activity')
plt.tight_layout()
plt.yticks(range(0, 101, 10))
plt.legend(title='part of the day (recoded)', ncol=2)
plt.xlabel('with who (recoded)')
plt.savefig('graphs/bivariate_graphs/company_by_time.png', format="png")
plt.show()
