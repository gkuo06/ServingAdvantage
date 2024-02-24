import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
from sklearn.model_selection import train_test_split
import zipfile
import io

import tensorflow as tf
from tensorflow import keras # Keras is a high-level API for TensorFlow that helps us build and train deep learning models
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist # Neural network testing
from tensorflow.keras.models import Sequential, load_model

zip_file_path = '/mnt/c/Users/garok/Downloads/archive.zip'
csv_file_name = "training.1600000.processed.noemoticon.csv"

with zipfile.ZipFile(zip_file_path) as z:
    with z.open(csv_file_name) as csv_file:
        df = pd.read_csv(csv_file, encoding='ISO-8859-1')

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

print(f"Test Data Head:\n{test_data.head()}",end="\n\n")
print(f"Train Data Head:\n{train_data.head()}")

sentiment_analysis_model = Sequential()

# Add conditions and other funny haha stuff here 
sentiment_analysis_model.add(Dense())