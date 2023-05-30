from keras.models import load_model

PATH_TO_MODEL = "model/kanji_ocr.h5"

model = load_model(PATH_TO_MODEL)
