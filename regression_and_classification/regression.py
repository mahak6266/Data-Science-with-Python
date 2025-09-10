# Q1 predict the price of the car based on its features. Use appropriate evaluation metrice. Dataset : car.csv
'''
import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Download latest version
path = kagglehub.dataset_download("osama12bin/cars-csv")

print("Path to dataset files:", path)
car = pd.read_csv(path +"/cars.csv")

print(car.head(10))
print(car.info())
print(car.isnull().sum())
print(car.describe())
car_data_encoded = pd.get_dummies(car, columns=['brand', 'fuel', 'owner'], drop_first = True)
x = car_data_encoded.drop('selling_price', axis=1)
y = car_data_encoded['selling_price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_absolute_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.sf}")


# Q2 Create a model that can predict the profit based on the features. Use appropriate evaluation metrice. Datadset : 50_startups.csv

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Download latest version
path = kagglehub.dataset_download("gaurav9712/50-startups")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/50_startups.csv")
print(df.head(10))
print(df.info())
print(df.describe())

startup_data_encoded = pd.get_dummies(df, columns=['State'], drop_first = True)
x = startup_data_encoded.drop('Profit', axis=1)
y = startup_data_encoded['Profit']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_absolute_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
'''
# Q3 Create a model that can predict the profit based on the features. Use appropriate evaluation metrice. Datadset : Salary_Data

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Download latest version
path = kagglehub.dataset_download("mohithsairamreddy/salary-data")

print("Path to dataset files:", path)
df = pd.read_csv(path +'/salary_data.csv')
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())

startup_data_encoded = pd.get_dummies(df, columns=['Gender', 'Education Level', 'Job Title'], drop_first = True)
x = startup_data_encoded.drop('Salary', axis=1)
y = startup_data_encoded['Salary']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_absolute_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")