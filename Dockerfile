FROM python:3.12.3-alpine3.19

WORKDIR /usr/src/app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

# Configuração para incluir o arquivo SQLite no contêiner
COPY projeto_escola/db/db.sqlite3 .

EXPOSE 8000

CMD python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000 --noreload
