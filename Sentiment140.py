import re
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

def cleanText(path2, cleanedPath):
    # Read the input file in path2 and write to cleaned file cleanedPath
    fp = open(path2,"rb") #read in binary mode 
    text = fp.read().decode('utf-8', 'ignore').lower() #decode it in utf-8. Wherever it doesn't work, ignore the word
    fp.close()
    
    fp = open(cleanedPath, "w+", encoding="utf-8")
    fp.write(str(text))
    fp.close()
    
# download the file from the following path 
# https://www.kaggle.com/kazanova/sentiment140/downloads/training.1600000.processed.noemoticon.csv/2
path2='Dataset/Sentiment140/training.1600000.processed.noemoticon.csv'
cleanedPath = "Dataset/Sentiment140/training.csv" 

# Clean up the input file of non-ascii characters
cleanText(path2, cleanedPath)    

# Read from the cleanedPath
df=pd.read_csv(cleanedPath)
df.columns = ["target","ids","date","flag","user","text"]
df = df[["target","text"]]
print(df.head(5))

print(df["target"].unique())
print(len(df[df["target"]==0]))
print(len(df[df["target"]==4]))


#delete tags "@Lynn"

# Remove the anchor tags
def removeTags(s):
    s = re.sub("@[a-zA-Z0-9_]+"," ", s) #remove the @<the word>
    s = re.sub("#[a-zA-Z0-9_]+"," ", s) #remove the #<the word>
    return s

df.columns = ["target","ids","date","flag","user","text"]
df["text"] = df["text"].apply(removeTags)

df.head(10)



