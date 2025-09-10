# Q1  Perform text prepocessing on SMSSpamCollecion Dataset. 

import kagglehub
import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
nltk.download('stopword')

def textprocessing(data):
    remove_pun = [c for c in  data if c not in string.punctuation]
    sentence = ''.join(remove_pun)
    words = sentence.split(" ")
    vocabulary = [word for word in words if word not in  stopwords.words("english")]
    return vocabulary
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Path to dataset files:", path)

df = pd.read_csv(path +"/spam.csv")    
wordVector = CountVectorizer(analyzer=textprocessing)
finalWordVector = wordVector.fit(df["v2"])
finalWordVector.vocabulary_
bow = finalWordVector.transform(df["v2"])
print(bow)
tfidobject = TfidfTransformer.fit(bow)
final_feature = tfidobject.transform(bow)
print(final_feature)

