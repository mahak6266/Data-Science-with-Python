# Q1 Create a model that can predict that the customer has purchase item or not based on features given in the dataset. Use appropriate 
# evaluation metrics. 

import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

path = kagglehub.dataset_download("d4rklucif3r/social-network-ads")

print("Path to dataset files:", path)
df = pd.read_csv(path +"/Social_Network_Ads.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())

x = df[['Age', 'EstimatedSalary']]
y = df['Purchased']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print("Confusion Matrix:/n ", conf_matrix)
