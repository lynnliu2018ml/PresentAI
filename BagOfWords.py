import pandas as pd
import numpy as np
import re
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer


# Wordnet is an large, freely and publicly available lexical database for the English language 
# aiming to establish structured semantic relationships between words. 
# It offers lemmatization capabilities as well and is one of the earliest and most commonly used lemmatizers.



wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I)
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

def Lemmitize(s):
    #nltk.download('wordnet') #Download this only for the first time
    from nltk.stem import WordNetLemmatizer
    # Init the Wordnet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_output = " ".join([lemmatizer.lemmatize(w) for w in s.split(" ")])
    return lemmatized_output
    
def RemoveNumbers(s):
    s = re.sub(r'\d+',' ', s)
    return s

def RemoveSpecialCharacters(s):
    return s.replace('_', ' ')

def RemoveUnicodeChars(s):
    #remove the ZERO WIDTH NO-BREAK SPACE unicode character
    s = s.replace(u'\ufeff', '')
    s = re.sub(r'[^\x00-\x7F]+',' ', s) #Replace non-ASCII characters with a single space
    return s

def GetBooks():
    folderPath = "txt/"
    files = os.listdir(folderPath)
    
    corpus = []
    labels = []
    for file in files:        
        with open(folderPath + file, encoding="utf8") as f:
            lines = f.readlines()
            long_string = " ".join(lines)
            long_string = normalize_document(long_string)
            long_string = RemoveUnicodeChars(long_string)
            long_string = RemoveNumbers(long_string)
            long_string = RemoveSpecialCharacters(long_string)
            long_string = Lemmitize(long_string) 
            long_string = " ".join(list(set(long_string.split(" ")))) #retain only the unique words
            book_name = file.split(".")[0] #extract the filename without the extension
            labels.append(book_name)
            corpus.append(long_string)
    corpus = np.array(corpus)
    corpus_df = pd.DataFrame({'Document': corpus, 'Category': labels})
    corpus_df = corpus_df[['Document', 'Category']]
    return corpus_df

corpus_df = GetBooks()
print(GetBooks().head(10))


 
#Bag of Words Model
cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(corpus_df["Document"])
cv_matrix = cv_matrix.toarray()
cv_matrix
 
vocab = cv.get_feature_names()
print(pd.DataFrame(cv_matrix, columns=vocab))
print(len(vocab))
#print(vocab)

with open("vocabulary.txt", "w") as f:
    f.write(re.sub(r',',',\n', str(vocab)))
    