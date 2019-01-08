from glove import Corpus, Glove


import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
from sklearn.model_selection import train_test_split

def get_w2v_general(tweet, size, vectors, aggregation='mean'):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in tweet.split():
        try:
            vec += vectors[word].reshape((1, size))
            count += 1.
        except KeyError:
            continue
    if aggregation == 'mean':
        if count != 0:
            vec /= count
        return vec
    elif aggregation == 'sum':
        return vec
df = pd.read_csv('C:\\Users\\tblakeley\\Documents\\GitHub\PresentAI\\Dataset\\training_cleaned.csv')

df.head()
df_new = df.loc[df['Tweet'].apply(type) == str].copy()
df_new['Tweet_Clean'] = df_new['Tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)> 1]))

df_new.head()

import gensim.downloader as api

glove_twitter = api.load("glove-twitter-200")


X_train, X_test, y_train, y_test = train_test_split(df_new['Tweet'], df_new['Sentiment'], test_size=0.1, random_state=37)

X_train.head(1)

glove_twitter["cat"].reshape(1,200)



for i in X_train.head(1):
    print(get_w2v_general(i,200,glove_twitter,'mean'))











