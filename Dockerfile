FROM python:3.5.2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && python manage_prod.py collectstatic --noinput


CMD ["uwsgi","--ini","django_uwsgi.ini"]


