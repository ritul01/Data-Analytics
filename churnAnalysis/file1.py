import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Churn.csv')
df["TotalCharges"]=df["TotalCharges"].replace(" ","0")
df["TotalCharges"]=df["TotalCharges"].astype("float")
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())
# print(df.duplicated().sum())

# converted 0 and 1 value of senior citizen to yes/no to amke it easier to understand
def convert(val):
    if val==1:
        return "Yes"
    else:
        return "No"
df['SeniorCitizen']=df['SeniorCitizen'].apply(convert)

# print(df.head(20))
# ax=sns.countplot(x='Churn',data=df)
# ax.bar_label(ax.containers[0])
# plt.title("Count of Customers by Churn")

# plt.figure(figsize=(3,4))
# gb=df.groupby("Churn").agg({'Churn':"count"})
# plt.pie(gb['Churn'],labels=gb.index,autopct="%1.2f%%")
# plt.title("Percentage of Churned Customers", fontsize=10)

# plt.figure(figsize=(3,3))
# sns.countplot(x="gender",data=df,hue="Churn")
# plt.title("Churn by Gender")


# plt.figure(figsize=(3,3))
# sns.countplot(x="SeniorCitizen",data=df)
# ax.bar_label(ax.containers[0])
# plt.title("Churn by Senior Citizens")

# print(plt.show())


# plt.figure(figsize=(8, 6))

# # Create a stacked bar chart with sns.histplot
# ax = sns.histplot(
#     data=df,
#     x="SeniorCitizen",
#     hue="Churn",
#     multiple="fill",    # Stacks bars to show percentage fill
#     shrink=0.8,         # Adjusts bar width
#     stat="probability"  # Scales the y-axis to probability (percentage)
# )

# # Adding percentages on each bar
# for c in ax.containers:
#     labels = [f'{v.get_height() * 100:.1f}%' for v in c]
#     ax.bar_label(c, labels=labels, label_type='center')

# # Add titles and labels
# plt.title("Churn by Senior Citizens")
# plt.xlabel("Senior Citizen")
# plt.ylabel("Percentage")


# plt.figure(figsize=(9,4))
# sns.histplot(x='tenure',data=df,bins=72,hue="Churn")


# plt.figure(figsize=(4,4))
# ax=sns.countplot(x="Contract",data=df,hue="Churn")
# ax.bar_label(ax.containers[0])
# plt.title("Count of Customers by Contract")


# plt.show()


# print(df.columns.values)


# columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# # Set up the figure size and the layout for subplots
# plt.figure(figsize=(15, 12))

# # Loop over each column and create a subplot for it
# for i, column in enumerate(columns, 1):
#     plt.subplot(3, 3, i)  # 3x3 grid for 9 subplots
#     sns.countplot(data=df, x=column,hue='Churn')
#     plt.title(f'Count of {column}')
#     plt.xticks(rotation=45)
#     plt.ylabel('Count')
#     plt.xlabel('')

# # Adjust layout and show the plot
# plt.tight_layout()
# plt.show()


plt.figure(figsize=(8,6))
ax=sns.countplot(x="PaymentMethod",data=df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Count of Customers by Payment Method")
plt.xticks(rotation=45)

print(plt.show())