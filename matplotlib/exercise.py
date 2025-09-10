# Q1  perform Exploratory Data Anlaysis for the dataset Mall_customer. 

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download latest version
path = kagglehub.dataset_download("priyansh2904/mall-customer")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/Mall_Customers.csv")
print(df.head(10))
print(df.info())
print(df.describe())

plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Annual Income (k$)'], bins=10, kde=True)
plt.title('Distribution of Annual Income (k$)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Spending Score (1-100)'], bins=10, kde=True)
plt.title('Distribution of Spending Score (1-100)')
plt.xlabel('Spending Score (1-100)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(6, 5))
sns.countplot(x='Genre', data=df)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('count')
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df, hue='Genre')
plt.title('Annual Income (k$) vs Spending Score (1-100)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Age', y='Spending Score (1-100)', data=df, hue='Genre')
plt.title('Age vs Spending Score (1-100)')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Genre', y='Spending Score (1-100)', data=df)
plt.title('Genre vs Spending Score (1-100)')
plt.xlabel('Genre')
plt.ylabel('Spending Score (1-100)')
plt.show()


# Q2 perform Exploratory Data Anlaysis for the dataset salary_data.

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("mohithsairamreddy/salary-data")

print("Path to dataset files:", path)
df = pd.read_csv(path +'/salary_data.csv')
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Gender distribution", df['Gender'].value_counts())
print("Education distribution", df['Education Level'].value_counts())
print("Top 10 job title", df['Job Title'].value_counts().head(10))

plt.figure(figsize=(8, 6))
sns.histplot(df['Salary'], bins=10, kde=True)
plt.title('Distribution of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Years of Experience', y='Salary', data=df)
plt.title('Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Education Level', y='Salary', data=df)
plt.title('Education Level vs Salary')
plt.xlabel('Education Level')
plt.ylabel('Salary')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Salary', data=df)
plt.title('Gender vs Salary')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()

# Q2 perform Exploratory Data Anlaysis for the dataset salary_data.
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("d4rklucif3r/social-network-ads")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/Social_Network_Ads.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())


plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['EstimatedSalarye'], bins=10, kde=True)
plt.title('Distribution of EstimatedSalarye')
plt.xlabel('EstimatedSalarye')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.jointplot(x='Age', y='EstimatedSalary', data=df, kind='scatter')
plt.title('Age vs EstimatedSalary')
plt.xlabel('Age')
plt.ylabel('EstimatedSalary')
plt.show()


