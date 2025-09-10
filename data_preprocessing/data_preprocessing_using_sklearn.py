# perform data preprocessing on melb_data.csv dataset with statistical pwerspection.

import kagglehub
import numpy as np
import pandas as pd 
from  sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
path = kagglehub.dataset_download("gunjanpathak/melb-data")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/melb_data.csv")
print(df.head(10))
print(df.info())
print(df.isnull().sum())
for col in ['Price', 'Room', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'longtitute']:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace = True)
for col in ['Suburb', 'Address', 'Type', 'Method', 'SellerG', 'Regionname', 'CouncilArea']:
    if col in df.columns:
        df[col].fillna(df[col].mode(), inplace = True)
        
categorical_cols = ['Suburb', 'Type', 'Method', 'CouncilArea']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder_features = encoder.fit_transform(df[categorical_cols])
encoder_df = pd.DataFrame(encoder_features, columns=encoder.get_feature_names_out(categorical_cols))
df = df.drop(columns=categorical_cols)
df = df.concat([df, encoder_df], axis = 1)


