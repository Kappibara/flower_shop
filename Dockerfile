FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev gcc \
                            libffi-dev openssl-dev
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py db init
ENV DATABASE_URL postgres://postgres:postgres@database:5432/flower_shop
ENV FLASK_APP=run.py
EXPOSE 5000