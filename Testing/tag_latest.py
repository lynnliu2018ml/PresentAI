import pandas as pd
import nltk

from nltk import word_tokenize, pos_tag, pos_tag_sents
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


path2='C:\\Users\\Andy\\Desktop\\ML1010\\Assignment\\HealthNewsTweets_cleaned.csv'

df=pd.read_csv(path2)
df.columns = ['tweet']
text=df
#remove numbers
trans_dict = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "0": ""}
trans_table ="1234567890".maketrans(trans_dict) 
text["tweet"]= text["tweet"].str.translate(trans_table) 


#combine tokenize and tagging function

tok_and_tag = lambda x: pos_tag(word_tokenize(x))
#tokenize and tag sentences, remove NAs

tagtext=text["tweet"].fillna("").map(tok_and_tag)

''' still needs work  
tagtext[i][j][1] gives the tage for row i word j
tags from pos_tag does not match WordNetLemmatizer need to change it
 
replace() doesn't work here for some reason
for i in range(0,len(tagtext)):
        for j in range(0,len(tagtext[i])): 
            if tagtext[i][j][1].startswith('J'):                
                tagtext.replace(tagtext[i][j][1],wordnet.ADJ)                
            elif tagtext[i][j][1].startswith('V'):
                tagtext.replace(tagtext[i][j][1],wordnet.VERB)             
            elif tagtext[i][j][1].startswith('N'):
                tagtext.replace(tagtext[i][j][1],wordnet.NOUN)
            elif tagtext[i][j][1].startswith('R'):
                tagtext.replace(tagtext[i][j][1],wordnet.ADV)
            else:
                tagtext.replace(tagtext[i][j][1],wordnet.NOUN) #noun is default
                
lemmatizer=WordNetLemmatizer                
for i in range(0,len(tagtext)):
        for j in range(0,len(tagtext[i])): 
            lemma=lemmatizer.lemmatize(tagtext[i][j][0], pos=tagtext[i][j][1])    


foudn this bit  form stack overflow but it doesn't work
rename pos_tag
def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None # for easy if-statement    

from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
tagged = nltk.pos_tag(tokens)
for word, tag in tagtext:
    wntag = get_wordnet_pos(tag)
    if wntag is None:# not supply tag in case of None
        lemma = lemmatizer.lemmatize(word) 
    else:
        lemma = lemmatizer.lemmatize(word, pos=wntag)            
