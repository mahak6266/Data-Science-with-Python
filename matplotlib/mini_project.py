'''
Perform Exploratory Data Analysis for the Diabetes Dataset.
Dataset: Diabetes.csv
Perform the following tasks:
1. Load the data in the DataFrame
2. Data Pre-processing
3. Handle the Categorical Data
4. Perform Uni-variate Analysis
5. Perform Bi-variate Analysis'''

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = kagglehub.dataset_download("akshaydattatraykhare/diabetes-dataset")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/diabetes.csv")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('Diabetes.csv')
    print("Dataset loaded successfully.")
    print(df.head())
except FileNotFoundError:
    print("Error: Diabetes.csv not found. Please ensure the file is in the correct directory or provide the full path.")
 
print("\nMissing values before pre-processing:")
print(df.isnull().sum())
cols_to_replace_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in cols_to_replace_zero:
    df[col] = df[col].replace(0, pd.NA) 
for col in cols_to_replace_zero:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing values after pre-processing:")
print(df.isnull().sum())
print("\nData types:")
print(df.info())
print("\nFirst 5 rows after handling (or confirming) categorical data:")
print(df.head())

df.hist(figsize=(12, 10))
plt.suptitle('Histograms of Numerical Features')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.columns[:-1]): 
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df[column])
    plt.title(f'Box plot of {column}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Features')
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Glucose', y='BMI', hue='Outcome', palette='viridis')
plt.title('Glucose vs BMI colored by Outcome')
plt.show()


plt.figure(figsize=(15, 10))
for i, column in enumerate(df.columns[:-1]):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(x='Outcome', y=column, data=df, palette='pastel')
    plt.title(f'{column} by Outcome')
plt.tight_layout()
plt.show()