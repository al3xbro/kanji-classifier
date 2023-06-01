import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, PReLU

from dataset_creation import training_set
from dataset_creation import validation_set
from config import MODEL_PATH, CLASS_PATH, PREDICT_PATH, TRAINING_IMAGES_PATH, UNPROCESSED_IMAGES_PATH

EPOCHS = 4

print("\n====================================================================")
print("Building model\n")
model = Sequential()

model.add(Conv2D(16, (5, 5), 1, activation='relu', input_shape=(92, 92, 1)))
model.add(BatchNormalization())
model.add(PReLU())
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Conv2D(32, (5, 5), 1, activation='relu'))
model.add(BatchNormalization())
model.add(PReLU())
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(6000, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(3040, activation='softmax'))

model.compile("adam", loss=tf.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.summary()

print("\n====================================================================")
print("Training\n")

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
model.fit(training_set, epochs=EPOCHS,
          validation_data=validation_set, callbacks=[tensorboard_callback])

model.save(MODEL_PATH)
