'''
Dataset: datasetExample.csv
Perform the following task:
1. Load the data in the DataFrame.
2. Detection of Outliers'''

import pandas as pd 
import numpy as np 

def outDetection(array):
    sorted (array)
    Q1,Q3  = np.percentile (array, [25,75]) 
    IQR = Q3-Q1 
    lr = Q1 (1.5* IQR) 
    ur = Q3 + (1.5* IQR)

    return lr, ur

df = pd.read_csv('DatasetExample.csv')
array = df.iloc[:[0]].values
lr, ur = outDetection(array)
import seaborn as sns 
sns.displot(array)
updated_array = array[(array>lr) & (array<ur)] 
sns.displot(updated_array)

lr1, ur1 = outDetection(updated_array)
final_arrray = updated_array[(updated_array>lr1) & (updated_array<ur1)] 
sns.displot(final_arrray)

