import tensorflow as tf
import keras
from PIL import Image

import numpy as np

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

MODEL_PATH = "model/kanji_ocr.h5"
CLASS_PATH = "model/label_keys.csv"
IMAGE_PATH = "model/say.png"

class_file = open(CLASS_PATH, "r")
class_keys = class_file.read().split(",")
class_file.close()

im = Image.open(IMAGE_PATH)
print(im.getdata)
newImData = []
for pixel in im.getdata():
    if pixel < 237:
        newImData.append(1)
    else:
        newImData.append(0)

newIm = Image.new(im.mode, im.size)
newIm.putdata(newImData)

image_as_tensor = tf.convert_to_tensor(newIm)
image_as_tensor = tf.reshape(image_as_tensor, (1, 92, 92, 1))

model = keras.models.load_model(MODEL_PATH)
output = np.array(model(image_as_tensor, training=False))

print()
print(np.argmax(output))
print(chr(int(class_keys[np.argmax(output)], 16)))

file = open("bruh.txt", "w")
file.write("input:")
file.write(str(np.array(image_as_tensor)))
file.write("output:")
file.write(str(np.array(output)))
file.close()
