import tensorflow as tf
from tensorflow import keras
import os

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

IMG_HEIGHT = 92
IMG_WIDTH = 92
BATCH_SIZE = 32
IMAGES_PATH = "data/images_processed"
CLASS_PATH = "model/label_keys.csv"

class_file = open(CLASS_PATH, "w")
class_keys = sorted(os.listdir(IMAGES_PATH))
class_file.write(",".join(class_keys))

print("\n====================================================================")
print("Creating training set\n")
training_set = keras.preprocessing.image_dataset_from_directory(
    IMAGES_PATH,
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="training"
)

print("\n====================================================================")
print("Creating validation set\n")
validation_set = keras.preprocessing.image_dataset_from_directory(
    IMAGES_PATH,
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="validation"
)
