from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import json
import pickle
import string

training_data = pickle.load(open("training_data", "rb"))
words = training_data['words']
classes = training_data['classes']
train_x = training_data['train_x']
train_y = training_data['train_y']
punc_dic = dict((ord(punct),None) for punct in string.punctuation)
stemmer = LancasterStemmer()

with open('intents.json') as json_data:
    intents = json.load(json_data)

def cleanUp(sentence):
    sentence_words = word_tokenize(sentence.lower())
    sentence_words = [word.translate(punc_dic) for word in sentence_words]
    while '' in sentence_words:
        sentence_words.remove('')
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bagOfWords(sentence, words):
    sentence_words = cleanUp(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    return(np.array(bag))

tf.reset_default_graph()
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('./model.tflearn')

def response(sentence):
    results = model.predict([bagOfWords(sentence, words)])
    results_index = np.argmax(results)
    tag = classes[results_index]

    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = intent['child']
            break
    return response
