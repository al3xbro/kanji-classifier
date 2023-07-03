FROM tensorflow/tensorflow:2.12.0

WORKDIR /app

COPY requirements.txt .
COPY server.py .
COPY kanji_ocr.tflite .
COPY label_keys.csv .

EXPOSE 8000

RUN  pip install -r requirements.txt 

CMD [ "python", "server.py" ]