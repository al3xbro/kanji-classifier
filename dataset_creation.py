import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator

IMG_HEIGHT = 92
IMG_WIDTH = 92
BATCH_SIZE = 32

training_set = keras.preprocessing.image_dataset_from_directory(
    "data/images/ETL8G",
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="training"
)

validation_set = keras.preprocessing.image_dataset_from_directory(
    "data/images/ETL8G",
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    shuffle=True,
    seed=420,
    validation_split=0.10,
    subset="validation"
)
