FROM tensorflow/tensorflow:2.12.0

WORKDIR /app

COPY requirements.txt .
COPY server.py .
COPY kanji_ocr.h5 .
COPY label_keys.csv .

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY server.py ${LAMBDA_TASK_ROOT}

CMD [ "server.handler" ]