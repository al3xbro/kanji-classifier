import tensorflow as tf
import keras

model = keras.models.load_model("model/kanji_ocr.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_model = converter.convert()

with open("model/kanji_ocr.tflite", "wb") as f:
    f.write(tflite_model)