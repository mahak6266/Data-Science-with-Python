''''
Dataset: melb data.csv
The dataset can be downloaded melb data.csv | Kaggle
Perform the following tasks:
1. Load the data in dataframe (Pandas)
2. Handle inappropriate data
3. Handle the missing data
4. Handle the categorical data'''

import pandas as pd

try:
    df = pd.read_csv('melb_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: melb_data.csv not found. Please ensure the file is in the correct directory.")
    exit()

print("\nInitial DataFrame Info:")
df.info()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
print("\nDataFrame Info after handling potential date type issues:")
df.info()

missing_values_count = df.isnull().sum()
print("\nMissing values before handling:")
print(missing_values_count[missing_values_count > 0])

numerical_cols = df.select_dtypes(include=['number']).columns
for col in numerical_cols:
    if df[col].isnull().any():
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df[col].isnull().any():
        mode_val = df[col].mode()[0]
        df[col].fillna(mode_val, inplace=True)
      

print("\nMissing values after handling:")
print(df.isnull().sum()[df.isnull().sum() > 0])


categorical_cols_to_encode = df.select_dtypes(include=['object']).columns

if not categorical_cols_to_encode.empty:
    df = pd.get_dummies(df, columns=categorical_cols_to_encode, drop_first=True) # drop_first avoids multicollinearity
    print("\nDataFrame Info after one-hot encoding categorical features:")
    df.info()
else:
    print("\nNo categorical columns found for one-hot encoding.")

print("\nFirst 5 rows of the processed DataFrame:")
print(df.head())