from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import json
import string
import numpy as np
import pickle
punc_dic = dict((ord(punct),None) for punct in string.punctuation)
words = []
classes = []
documents = []

with open('intents.json') as json_data:
    intents = json.load(json_data)

for intent in intents['intents']:
    pattern = intent['parent']
    w = word_tokenize(pattern)
    words.extend(w)
    documents.append((w, intent['tag']))
    classes.append(intent['tag'])

stemmer = LancasterStemmer()
words = [stemmer.stem(word.lower()) for word in words]
words = [word.translate(punc_dic) for word in words]
words = sorted(list(set(words)))
words.remove('')

#print(len(documents), "documents")
#print(len(classes), "tags", classes)
#print(len(words), "unique stemmed words", words)

training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    parent_words = doc[0]
    parent_words = [stemmer.stem(word.lower()) for word in parent_words]
    parent_words = [word.translate(punc_dic) for word in parent_words]
    while '' in parent_words:
        parent_words.remove('')
    for w in words:
        bag.append(1) if w in parent_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

training = np.array(training)
train_x = list(training[:,0])
train_y = list(training[:,1])

pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )
#print("data pickled successfully!")
