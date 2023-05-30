import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
import os

IMG_HEIGHT = 92
IMG_WIDTH = 92
BATCH_SIZE = 32
IMAGE_DIRECTORY = "data/images_processed"

label_keys = list(sorted(os.listdir(IMAGE_DIRECTORY)))

print("Creating training set")
training_set = keras.preprocessing.image_dataset_from_directory(
    IMAGE_DIRECTORY,
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

print("Creating testing set")
validation_set = keras.preprocessing.image_dataset_from_directory(
    IMAGE_DIRECTORY,
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
