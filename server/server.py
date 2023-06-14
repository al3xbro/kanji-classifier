# CD INTO SERVER AND RUN uvicorn server:app --reload

from tensorflow import lite
from tensorflow import image as tfimage
import numpy as np
import cv2

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import uvicorn
import mangum

interpreter = lite.Interpreter(model_path="kanji_ocr.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

class_file = open("label_keys.csv", "r")
class_keys = class_file.read().split(",")
class_file.close()

app = FastAPI()
handler = mangum.Mangum(app)

origins = [
    "https://www.al3xbro.me"
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
    im = tfimage.resize(im, [92, 92])
    im = np.expand_dims(im, 0)
    
    interpreter.set_tensor(input_details[0]['index'], im)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0]

    print(type(output))
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
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)