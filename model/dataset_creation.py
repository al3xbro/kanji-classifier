import tensorflow as tf
from tensorflow import keras

import os

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")
PREDICT_PATH = config.get("Paths", "PREDICT_PATH")
TRAINING_IMAGES_PATH = config.get("Paths", "TRAINING_IMAGES_PATH")
UNPROCESSED_IMAGES_PATH = config.get("Paths", "UNPROCESSED_IMAGES_PATH")

# configures memory growth
gpus = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(gpus[0], True)
except:
    pass

BATCH_SIZE = 10

# generates a csv file that contains all labels
class_file = open(CLASS_PATH, "w")
class_keys = sorted(os.listdir(TRAINING_IMAGES_PATH))
class_file.write(",".join(class_keys))

print("\n====================================================================")
print("Creating training set\n")

# returns a tf.data.Dataset object with tuple (images, labels)
# where images has shape (10, 92, 92, 1),
# and labels are an int32 tensor of shape (batch_size,)
training_set = keras.preprocessing.image_dataset_from_directory(
    TRAINING_IMAGES_PATH,
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    image_size=(92, 92),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="training"
)

print("\n====================================================================")
print("Creating validation set\n")

validation_set = keras.preprocessing.image_dataset_from_directory(
    TRAINING_IMAGES_PATH,
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    image_size=(92, 92),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="validation"
)
