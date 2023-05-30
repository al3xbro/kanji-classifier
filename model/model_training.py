import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

from dataset_creation import training_set
from dataset_creation import validation_set

MODEL_SAVE_PATH = "model/kanji_ocr.h5"

print("\n------------------------------------------------------")
print("Creating model")
model = Sequential()

model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(92, 92, 1)))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(6000, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3040, activation='sigmoid'))

model.compile("adam", loss=tf.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

print("\n------------------------------------------------------")
print("Training")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
hist = model.fit(training_set, epochs=4,
                 validation_data=validation_set, callbacks=[tensorboard_callback])

model.save(MODEL_SAVE_PATH)
