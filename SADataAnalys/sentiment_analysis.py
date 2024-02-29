import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #Tensorflow logs all messages except INFO and WARNING to clear unnecessary clutter from the console

import pandas as pd #Imported to read Dataset CSV File using variables {zip_file_path} and {csv_file_path}
from sklearn.model_selection import train_test_split
import zipfile
import numpy as np

#All TensorFlow imports
import tensorflow as tf
from tensorflow import keras #Keras is a high-level API for TensorFlow that helps us build and train deep learning models
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D, Dropout, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#File paths where the zip and csv files are located on PC
#Twitter 1.6mil Sentiment Analysis Dataset (Kaggle)
zip_file_path = '/mnt/c/Users/garok/Downloads/archive.zip'
csv_file_name = 'training.1600000.processed.noemoticon.csv'

#Open the zip file using zipfile library
#Open the csv file
#Read csv file using pandas
with zipfile.ZipFile(zip_file_path) as z:
    with z.open(csv_file_name) as csv_file:
        df = pd.read_csv(csv_file, dtype=str, header=None, encoding='ISO-8859-1')
        labels = df[0].astype(int) #First column of csv
        texts = df[5].astype(str) #Sixth column of csv

#Test size of 20% of the entire dataset
train_text, test_text, train_label, test_label = train_test_split(texts, labels, test_size=0.2, random_state=42)

#Set words to tokens
vocab_size = 500000
tokenizer = Tokenizer(num_words=vocab_size, lower=True, oov_token='8==D')
tokenizer.fit_on_texts(train_text)

#String sequences into tokenized lists
train_sequences = tokenizer.texts_to_sequences(train_text)
test_sequences = tokenizer.texts_to_sequences(test_text)

#Pad with max word length of 20
#Most tweets < 25-30 words
max_length = 20
type = 'post'
train_sequences_padded = pad_sequences(train_sequences, maxlen=max_length, padding=type, value=0)
test_sequences_padded = pad_sequences(test_sequences, maxlen=max_length, padding=type, value=0)

'''
#Print to test
print(f'Train Sequence Text Head:\n{train_sequences_padded[1:9]}')
print(f'Test Sequence Test Head:\n{test_sequences_padded[1:9]}', end='\n\n')
print(f'Translated Train Text:\n{tokenizer.sequences_to_texts(train_sequences_padded[1:9])}')
print(f'Translated Test Text:\n{tokenizer.sequences_to_texts(test_sequences_padded[1:9])}')
'''

#Initialize model
sentiment_analysis_model = Sequential()

#Add conditions and other funny haha stuff here
embeddings = 128
sentiment_analysis_model.add(Embedding(vocab_size, embeddings, input_length=max_length))

sentiment_analysis_model.add(GlobalAveragePooling1D()) # Averages all embeddings in a sequence

#Layers
#256 -> 128 -> 64 -> 32 -> 16 -> 1 (output)
#Currently in testing phase WILL BE CHANGED
sentiment_analysis_model.add(Dense(1024, activation="relu"))
sentiment_analysis_model.add(Dense(512, activation="relu"))
sentiment_analysis_model.add(Dense(256, activation="relu"))
sentiment_analysis_model.add(Dense(128, activation="relu"))
sentiment_analysis_model.add(Dense(64, activation="relu"))
sentiment_analysis_model.add(Dense(32, activation="relu"))
sentiment_analysis_model.add(Dense(16, activation="relu"))
sentiment_analysis_model.add(Dense(8, activation="relu"))
sentiment_analysis_model.add(Dense(4, activation="relu"))
sentiment_analysis_model.add(Dense(2, activation="relu"))

#Final output
sentiment_analysis_model.add(Dense(1, activation="sigmoid"))

sentiment_analysis_model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

#Model training
sentiment_analysis_model.fit(train_sequences_padded, train_label, epochs=5, 
                             batch_size=32, validation_data=(test_sequences_padded, test_label))

loss, accuracy = sentiment_analysis_model.evaluate(test_sequences_padded, test_label)
print(f"Accuracy score: {accuracy*100}")

