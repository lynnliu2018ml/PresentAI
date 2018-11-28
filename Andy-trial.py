
import nltk
from string import digits
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import string
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
#str.maketrans replace the first argument with second
remove_digits = str.maketrans('', '', digits)

wpt = nltk.WordPunctTokenizer()
#stop words, like the, their, or etc
stopWords = set(stopwords.words('english'))

greatexp = strip_headers(load_etext(1400)).strip()
oliver=strip_headers(load_etext(730)).strip()
meta=strip_headers(load_etext(5200)).strip() 


#lower case
greatexp=greatexp.lower()

  #tokenize words and phrases
phrasegreat = sent_tokenize(greatexp)
wordsgreat = word_tokenize(greatexp)
 
# list of stopwords
stopwords = set(stopwords.words('english'))

wordsFiltered = []
 

for w in wordsgreat:
    if w not in stopwords:
        wordsFiltered.append(w)
 
wordsFiltered=str(wordsFiltered)

#remove punctuation
for c in string.punctuation:
    wordsFiltered= wordsFiltered.replace(c,"")
#remove digits problem also removes apposterphies 
remove_digits = str.maketrans('', '', digits)
wordsFiltered = wordsFiltered.translate(remove_digits)

wordsFiltered = word_tokenize(wordsFiltered)

lm = WordNetLemmatizer()

lemfilter=[]
for lem in wordsFiltered:
    print(lm.lemmatize(wordsFiltered))


ps= PorterStemmer()
psfilter=[]

#lemmatize 
for i in range(0, len(wordsFiltered)):
    lemfilter.append(lm.lemmatize(wordsFiltered[i]))

#stemming
for j in range(0, len(wordsFiltered)):
    psfilter.append(ps.stem(wordsFiltered[j]))
#checking words
print(ps.stem(wordsFiltered[374]))
print(lm.lemmatize(wordsFiltered[406]))
wordsFiltered[586]

# count number of unique words
uniqueWordslm = [] 
for i in lemfilter:
      if not i in uniqueWordslm:
          uniqueWordslm.append(i)

# count number of unique words
uniqueWordsps = [] 
for i in psfilter:
      if not i in uniqueWordsps:
          uniqueWordsps.append(i)
          
# takes a very long time. not viable          
for doc in greatexp:
    tok_doc=nltk.word_tokenize(wordsFiltered)
    pos_tag_doc=nltk.pos_tag(tok_doc)
    lem=[]
    for i in range(len(tok_doc)):
        temp=lm.lemmatize(tok_doc[i])
        lem.append(temp)