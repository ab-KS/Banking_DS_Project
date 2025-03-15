import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('banking_data.csv')
#Distribution of age among clients
# print(df['age'].unique())
sns.set_style('whitegrid')

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
print("Part E")
dY = df['default'].value_counts(normalize=True).get('yes') *100
print("Percentage of clients who are in default are: ",dY,'%')
print("The total number of clients in default are: ",df['default'].value_counts().get('yes'))
print()
#f) Check Again
plt.figure(figsize=(10, 6))
sns.histplot(df['balance'], bins=30, kde=True)  # kde=True adds a density curve
plt.xlabel("Average Yearly Balance")
plt.ylabel("Number of Clients")
plt.title("Distribution of Average Yearly Balance Among Clients")
plt.show()
#G)
print('Part G')
print("Total Number of Clients having Housing Loan: ",df['housing'].value_counts().get('yes'))
print()
#H)
print('Part H')
print("Total Number of Clients having Personal Loan: ",df['loan'].value_counts().get('yes'))
print()
#I)
print("Part I")
print("The different types of communication modes are:")
for i in df['contact'].unique():
    if(i!='unknown'):
        print(i.capitalize())
print()
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
plt.figure(figsize=(12, 8))
sns.countplot(x = df['day'])
plt.xlabel("Last Contact Day of the Month")
plt.ylabel("Number of Clients Contacted")
plt.title("Distribution of Last Contact Day Across Different Months")
plt.show()
#Part L
# plt.figure(figsize=(12, 8))
# sns.countplot(x = df['month'])
# plt.xlabel("Last Contact Month")
# plt.ylabel("Number of Clients Contacted")
# plt.title("Distribution of Last Contact Month")
# plt.show()
months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
numCM = []
for i in months:
    numCM.append(df['month'].value_counts().get(i.lower()))
plt.figure(figsize=(12,8))
sns.barplot(x=months,y=numCM)
plt.xlabel("Last Contact Month")
plt.ylabel("Number of Clients Contacted")
plt.title("Distribution of Last Contact Month")
plt.show()
