import tensorflow as tf
from dataset_creation import training_set
from dataset_creation import validation_set
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

import numpy as np
from matplotlib import pyplot as plt

training_set_iterator = training_set.as_numpy_iterator()

model = Sequential()

model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(92, 92, 1)))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(6000, activation='relu'))
model.add(Dense(3040, activation='sigmoid'))

model.compile("adam", loss=tf.losses.SparseCategoricalCrossentropy,
              metrics=['accuracy'])

model.summary()
