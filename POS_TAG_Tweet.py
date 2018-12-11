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

path2='Dataset\\HealthNewsTweets_cleaned.csv'

df=pd.read_csv(path2)
df.columns = ['sent']
print(df.head(5))

#remove numbers
#trans_dict = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "0": ""}
#trans_table ="1234567890".maketrans(trans_dict)
#df["sent"]= df["sent"].str.translate(trans_table)



df = pd.read_csv(path2)#, delimiter=';')
df.columns = ['sent']

tok_and_tag = lambda x: pos_tag(word_tokenize(x))




df['lower_sent'] = df['sent'].str.lower()
df['lower_sent'].dropna(inplace=True)
df['tagged_sent'] = df['lower_sent'].apply(tok_and_tag)
df['tagged_sent'].dropna(inplace=True)
possible_tags = sorted(set(list(zip(*chain(*df['tagged_sent'])))[1]))

def add_pos_with_zero_counts(counter, keys_to_add):
    for k in keys_to_add:
        counter[k] = counter.get(k, 0)
    return counter


# Detailed steps.
df['tagged_sent'].dropna(inplace=True)
df['pos_counts'] = df['tagged_sent'].apply(lambda x: Counter(list(zip(*x))[1]))
df['pos_counts'].dropna(inplace=True)
df['pos_counts_with_zero'] = df['pos_counts'].apply(lambda x: add_pos_with_zero_counts(x, possible_tags))
df['pos_counts_with_zero'].dropna(inplace=True)
df['sent_vector'] = df['pos_counts_with_zero'].apply(lambda x: [count for tag, count in sorted(x.most_common())])
df['sent_vector'].dropna(inplace=True)
df['tagged_sent'].dropna(inplace=True)
# All in one.
df['sent_vector'] = df['tagged_sent'].apply(lambda x:
    [count for tag, count in sorted(
        add_pos_with_zero_counts(
            Counter(list(zip(*x))[1]),
                    possible_tags).most_common()
         )
    ]
)
df['sent_vector'].dropna(inplace=True)
df2 = pd.DataFrame(df['sent_vector'].tolist())
df2.columns = possible_tags

df2["tweet"] = df['lower_sent']

print(df2.head(100))