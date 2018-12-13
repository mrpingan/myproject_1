FROM python:3.5.2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt \
    && python manage_prod.py collectstatic --noinput


CMD ["uwsgi","--ini","django_uwsgi.ini"]


