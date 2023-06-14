FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

COPY requirements.txt .
COPY server.py .
COPY kanji_ocr.tflite .
COPY label_keys.csv .

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY server.py ${LAMBDA_TASK_ROOT}

CMD [ "server.handler" ]