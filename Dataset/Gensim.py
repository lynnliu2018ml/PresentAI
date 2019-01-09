#Download the pre-trained collection of word vectors based on 2 billion tweets, "glove.twitter.27B.zip" 
#from "http://nlp.stanford.edu/data/glove.twitter.27B.zip"
#Its 1.42GB

#convert that into word2vec format from glove format.
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = 'glove.6B.100d.txt'
word2vec_output_file = 'glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, word2vec_output_file)

#created a gensim model
from gensim.models import KeyedVectors
# load the Stanford GloVe model
filename = 'glove.6B.100d.txt.word2vec'
model = KeyedVectors.load_word2vec_format(filename, binary=False)


#use that model to compute the cosine similarity between 2 words.
#Closer the value of similarity is to 0, dissimilar the words are
#Closer the value of similarity to 1, higher the degree of similarity between the words

print(model.similarity("good","great"))
print(model.similarity("good","monday"))
print(model.similarity("good","bad"))

