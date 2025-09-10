# Q1 Doenload the dta set and rename to cars.csv
# a. Import Pandas
# b. Import the cars dataset and store the pandas dataframe in the variable cars.
# c. Inspect the first 10 row of the dtaframe cars.
# d. Inspect the datafra\me cars by "printing" cars.
# e. Inspect the last 5 rows.
# f. Getv some meta information on our dataframe.

import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("osama12bin/cars-csv")
cars = pd.read_csv(path +'/cars.csv')
print(cars.head(10))
print(cars)
print(cars.tail(5))
print(cars.Info())

# Q2 Download 50 startups dataset
# a. Create dataframe using pandas 
# b. REad the datav from 50 startups.csv file and load into dataframe.
# c. check the statistical summary.
# d. Checkn for corelation coefficient between dependent and independent variables.

import pandas as pd 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("gaurav9712/50-startups")
df = pd.read_csv(path +"/50_startup.csv")
df.describe()
correlation_matrix = df.corr()
print(correlation_matrix)