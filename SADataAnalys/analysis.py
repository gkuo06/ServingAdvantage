import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np 
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


def sentimentAnalysis(undetermined):
    undetermined_static = undetermined
    nltk.download('punkt')
    #Start with text processing
    #Lower and remove punctuation
    undetermined = [sentence.lower().translate(str.maketrans('', '', string.punctuation)) for sentence in undetermined]

    #Remove stop words
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    undetermined = [' '.join([word for word in word_tokenize(sentence) if word.lower() not in stop_words]) for sentence in undetermined]

    #Lemmatizeation
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    undetermined = [' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(sentence)]) for sentence in undetermined]

    #Tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle) 
    undetermiend_sequences = tokenizer.texts_to_sequences(undetermined) 

    #Pad sequences
    max_length = 15
    padded_sequences = pad_sequences(undetermiend_sequences, maxlen=max_length, padding='post')
    
    #Load ML model
    model = load_model('sentiment_analysis_ML')

    #Predict rating
    predictions = model.predict(padded_sequences)

    #Test print
    #print(predictions)

    #Determine sentiment and classify
    predictions_list = predictions.tolist()
    pos = []
    neg = []
    for i in range(len(predictions_list)):
        if predictions_list[i][0] > 0.5:
            pos.append(undetermined_static[i])
        else:
            neg.append(undetermined_static[i])

    return pos, neg