import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
df = pd.read_csv(r'Banking_DS_Project\banking_data.csv')
#Distribution of age among clients
# print(df['age'].unique())
sns.set_style('whitegrid')
pd.set_option('future.no_silent_downcasting', True)
#a) Style 1
#age_counts = df['age'].value_counts().sort_index()

# plt.figure(figsize=(20,10))
# sns.barplot(x=age_counts.index, y=age_counts.values)  # X-axis: Age (sorted), Y-axis: Count

# plt.xlabel('Age')
# plt.ylabel('Count of People')
# plt.title('Age Distribution')
# plt.show()

#a) Style 2
# plt.figure(figsize=(10,15))
# sns.countplot(x=df['age'])  # Count occurrences of each age
# plt.xlabel("Age")
# plt.ylabel("Count of People")
# plt.title("Age Distribution")
# plt.show()

#b)
# plt.figure(figsize=(10,15))
# sns.countplot(x=df['job'],order=df['job'].value_counts().index)  # Count occurrences of each age
# plt.xlabel("Job")
# plt.ylabel("Count of People")
# plt.title("Job Distribution")
# plt.show()

#c)
# plt.figure(figsize=(10,15))
# sns.countplot(x=df['marital_status'])  # Count occurrences of each age
# plt.xlabel("Marital Status")
# plt.ylabel("Count of People")
# plt.title("Marital Status Distribution")
# plt.show()

#d) #Count Plot
# plt.figure(figsize=(10,15))
# sns.countplot(x=df['education'])  # Count occurrences of each age
# plt.xlabel("Education")
# plt.ylabel("Count of People")
# plt.title("Education Distribution")
# plt.show()

#Pie Plot
# df['education'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 6))
# plt.title("Proportion of Education Levels Among Clients")
# plt.ylabel("")  # Hide default ylabel
# plt.show()

#e)
# print("Part E")
# dY = df['default'].value_counts(normalize=True).get('yes') *100
# print("Percentage of clients who are in default are: ",dY,'%')
# print("The total number of clients in default are: ",df['default'].value_counts().get('yes'))
# print()
#f) Check Again
# plt.figure(figsize=(10, 6))
# sns.histplot(df['balance'], bins=30, kde=True)  # kde=True adds a density curve
# plt.xlabel("Average Yearly Balance")
# plt.ylabel("Number of Clients")
# plt.title("Distribution of Average Yearly Balance Among Clients")
# plt.show()
#G)
# print('Part G')
# print("Total Number of Clients having Housing Loan: ",df['housing'].value_counts().get('yes'))
# print()
#H)
# print('Part H')
# print("Total Number of Clients having Personal Loan: ",df['loan'].value_counts().get('yes'))
# print()
#I)
# print("Part I")
# print("The different types of communication modes are:")
# for i in df['contact'].unique():
#     if(i!='unknown'):
#         print(i.capitalize())
# print()
#J)
#May-2008 -- Nov-2010; Feb passed in 2008 so no leap year needs to be considered
# last_days = (31,28,31,30,31,30,31,31,30,31,30,31)
# unique_months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
# last_days_months = []
# for i in range(12):
#     last_days_months.append(str(last_days[i])+'-'+unique_months[i])
# # print(last_days_months)
# count_ldm = []
# for i in last_days_months:
#     count_ldm.append(int(df['day_month'].value_counts().get(i,0)))
# # print(count_ldm)
# plt.figure(figsize=(20,10))
# sns.barplot(x=last_days_months,y=count_ldm)
# plt.xlabel('Last Days of Months')
# plt.ylabel('Number of Clients Contacted')
# plt.title('')

#Part K
# plt.figure(figsize=(12, 8))
# sns.countplot(x = df['day'])
# plt.xlabel("Last Contact Day of the Month")
# plt.ylabel("Number of Clients Contacted")
# plt.title("Distribution of Last Contact Day Across Different Months")
# plt.show()
#Part L
# plt.figure(figsize=(12, 8))
# sns.countplot(x = df['month'])
# plt.xlabel("Last Contact Month")
# plt.ylabel("Number of Clients Contacted")
# plt.title("Distribution of Last Contact Month")
# plt.show()

# months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
# numCM = []
# for i in months:
#     numCM.append(df['month'].value_counts().get(i.lower()))
# plt.figure(figsize=(12,8))
# sns.barplot(x=months,y=numCM)
# plt.xlabel("Last Contact Month")
# plt.ylabel("Number of Clients Contacted")
# plt.title("Distribution of Last Contact Month")
# plt.show()
#Next Part
#print("The below data can be extracted from the duration of contact:")
#print(df['duration'].describe())
# plt.figure(figsize=(12,8))
# sns.kdeplot(df['duration'],shade=True)
# plt.xlabel('Duration of Contact(seconds)')
# plt.ylabel('Density')
# plt.title('Distribution of Duration of Contact')
# plt.show()
#Next Part
# print(df['campaign'].describe())
# times_contacted =  df['campaign'].value_counts().sort_index()
# print(times_contacted)

# plt.figure(figsize=(10,5))
# sns.histplot(df['campaign'], bins=15, kde=True)
# plt.xlabel("Number of Contacts")
# plt.ylabel("Number of Clients")
# plt.title("Distribution of Contacts per Client")
# plt.show()

#Next Part
# filtered_acc_pdays = df[df['pdays'] != -1]  #To Remove -1 values
# filteredDays= filtered_acc_pdays['pdays']
# print(filteredDays.describe())
# print(filteredDays.unique())
# plt.figure(figsize=(10,5))
# sns.histplot(filteredDays, bins=15, kde=True)
# plt.xlabel("Number of Days Passed Since Client was Last Contacted since Previous Campaign")
# plt.ylabel("Number of Clients")
# plt.title("Distribution of Number of Days Passed since Client Was Last Contacted")
# plt.show()

#And the next part
# print(df['previous'].describe())
# plt.figure(figsize=(10,5))
# sns.histplot(df[df['previous'] != 0]['previous'], bins=30, kde=True)
# plt.xlabel("Number of Times Contacted Last Time")
# plt.ylabel("Number of Clients")
# plt.title("Distribution of Number of Clients Contacted Last Time (Excluding 0)")
# plt.show()

#Previous Outcomes
previousOutcomeBrackets = df['poutcome'].unique()
#print(previousOutcomeBrackets)
print('Previous Outcomes')
for i in range(len(previousOutcomeBrackets)):
    print(previousOutcomeBrackets[i]+' : '+str(df['poutcome'].value_counts().get(previousOutcomeBrackets[i])))
#Next Part
tdyes = df['y'].value_counts(normalize=True).get('yes')
tdno = k = df['y'].value_counts(normalize=True).get('no')
print('Percentage of people subscribing to a term deposit : ',tdyes)
print('Percentage of people not subscribing to a term deposit : ',tdno)

####Last Part
print(df.columns)
print(df.dtypes)
#One Hot Encoding
df = pd.get_dummies(df, columns=['job', 'marital', 'marital_status', 'education', 'month', 'contact', 'poutcome'], drop_first=True)
df[df.select_dtypes(include='bool').columns] = df.select_dtypes(include='bool').astype(int)
#Classification
df['y'] = df['y'].map({'yes': 1, 'no': -1}).astype(int)
df[['housing', 'loan', 'default']] = df[['housing', 'loan', 'default']].applymap(lambda x: 1 if x == 'yes' else 0).astype(int)
#Normalisation
scaler = StandardScaler()
df[['age', 'balance','duration','campaign','previous']] = scaler.fit_transform(df[['age', 'balance','duration','campaign','previous']])
df.loc[df['pdays'] != -1, 'pdays_normalized'] = scaler.fit_transform(df.loc[df['pdays'] != -1, ['pdays']])

print(df.columns)
print(df.dtypes)
df.select_dtypes(include=[np.number]).corr().to_csv("correlation_matrix.csv")
# plt.figure(figsize=(12, 8))
# sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt=".2f")
# plt.show()


correlation_with_y = df.select_dtypes(include=[np.number]).corr()['y'].drop('y')
correlation_with_y.sort_values().plot(kind='barh', figsize=(8, 6), cmap='coolwarm')
plt.title("Correlation of Features with Target (y)")
plt.show()