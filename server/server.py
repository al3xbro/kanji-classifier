import tensorflow as tf
import keras
import numpy as np
import cv2
import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
import matplotlib.pyplot as plt

from configparser import ConfigParser
config = ConfigParser()
config.read("../config.ini")
MODEL_PATH = os.path.join("..", config.get("Paths", "MODEL_PATH"))
CLASS_PATH = os.path.join("..", config.get("Paths", "CLASS_PATH"))

model = keras.models.load_model(MODEL_PATH)
class_file = open(CLASS_PATH, "r")
class_keys = class_file.read().split(",")
class_file.close()

app = FastAPI()

origins = [
    "http://localhost:5173" # change this later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):

    im = cv2.imdecode(np.frombuffer(file.file.read(), np.uint8), cv2.IMREAD_COLOR)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    file.close()

    for y in range(0, im.shape[0]):
        for x in range(0, im.shape[1]):
            if im[y][x] < 237:
                im[y][x] = 0
            else:
                im[y][x] = 1

    im = np.atleast_3d(im)
    im = tf.image.resize(im, [92, 92])
    im = np.expand_dims(im, 0)

    output = np.squeeze(model(im, training=False))
    sorted_prob = np.flipud(np.sort(output)[-5:]).tolist()
    sorted_char = []

    for i in np.flipud(np.argsort(output)[-5:]):
        sorted_char.append(chr(int(class_keys[i], 16)))
    for i in range(0, 5):
        sorted_prob[i] = "{:.2f}".format(sorted_prob[i])

    return {
        "predictions":sorted_char,
        "certainty":sorted_prob
    }
