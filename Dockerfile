FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY config.docker ./config.ini
COPY grade_escolar ./grade_escolar

CMD [ "python", "app.py" ]