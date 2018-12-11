import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk import word_tokenize, pos_tag, pos_tag_sents
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#nltk.download('averaged_perceptron_tagger')
from collections import Counter
from itertools import chain


import pandas as pd
from nltk import word_tokenize, pos_tag

# Clean up the input file of non-ascii characters


# download the file from the following path 
# https://www.kaggle.com/kazanova/sentiment140/downloads/training.1600000.processed.noemoticon.csv/2
path2='Dataset/Sentiment140/training.1600000.processed.noemoticon.csv'
cleanedPath = "Dataset/Sentiment140/training.csv" 
string = ""
fp = open(path2,"rb")
text = fp.read().decode('utf-8', 'ignore').lower()
fp.close()

fp = open(cleanedPath, "w+", encoding="utf-8")
fp.write(str(text))
fp.close()


df=pd.read_csv(cleanedPath)
df.columns = ["target","ids","date","flag","user","text"]
df = df[["target","text"]]
print(df.head(5))

print(df["target"].unique())
print(len(df[df["target"]==0]))
print(len(df[df["target"]==4]))


#delete tags "@Lynn"

import re

def removeTags(s):
    s = re.sub("@[a-zA-Z0-9_]+"," ", s)
    return s

df.columns = ["target","ids","date","flag","user","text"]
df["text"] = df["text"].apply(removeTags)

df.head(10)



