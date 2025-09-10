# perform data preprocessing on melb_data.csv dataset using pandas .

import pandas as pd
df = pd.read_csv("melb_data.csv")
print(df.info)
print(df.isnull().sum)
print(df.describe())
df.dropna(subset=['YearBuild'], inplace=True)
df.drop(columns='Date')
for col in ['Price', 'Room', 'Bathroom', 'Bedroom2',  'Car', 'Landsize', 'BuildingArea',  'Lattitude', 'longtitute', 'Propertycount']:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace = True)
for col in ['Suburb', 'Address', 'Type', 'Method', 'SellerG', 'Regionname', 'CouncilArea']:
    if col in df.columns:
        df[col].fillna(df[col].mode(), inplace = True)

df["YearBuild"] = pd.to_numeric(df['YearBuild'], errors = 'coerce').astype('Int64')
for col in ['Suburb', 'Type', 'Method', 'CouncilArea']:
    df = pd.get_dummies(df, columns=['col'], drop_first=True)


    
