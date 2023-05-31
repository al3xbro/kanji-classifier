import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, PReLU

from dataset_creation import training_set
from dataset_creation import validation_set

MODEL_PATH = "model/kanji_ocr.h5"
EPOCHS = 4

print("\n====================================================================")
print("Training model\n")
model = Sequential()

model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(92, 92, 1)))
model.add(BatchNormalization())
model.add(PReLU())
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Conv2D(32, (3, 3), 1, activation='relu'))
model.add(BatchNormalization())
model.add(PReLU())
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(6000, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(3040, activation='sigmoid'))

model.compile("adam", loss=tf.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

print("\n====================================================================")
print("Training\n")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
hist = model.fit(training_set, epochs=EPOCHS,
                 validation_data=validation_set, callbacks=[tensorboard_callback])

model.save(MODEL_PATH)
