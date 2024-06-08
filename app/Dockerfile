FROM PYTHON:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r app/requirements.txt

COPY . /app

CMD bash -c "whuile true; do sleep 1; done"