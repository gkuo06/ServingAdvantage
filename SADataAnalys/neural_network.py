import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras # Keras is a high-level API for TensorFlow that helps us build and train deep learning models
from keras import layers
from keras.datasets import mnist # Import the MNIST dataset

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

(x_train, y_train), (x_test, y_test) = mnist.load_data() # Load the MNIST dataset
print(x_train.shape)
print(y_train.shape)