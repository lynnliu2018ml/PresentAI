import pandas as pd
import numpy as np
import re
import nltk
from string import digits
from sklearn.feature_extraction.text import CountVectorizer


wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')


remove_digits = str.maketrans('', '', digits)


def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I)

    doc = doc.lower()
    doc = doc.strip()
    doc = doc.translate(remove_digits)
    # tokenize document
    tokens = wpt.tokenize(doc)

    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]

    #filtered_tokens = [token for token in tokens if token == "000"]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    print("run")
    return doc


#Need to load gutenberg package

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers


text = strip_headers(load_etext(2701)).strip()
text2 = strip_headers(load_etext(3701)).strip()
labels = ['Moby Dick','Book2']
corpus = np.array([text,text2])
corpus_df = pd.DataFrame({'Document': corpus,
                          'Category': labels})
print(corpus_df.head())

#Tokenize words and clean them




normalize_corpus = np.vectorize(normalize_document)

norm_corpus = normalize_corpus(corpus)
#norm_corpus



# Run bag of words
cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(norm_corpus)
cv_matrix = cv_matrix.toarray()


# get all unique words in the corpus
vocab = cv.get_feature_names()
# show document feature vectors
print(pd.DataFrame(cv_matrix, columns=vocab))

