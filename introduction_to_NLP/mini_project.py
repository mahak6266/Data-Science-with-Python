'''
Create a model that will predict the rating based on the feedback of the customer.
Feature: Text
Label: Stars
Dataset: yelp.csv'''

import kagglehub
import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
nltk.download('stopword')

path = kagglehub.dataset_download("sheikhraselahmed/yelpcsv")
print("Path to dataset files:", path)

def textprocessing(data):
    remove_pun = [c for c in  data if c not in string.punctuation]
    sentence = ''.join(remove_pun)
    words = sentence.split(" ")
    vocabulary = [word for word in words if word not in  stopwords.words("english")]
    return vocabulary

df = pd.read_csv(path+"/yelp.csv")

wordVector = CountVectorizer(analyzer=textprocessing)
finalWordVector = wordVector.fit(df["text"])
finalWordVector.vocabulary_
bow = finalWordVector.transform(df["text"])
print(bow)
tfidobject = TfidfTransformer.fit(bow)
final_text = tfidobject.transform(bow)
print(final_text)
df = df.concat([df, final_text], axis = 1)

x = df['final_text']
y = df['stars']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
tfidf_vectorizer = TfidfVectorizer(max_features=5000) 
X_train_tfidf = tfidf_vectorizer.fit_transform(x_train)
X_test_tfidf = tfidf_vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", report)
