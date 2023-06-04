import uvicorn
from fastapi import FastAPI
import numpy as np
import tensorflow as tf
import keras

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
MODEL_PATH = config.get("Paths", "MODEL_PATH")
CLASS_PATH = config.get("Paths", "CLASS_PATH")

model = keras.models.load_model(MODEL_PATH)

class_file = open(CLASS_PATH, "r")
class_keys = class_file.read().split(",")
class_file.close()

kanjik = FastAPI()

@kanjik.post("/")
def predict(data:list):

    # data = an array of numbers, process im

    output = np.squeeze(model(im, training=False))
    sorted_prob = np.flipud(np.sort(output)[-5:]).tolist()
    sorted_char = []
    for i in np.flipud(np.argsort(output)[-5:]):
        sorted_char.append(chr(int(class_keys[i], 16)))
    
    return  {
        "predictions":sorted_char,
        "certainty":sorted_prob
    }

if __name__ == "__main__.py":
    uvicorn.run(kanjik, host="localhost", port=8000)