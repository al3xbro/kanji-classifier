import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, PReLU
from keras.callbacks import EarlyStopping

from dataset_creation import training_set
from dataset_creation import validation_set

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")
PREDICT_PATH = config.get("Paths", "PREDICT_PATH")
TRAINING_IMAGES_PATH = config.get("Paths", "TRAINING_IMAGES_PATH")
UNPROCESSED_IMAGES_PATH = config.get("Paths", "UNPROCESSED_IMAGES_PATH")

EPOCHS = 20

print("\n====================================================================")
print("Building model\n")

model = Sequential()

model.add(Conv2D(16, (5, 5), 1, activation='relu', input_shape=(92, 92, 1)))
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
model.add(Dropout(0.1))

model.add(Dense(2965, activation='softmax'))

model.compile("adam", loss=tf.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.summary()

print("\n====================================================================")
print("Training\n")

early_stopping = EarlyStopping(monitor='val_loss', patience=2, verbose=1, restore_best_weights=True)

model.fit(training_set, 
          epochs=EPOCHS, 
          validation_data=validation_set, 
          callbacks=[early_stopping]
)

model.save(MODEL_PATH)
